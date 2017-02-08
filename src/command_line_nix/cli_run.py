"""Object which defines the subparser for the new command.
"""
import argparse
import logging

from libnix.config.script.run_script import RunScript

LOG = logging.getLogger(__name__)


class CLIRun(object):
    """Object which defines the subparser for the new command.
    """

    def __init__(self, subparsers: argparse._SubParsersAction):
        """

        :param subparsers: Object that will contain the argument definitions.
        :type subparsers: ArgumentParser
        """
        LOG.debug("Create instance of {}".format(self.__class__.__name__))
        LOG.debug("Define a cli parser for running scripts")

        subparser = subparsers.add_parser('run',
                                          help='Create a new script.')

        subparser.add_argument(type=str,
                               help="Name of script",
                               dest='script')

        subparser.add_argument(type=str,
                               help="parameters",
                               nargs='*',
                               dest='param')

        # subparser.add_argument(type=str,
        #                        help="Tags to apply to the new script",
        #                        nargs='+',
        #                        dest='tags')

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

        _run_script = RunScript()

        _run_script.run(args.script)
