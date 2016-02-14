#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by 冯雪娜
# Copyright (c) 2016 冯雪娜
#
# License: MIT
#

"""This module exports the StylelintG plugin class."""

from SublimeLinter.lint import NodeLinter, util


class StylelintG(NodeLinter):
    """Provides an interface to stylelint-g."""

    syntax = ('css', 'css3', 'sass', 'scss', 'postcss')
    cmd = ('node', os.path.dirname(os.path.realpath(__file__)) + '/stylelint_wrapper.js', '@')
    error_stream = util.STREAM_BOTH
    config_file = ('--config', '.stylelintrc', '~')
    tempfile_suffix = 'css'
    regex = (
        r'^(?P<line>[0-9]+)\:(?P<col>[0-9]+)(?P<message>.+)'
    )

