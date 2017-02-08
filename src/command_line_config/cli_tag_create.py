"""Object which defines the subparser for the new command.
"""
import argparse
import logging

from libnix.config.tag.create_tag import CreateTag

LOG = logging.getLogger(__name__)


class CLITagCreate(object):
    """Object which defines the subparser for the new command.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for creating tags")

        subparser = subparsers.add_parser('tag-create',
                                          help='Create a tag.')

        subparser.add_argument(type=str,
                               help="Name of new tag",
                               dest='tag')

        subparser.add_argument(type=str,
                               help="Description",
                               dest='desc')

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
        LOG.info("Begin action to create a tag")

        if args.debug:
            logging.getLogger().setLevel(level=logging.DEBUG)

        _create_tag = CreateTag()

        _create_tag.create(args.tag, args.desc)
