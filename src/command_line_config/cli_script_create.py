"""Object which defines the subparser for the new command.
"""
import argparse
import logging

from libnix.config.script.create_script import CreateScript

LOG = logging.getLogger(__name__)


class CLIScriptCreate(object):
    """Object which defines the subparser for the new command.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for creating config file metadata")

        subparser = subparsers.add_parser('script-create',
                                          help='Create a new script.')

        subparser.add_argument(type=str,
                               help="Name of new script",
                               dest='name')

        subparser.add_argument(type=str,
                               help="Description",
                               dest='desc')

        subparser.add_argument(type=str,
                               help="Tags to apply to the new script",
                               nargs='+',
                               dest='tags')

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

        create_script = CreateScript(args.name, args.desc, args.tags)

        create_script.create()
