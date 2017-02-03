"""Object which defines the subparser for the new command.
"""
import argparse
import logging

from libnix.config.tag.rename_tag import RenameTag

LOG = logging.getLogger(__name__)


class CLITagRename(object):
    """Object which defines the subparser for the tag rename command.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for renaming tags")

        subparser = subparsers.add_parser('tag-rename',
                                          help='Rename a tag.')

        subparser.add_argument(type=str,
                               help="Current tag name",
                               dest='tag')

        subparser.add_argument(type=str,
                               help="New tag name",
                               dest='tag_new')

        subparser.add_argument("--debug",
                               help="Include debug information in log file",
                               action='store_true',
                               dest='debug')

        subparser.set_defaults(func=self._process)

    @staticmethod
    def _process(args):
        """Process a command line action for renaming tags.

        :param args: Command line arguments
        :type args: Namespace
        """
        LOG.info("Begin action to rename a tag")

        if args.debug:
            logging.getLogger().setLevel(level=logging.DEBUG)

        _rename_tag = RenameTag()

        _rename_tag.rename(args.tag, args.tag_new)
