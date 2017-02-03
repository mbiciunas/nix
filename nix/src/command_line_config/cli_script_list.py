"""Object which defines the subparser for the new command.
"""
import argparse
import logging

from libnix.config.script.list_script import ListScript

LOG = logging.getLogger(__name__)


class CLIScriptList(object):
    """Object which defines the subparser for the new command.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for listing scripts")

        subparser = subparsers.add_parser('script-list',
                                          help='List scripts.')

        subparser.add_argument(type=str,
                               help="Filter by tags",
                               nargs='*',
                               dest='tags')

        subparser.add_argument("--debug",
                               help="Include debug information in log file",
                               action='store_true',
                               dest='debug')

        subparser.set_defaults(func=self._process)

    @staticmethod
    def _process(args):
        """Process a command line action for listing scripts.

        :param args: Command line arguments
        :type args: Namespace
        """
        LOG.info("Begin action to list scripts")

        if args.debug:
            logging.getLogger().setLevel(level=logging.DEBUG)

        _list_script = ListScript()

        _list_script.list(args.tags)
