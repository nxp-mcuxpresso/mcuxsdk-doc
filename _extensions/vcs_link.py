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


def vcs_link_get_url(app: Sphinx, pagename: str, mode: str = "blob") -> Optional[str]:
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
    found_repstr = ""
    pagepath = app.env.project.doc2path(pagename, basedir=False).replace("\\","/")
    for index in range(len(app.config.vcs_link_prefixes)): 
        pattern = app.config.vcs_link_prefixes[index]["pattern"]
        repstr = app.config.vcs_link_prefixes[index]["replace_prefix"]
        prefix = app.config.vcs_link_prefixes[index]["link"]
        if re.match(pattern, pagepath):
            found_prefix = prefix
            found_repstr = repstr
            break

    if found_prefix is None:
        return None

    if app.config.is_internal_doc:
        mode = "browse"
        return "/".join(
            [
                found_prefix,
                mode,
                pagepath.lstrip(found_repstr)
            ]) + f'?at=refs/heads/{app.config.vcs_link_version}'
    else:
        return "/".join(
            [
                found_prefix,
                mode,
                app.config.vcs_link_version,
                pagepath.lstrip(found_repstr)
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
    found_repstr = ""
    pagepath = app.env.project.doc2path(pagename, basedir=False).replace("\\","/")
    for index in range(len(app.config.vcs_link_prefixes)): 
        pattern = app.config.vcs_link_prefixes[index]["pattern"]
        repstr = app.config.vcs_link_prefixes[index]["replace_prefix"]
        prefix = app.config.vcs_link_prefixes[index]["link"]
        if re.match(pattern, pagepath):
            found_prefix = prefix
            found_repstr = repstr
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

    if app.config.is_internal_doc:
        issue_server = app.config.vcs_link_prefixes[0]["link"].split("/projects")[0].replace("bitbucket", "jira")
        return f"{issue_server}/secure/CreateIssueDetails!init.jspa?pid=10001&issuetype=10&priority=3&summary={title}&description={body}"
    else:
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
    app.add_config_value("vcs_link_prefixes", [], "")
    app.add_config_value("vcs_link_exclude", [], "")
    app.add_config_value("vcs_link_version", "", "")
    app.add_config_value("is_internal_doc", "", "")

    app.connect("builder-inited", add_jinja_filter)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
