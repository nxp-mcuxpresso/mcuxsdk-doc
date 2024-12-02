"""
VCS Link
########

Copyright (c) 2021 Nordic Semiconductor ASA
SPDX-License-Identifier: Apache-2.0

Introduction
============

This Sphinx extension can be used to obtain the VCS URL for a given Sphinx page.
This is useful, for example, when adding features like "Open on GitHub" on top
of pages. The extension installs a Jinja filter which can be used on the
template to obtain VCS page URLs.

Configuration options
=====================

- ``vcs_link_base_url``: Base URL used as a prefix for generated URLs.
- ``vcs_link_prefixes``: Mapping of pages (regex) <> VCS prefix.
- ``vcs_link_exclude``: List of pages (regex) that will not report a URL. Useful
  for, e.g., auto-generated pages not in VCS.
"""

from functools import partial
import os
import re
from typing import Optional

from sphinx.application import Sphinx
from sphinx.util import logging
from urllib.parse import quote
from textwrap import dedent

logger = logging.getLogger(__name__)

__version__ = "0.1.0"


def vcs_link_get_url(app: Sphinx, pagename: str) -> Optional[str]:
    """Obtain VCS URL for the given page.

    Args:
        app: Sphinx instance.
        pagename: Page name (path).

    Returns:
        VCS URL if applicable, None otherwise.
    """

    if not os.path.isfile(app.env.doc2path(pagename)):
        return None

    for exclude in app.config.vcs_link_exclude:
        if re.match(exclude, pagename):
            return None

    found_prefix = ""
    pagepath = app.env.project.doc2path(pagename, basedir=False).replace("\\","/")
    for pattern, prefix in app.config.vcs_link_prefixes.items():
        if re.match(pattern, pagepath):
            found_prefix = prefix
            break

    if found_prefix is None:
        return None

    if "boards" in found_prefix:
        return "/".join(
            [
                found_prefix,
                pagepath.replace("boards/","").replace("Boards/",""),
            ]
        )
    elif "examples/" in found_prefix:
        return "/".join(
            [
                found_prefix,
                re.sub(r'^examples/', '', pagepath)
            ]
        )
    elif "mcuboot" in found_prefix:
        return "/".join(
            [
                found_prefix,
                pagepath.replace("middleware/mcuboot_opensource/",""),
            ]
        )
    else:
        return "/".join(
            [
                found_prefix,
                pagepath,
            ]
        )

def vcs_link_get_open_issue_url(app: Sphinx, pagename: str) -> Optional[str]:
    """Link to open a new Github issue regarding "pagename" with title, body, and
    labels already pre-filled with useful information.

    Args:
        app: Sphinx instance.
        pagename: Page name (path).

    Returns:
        URL to open a new issue if applicable, None otherwise.
    """

    found_prefix = ""
    pagepath = app.env.project.doc2path(pagename, basedir=False).replace("\\","/")
    for pattern, prefix in app.config.vcs_link_prefixes.items():
        if re.match(pattern, pagepath):
            found_prefix = prefix
            break

    title = quote(f"doc: Documentation issue in '{pagename}'")
    labels = quote("area: Documentation")
    body = quote(
        dedent(
            f"""\
    **Describe the bug**

    << Please describe the issue here >>
    << You may also want to update the automatically generated issue title above. >>

    **Environment**

    * Page: `{pagename}`
    """
        )
    )


    return f"{found_prefix}/issues/new?title={title}&labels={labels}&body={body}"

def add_jinja_filter(app: Sphinx):
    if app.builder.name != "html":
        return

    app.builder.templates.environment.filters["vcs_link_get_url"] = partial(
        vcs_link_get_url, app
    )

    app.builder.templates.environment.filters["vcs_link_get_open_issue_url"] = partial(
        vcs_link_get_open_issue_url, app
    )

def setup(app: Sphinx):
    app.add_config_value("vcs_link_prefixes", {}, "")
    app.add_config_value("vcs_link_exclude", [], "")

    app.connect("builder-inited", add_jinja_filter)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
