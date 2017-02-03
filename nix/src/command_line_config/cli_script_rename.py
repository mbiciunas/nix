"""Object which defines the subparser for the script rename command.
"""
import argparse
import logging

from libnix.config.script.rename_script import RenameScript

LOG = logging.getLogger(__name__)


class CLIScriptRename(object):
    """Object which defines the subparser for the script command.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for renaming a script file")

        subparser = subparsers.add_parser('script-rename',
                                          help='Rename a script.')

        subparser.add_argument(type=str,
                               help="Current name",
                               dest='name')

        subparser.add_argument(type=str,
                               help="New name",
                               dest='name_new')

        subparser.add_argument("--debug",
                               help="Include debug information in log file",
                               action='store_true',
                               dest='debug')

        subparser.set_defaults(func=self._process)

    @staticmethod
    def _process(args):
        """Process a command line action for listing setup groups.

        :param args: Command line arguments
        :type args: Namespace
        """
        LOG.info("Begin action to create a new script")

        if args.debug:
            logging.getLogger().setLevel(level=logging.DEBUG)

        rename_script = RenameScript()

        rename_script.rename(args.name, args.name_new)
