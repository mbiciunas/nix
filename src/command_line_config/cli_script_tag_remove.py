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

from libnix.config.script.tag.delete import Delete

LOG = logging.getLogger(__name__)


class CLIScriptTagRemove(object):
    """
    Command line subparser for removing a tag from a given script.

    The following arguments can be interpreted by the subprocessor:

    :Name: Name of the script to remove tags from.
    :Tags: One or more tags to remove from the script.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for updating scripts")

        subparser = subparsers.add_parser('script-tag-delete',
                                          help='Remove a tag from a script.')

        subparser.add_argument(type=str,
                               help="Name of script",
                               dest='script')

        subparser.add_argument(type=str,
                               help="Tag to remove",
                               nargs='+',
                               dest='tags')

        subparser.add_argument("--debug",
                               help="Include debug information in log file",
                               action='store_true',
                               dest='debug')

        subparser.set_defaults(func=self._process)

    @staticmethod
    def _process(args):
        """Process a command line action for removing a tag from a script.

        :param args: Command line arguments
        :type args: Namespace
        """
        LOG.info("Begin action to remove a tag from a script")

        if args.debug:
            logging.getLogger().setLevel(level=logging.DEBUG)

        _delete = Delete()

        _delete.delete(args.script, args.tags)
