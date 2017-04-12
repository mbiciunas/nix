# Nix
# Copyright (c) 2017  Mark Biciunas.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import argparse
import logging

from config.tag.list_tag import ListTag

LOG = logging.getLogger(__name__)


def add_subparser(subparsers: argparse._SubParsersAction):
    """
    Add a command line subparser for displaying a list of available tags.

    :param subparsers: Object that will contain the argument definitions.
    :type subparsers: ArgumentParser
    """
    LOG.debug("Define a cli parser for running scripts")

    _subparser = subparsers.add_parser('tags',
                                       help='List all tags.')

    _subparser.set_defaults(func=_process)


def _process(args):
    """Process a command line action for displaying a list of available tags.

    :param args: Command line arguments
    :type args: Namespace
    """
    LOG.info("Begin action to list the tags")

    _list_tag = ListTag()

    _list_tag.list()
