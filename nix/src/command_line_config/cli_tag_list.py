"""Object which defines the subparser for the new command.
"""
import argparse
import logging

from libnix.config.tag.list_tag import ListTag

LOG = logging.getLogger(__name__)


class CLITagList(object):
    """Object which defines the subparser for the new command.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for listing tags")

        subparser = subparsers.add_parser('tag-list',
                                          help='List tags.')

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
        LOG.info("Begin action to list tags")

        if args.debug:
            logging.getLogger().setLevel(level=logging.DEBUG)

        _list_tag = ListTag()

        _list_tag.list()
