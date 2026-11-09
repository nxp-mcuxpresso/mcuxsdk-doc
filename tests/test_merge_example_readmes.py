"""Regression coverage for merged example board selectors.

Copyright 2026 NXP
SPDX-License-Identifier: Apache-2.0
"""

import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_extensions"))

import merge_example_readmes as merge
from board_names import aliases, normalize
from sphinx.application import Sphinx


class MergeReadmesTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(dir=Path(__file__).parent)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.examples = self.root / "examples"
        self.common = self.examples / "usb_examples" / "cdc"
        self.common.mkdir(parents=True)
        self.readme = self.common / "readme.md"
        self.deleted = set()

    def board(self, directory, variant="", body="# Setup\nSet JP1 to 1-2.\n"):
        target = (self.examples / "_boards" / directory / "usb_examples" /
                  "cdc" / variant / "example_board_readme.md")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(body, encoding="utf-8")
        return target

    def board_page(self, directory, title):
        index = self.root / "boards" / "family" / directory / "index.rst"
        index.parent.mkdir(parents=True, exist_ok=True)
        index.write_text(f"{title}\n{'#' * len(title)}\n", encoding="utf-8")

    def link(self, name, directory, variant=""):
        middle = f"{variant}/" if variant else ""
        return (f"[{name}](../../_boards/{directory}/usb_examples/cdc/"
                f"{middle}example_board_readme.md)")

    def write(self, entries, tail="", heading="## Supported Boards"):
        self.readme.write_text(
            "# CDC\n\nCommon instructions.\n\n" + heading + "\n" +
            "\n".join(f"- {entry}" for entry in entries) + "\n" + tail,
            encoding="utf-8")

    def run_merge(self):
        result = merge._merge_one(self.readme, self.examples, self.deleted)
        return result, self.readme.read_text(encoding="utf-8")

    def test_mixed_plain_and_linked_entries(self):
        self.board("frdmk22f", body="This unlinked content must not be inferred.")
        board = self.board("lpcxpresso55s16")
        self.write(["FRDM-K22F", self.link("LPCXpresso55S16", "lpcxpresso55s16")])
        with patch.object(merge.logger, "warning") as warning:
            result, text = self.run_merge()
        self.assertEqual(result, (True, 1))
        self.assertIn(":name: board-frdmk22f", text)
        self.assertIn("##### FRDM-K22F", text)
        self.assertIn(merge._NO_SETUP, text)
        self.assertNotIn("unlinked content", text)
        self.assertIn("Set JP1 to 1-2.", text)
        self.assertEqual(self.deleted, {board.resolve()})
        warning.assert_not_called()

    def test_all_plain_entries_resolve_real_directories(self):
        self.board_page("evkbmimxrt1170", "MIMXRT1170-EVKB")
        self.board_page("evkmimxrt595", "MIMXRT595-EVK")
        self.board_page("frdmk22f", "FRDM-K22F")
        self.write(["MIMXRT1170-EVKB", "EVK-MIMXRT595", "FRDM-K22F"])
        with patch.object(merge.logger, "warning") as warning:
            result, text = self.run_merge()
        self.assertEqual(result, (True, 0))
        for directory in ("evkbmimxrt1170", "evkmimxrt595", "frdmk22f"):
            self.assertIn(f":name: board-{directory}\n", text)
        self.assertEqual(text.count(merge._NO_SETUP), 3)
        self.assertFalse(self.deleted)
        warning.assert_not_called()

    def test_missing_link_retains_board_and_warns_with_path(self):
        self.write([self.link("MIMXRT2660-EVK", "mimxrt2660evk")])
        missing = (self.examples / "_boards" / "mimxrt2660evk" /
                   "usb_examples" / "cdc" / "example_board_readme.md").resolve()
        with patch.object(merge.logger, "warning") as warning:
            result, text = self.run_merge()
        self.assertEqual(result, (True, 0))
        self.assertIn(":name: board-mimxrt2660evk", text)
        self.assertIn("##### MIMXRT2660-EVK", text)
        self.assertIn(merge._MISSING_SETUP, text)
        self.assertNotIn(merge._NO_SETUP, text)
        self.assertFalse(self.deleted)
        warning.assert_called_once()
        self.assertIn(missing, warning.call_args.args)

    def test_multicore_sections_have_unique_anchors(self):
        first = self.board("imx943evk", "cm33_core1", "# Core 1\nFirst setup.")
        second = self.board("imx943evk", "cm7_core0", "# Core 0\nSecond setup.")
        self.write([self.link("IMX943EVK (CM33)", "imx943evk", "cm33_core1"),
                    self.link("IMX943EVK (CM7)", "imx943evk", "cm7_core0")])
        result, text = self.run_merge()
        self.assertEqual(result, (True, 0))
        self.assertIn(":name: board-imx943evk\n", text)
        self.assertIn(":name: board-imx943evk-2\n", text)
        self.assertIn("First setup.", text)
        self.assertIn("Second setup.", text)
        self.assertFalse(self.deleted)
        self.assertTrue(first.is_file() and second.is_file())

    def test_variants_sharing_readme_keep_labels_without_duplicate_targets(self):
        board = self.board("imx952lpd5evk")
        self.write([self.link("IMX952LPD5EVK-19", "imx952lpd5evk"),
                    self.link("IMX952LPD5EVK-15", "imx952lpd5evk")])
        result, text = self.run_merge()
        self.assertEqual(result, (True, 1))
        self.assertEqual(text.count(":name: board-imx952lpd5evk"), 1)
        self.assertEqual(text.count("Set JP1 to 1-2."), 1)
        self.assertIn("IMX952LPD5EVK-19 / IMX952LPD5EVK-15", text)
        self.assertEqual(self.deleted, {board.resolve()})

    def test_duplicate_link_is_merged_once_without_repeated_label(self):
        self.board("frdmk22f")
        entry = self.link("FRDM-K22F", "frdmk22f")
        self.write([entry, entry])
        result, text = self.run_merge()
        self.assertEqual(result, (True, 1))
        self.assertEqual(text.count("##### FRDM-K22F"), 1)
        self.assertNotIn("FRDM-K22F / FRDM-K22F", text)

    def test_link_with_trailing_annotation_still_merges_setup(self):
        self.board("frdmk22f")
        self.write([self.link("FRDM-K22F", "frdmk22f") + " (bare metal)"])
        result, text = self.run_merge()
        self.assertEqual(result, (True, 1))
        self.assertIn("Set JP1 to 1-2.", text)
        self.assertNotIn(merge._NO_SETUP, text)

    def test_sections_after_supported_boards_are_preserved(self):
        self.board("frdmk22f")
        tail = "\n## Troubleshooting\n- This is not a board.\n\n## See also\nMore help.\n"
        self.write(["FRDM-K22F"], tail)
        _, text = self.run_merge()
        self.assertIn(tail.strip(), text)
        self.assertEqual(text.count("{container} board-setup"), 1)

    def test_embedded_board_setup_follows_overview_before_common_instructions(self):
        self.board("frdmk22f")
        self.board("lpcxpresso55s16")
        self.readme.write_text(
            "# CDC\n\nIntroduction.\n\n## Overview\n\nEcho characters.\n\n"
            "## Build and Run\n\nCommon build instructions.\n\n"
            "## Supported Boards\n- FRDM-K22F\n- " +
            self.link("LPCXpresso55S16", "lpcxpresso55s16") + "\n",
            encoding="utf-8")
        _, text = self.run_merge()
        self.assertLess(text.index("Echo characters."), text.index("## Supported Boards"))
        self.assertLess(text.index("## Supported Boards"), text.index("## Build and Run"))
        self.assertLess(text.index("## Supported Boards"), text.index("Set JP1 to 1-2."))
        self.assertLess(text.index("Set JP1 to 1-2."), text.index("## Build and Run"))
        self.assertLess(text.index(merge._NO_SETUP), text.index("## Build and Run"))
        self.assertNotIn("board-picker", text)
        self.assertNotIn("## Board-Specific Setup", text)
        self.assertNotIn("](#board-", text)
        self.assertEqual(text.count("## Supported Boards"), 1)
        self.assertIn(merge._NO_SETUP, text)
        self.assertIn("Follow the common instructions below.", text)

    def test_nonstandard_heading_level_and_list_markers(self):
        self.board("frdmk22f")
        self.readme.write_text(
            "# CDC\nCommon instructions.\n### Supported Boards\n"
            "* FRDM-K22F\n\n### Running\nUse a terminal.\n", encoding="utf-8")
        _, text = self.run_merge()
        self.assertIn(":name: board-frdmk22f", text)
        self.assertIn("### Running\nUse a terminal.", text)

    def test_unknown_name_retained_with_explicit_resolution_warning(self):
        self.write(["Future Board"])
        with patch.object(merge.logger, "warning") as warning:
            _, text = self.run_merge()
        self.assertIn("##### Future Board", text)
        self.assertIn(merge._NO_SETUP, text)
        self.assertIn(":name: board-unresolved-futureboard", text)
        warning.assert_called_once()

    def test_ambiguous_alias_does_not_guess_directory(self):
        self.board_page("evkalpha", "Alpha-EVK")
        self.board_page("alphaevk", "Alpha-EVK")
        self.write(["Alpha-EVK"])
        with patch.object(merge.logger, "warning") as warning:
            _, text = self.run_merge()
        self.assertIn(":name: board-unresolved-alphaevk", text)
        warning.assert_called_once()

    def test_explicit_link_resolves_matching_plain_display_name(self):
        self.board("directory_not_derived_from_label")
        self.board_page("outdated_directory", "Marketing Board")
        self.write(["Marketing Board",
                    self.link("Marketing Board", "directory_not_derived_from_label")])
        with patch.object(merge.logger, "warning") as warning:
            _, text = self.run_merge()
        self.assertIn(":name: board-directory_not_derived_from_label\n", text)
        self.assertIn(":name: board-directory_not_derived_from_label-2\n", text)
        warning.assert_not_called()

    def test_cross_example_readme_is_not_deleted(self):
        shared = self.examples / "_boards" / "frdmk22f" / "other" / "example_board_readme.md"
        shared.parent.mkdir(parents=True)
        shared.write_text("# Shared setup\nUse common jumpers.", encoding="utf-8")
        self.write(["[FRDM-K22F](../../_boards/frdmk22f/other/example_board_readme.md)"])
        result, text = self.run_merge()
        self.assertEqual(result, (True, 0))
        self.assertIn("Use common jumpers.", text)
        self.assertFalse(self.deleted)

    def test_image_link_heading_and_nested_fence_rewriting(self):
        body = ("Setup\n=====\n\n![Jumpers](jumpers.png)\n"
                "[Common](../../../../usb_examples/cdc/readme.md#supported-boards)\n"
                "````text\nnested example\n````\n")
        board = self.board("frdmk22f", body=body)
        (board.parent / "jumpers.png").write_bytes(b"fixture image")
        self.write([self.link("FRDM-K22F", "frdmk22f")])
        _, text = self.run_merge()
        self.assertIn("##### Setup", text)
        self.assertIn("![Jumpers](_board_images/frdmk22f/jumpers.png)", text)
        self.assertIn("[Common](readme.md#supported-boards)", text)
        self.assertIn("`````{container} board-setup", text)
        self.assertIn("``````{container} board-selector", text)
        self.assertEqual((self.common / "_board_images" / "frdmk22f" /
                          "jumpers.png").read_bytes(), b"fixture image")

    def test_no_supported_section_or_no_entries_is_unchanged(self):
        for source in ("# CDC\nNo boards here.\n",
                       "# CDC\n## Supported Boards\nNot a board list.\n"):
            with self.subTest(source=source):
                self.readme.write_text(source, encoding="utf-8")
                result, text = self.run_merge()
                self.assertEqual(result, (False, 0))
                self.assertEqual(text, source)

    def test_builder_merges_before_deferred_deletion(self):
        from types import SimpleNamespace
        shared = self.board("frdmk22f")
        self.write([self.link("FRDM-K22F", "frdmk22f")])
        other = self.examples / "usb_examples" / "variant"
        other.mkdir()
        reused = other / "readme.md"
        reused.write_text(
            "# Variant\n## Supported Boards\n" +
            "- [FRDM-K22F](../../_boards/frdmk22f/usb_examples/cdc/"
            "example_board_readme.md)\n", encoding="utf-8")
        app = SimpleNamespace(srcdir=str(self.root), confdir=str(self.root / "docs"),
                              config=SimpleNamespace(merge_example_readmes=True))
        merge.merge_examples(app)
        self.assertIn("Set JP1 to 1-2.", reused.read_text(encoding="utf-8"))
        self.assertFalse(shared.exists())

    def test_shared_aliases_keep_search_matching_behavior(self):
        import mcux_search
        self.assertIs(mcux_search._norm, normalize)
        self.assertIs(mcux_search._aliases, aliases)
        self.assertEqual(normalize("FRDM-K22F"), "frdmk22f")
        self.assertEqual(aliases("mimxrt1170evkb"),
                         {"mimxrt1170evkb", "evkbmimxrt1170"})

    def test_focused_sphinx_build_renders_every_board(self):
        self.board_page("evkbmimxrt1170", "MIMXRT1170-EVKB")
        self.board("lpcxpresso55s16")
        self.board("imx943evk", "cm33_core1")
        self.board("imx943evk", "cm7_core0")
        self.board("imx952lpd5evk")
        self.write(["MIMXRT1170-EVKB",
                    self.link("LPCXpresso55S16", "lpcxpresso55s16"),
                    self.link("MIMXRT2660-EVK", "mimxrt2660evk"),
                    self.link("IMX943EVK (CM33)", "imx943evk", "cm33_core1"),
                    self.link("IMX943EVK (CM7)", "imx943evk", "cm7_core0"),
                    self.link("IMX952LPD5EVK-19", "imx952lpd5evk"),
                    self.link("IMX952LPD5EVK-15", "imx952lpd5evk")],
                   "\n## Running\nUse a terminal.\n")
        conf = self.root / "config"
        conf.mkdir()
        (conf / "conf.py").write_text(
            "extensions = ['myst_parser', 'merge_example_readmes']\n"
            "myst_enable_extensions = ['colon_fence']\n"
            "exclude_patterns = ['boards/**', 'examples/_boards/**', "
            "'config/**', 'output/**']\n"
            "master_doc = 'index'\n", encoding="utf-8")
        # Board metadata lives in the configuration tree, not necessarily srcdir.
        self.board_page("frdmk22f", "FRDM-K22F")
        (self.root / "index.rst").write_text(
            "Examples\n========\n\n.. toctree::\n\n"
            "   examples/usb_examples/cdc/readme\n", encoding="utf-8")
        warnings = io.StringIO()
        output = self.root / "output"
        app = Sphinx(str(self.root), str(conf), str(output / "html"),
                     str(output / "doctrees"), "html", status=io.StringIO(),
                     warning=warnings, freshenv=True)
        app.build(force_all=True)
        self.assertEqual(app.statuscode, 0)
        html = (output / "html" / "examples" / "usb_examples" / "cdc" /
                "readme.html").read_text(encoding="utf-8")
        for directory in ("evkbmimxrt1170", "lpcxpresso55s16", "mimxrt2660evk",
                          "imx943evk", "imx943evk-2", "imx952lpd5evk"):
            self.assertRegex(html, f'id="board-{directory}"')
        self.assertIn(merge._NO_SETUP, html)
        self.assertIn(merge._MISSING_SETUP, html)
        self.assertIn('id="running"', html)
        self.assertLess(html.index('id="supported-boards"'),
                        html.index('id="board-evkbmimxrt1170"'))
        self.assertLess(html.index('id="board-imx952lpd5evk"'),
                        html.index('id="running"'))
        self.assertNotIn('id="board-specific-setup"', html)
        self.assertNotIn('href="#board-evkbmimxrt1170"', html)
        self.assertNotIn("board-picker", html)
        self.assertIn("localStorage.getItem('mcux_board')", html)
        self.assertIn("Missing board-specific setup README", warnings.getvalue())
        self.assertIn("mimxrt2660evk", warnings.getvalue())
        self.assertNotIn("Duplicate explicit target", warnings.getvalue())
        self.assertEqual(warnings.getvalue().count("WARNING"), 1, warnings.getvalue())

    def test_selector_preselects_catalog_board_and_switches_entries(self):
        javascript = r"""
const assert = require('assert');
const names = ['MIMXRT1170-EVKB', 'LPCXpresso55S16', 'MIMXRT2660-EVK', 'Second core'];
const ids = ['board-evkbmimxrt1170', 'board-lpcxpresso55s16',
             'board-mimxrt2660evk', 'board-lpcxpresso55s16-2'];
let stored = 'evkbmimxrt1170';
global.localStorage = {getItem: () => stored, setItem: (_, value) => stored = value};
function element() {
  return {style: {}, children: [], appendChild(c) {this.children.push(c)},
          addEventListener(_, callback) {this.change = callback}};
}
const setups = ids.map((id, i) => {
  const heading = {textContent: names[i], style: {}};
  return {id, style: {}, querySelector: () => heading};
});
const group = {
  firstChild: setups[0],
  querySelectorAll: () => setups,
  insertBefore(label, before) {
    assert.equal(before, setups[0]);
    this.label = label;
  }
};
global.document = {readyState: 'complete', head: element(), createElement: element,
                   querySelectorAll: () => [group]};
"""
        checks = r"""
const select = group.label.children[0];
assert.equal(select.selectedIndex, 0);
assert.equal(setups[0].style.display, 'block');
assert.equal(setups[1].style.display, 'none');
assert.deepEqual(select.children.map(o => o.textContent), names);
select.value = ids[2];
select.change();
assert.equal(setups[2].style.display, 'block');
assert.equal(setups[0].style.display, 'none');
assert.equal(stored, 'mimxrt2660evk');
select.value = ids[3];
select.change();
assert.equal(setups[3].style.display, 'block');
assert.equal(setups[1].style.display, 'none');
assert.equal(stored, 'lpcxpresso55s16-2');
select.value = ids[1];
select.change();
assert.equal(setups[1].style.display, 'block');
assert.equal(setups[3].style.display, 'none');
assert.equal(stored, 'lpcxpresso55s16');
"""
        completed = subprocess.run(
            ["node", "-e", javascript + merge._SELECTOR_JS + checks],
            capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stderr)


if __name__ == "__main__":
    unittest.main()
