"""
Nix
Copyright (C) 2017  Mark Biciunas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import argparse
import logging

from libnix.config.script.tag.add import Add

LOG = logging.getLogger(__name__)


class CLIScriptTagAdd(object):
    """Object which defines the subparser for the script-tag-add command.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for updating scripts")

        subparser = subparsers.add_parser('script-tag-add',
                                          help='Add a tag to a script.')

        subparser.add_argument(type=str,
                               help="Name of script",
                               dest='script')

        subparser.add_argument(type=str,
                               help="Filter by tags",
                               nargs='+',
                               dest='tags')

        subparser.add_argument("--debug",
                               help="Include debug information in log file",
                               action='store_true',
                               dest='debug')

        subparser.set_defaults(func=self._process)

    @staticmethod
    def _process(args):
        """Process a command line action for adding a tag to a script.

        :param args: Command line arguments
        :type args: Namespace
        """
        LOG.info("Begin action to add a tag to a script")

        if args.debug:
            logging.getLogger().setLevel(level=logging.DEBUG)

        _add = Add()

        _add.add(args.script, args.tags)
