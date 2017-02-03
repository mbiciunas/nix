"""Object which defines the subparser for the new command.
"""
import argparse
import logging

from libnix.config.script.show_script import ShowScript

LOG = logging.getLogger(__name__)


class CLIScriptShow(object):
    """Object which defines the subparser for the new command.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for showing a script")

        subparser = subparsers.add_parser('script-show',
                                          help='Show the contents of a script.')

        subparser.add_argument(type=str,
                               help="Name of script",
                               dest='name')

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
        LOG.info("Begin action to show a script")

        if args.debug:
            logging.getLogger().setLevel(level=logging.DEBUG)

        _show_script = ShowScript()

        _show_script.show(args.name)
