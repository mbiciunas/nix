#!/usr/bin/env python3
"""Object which defines the main entry to Nix configuration.
"""

import sys
import logging.handlers

from command_line_nix import cli
from libnix.exception.nix_error import NixError

LOG = logging.getLogger(__name__)


class Nix(object):
    """Object which defines the main entry to Nix configuration.
    """

    def __init__(self):
        """
        """
        # self.init_log()

        LOG.debug("Create instance of {}".format(self.__class__.__name__))

        _cli = cli.CLI()

        if len(sys.argv) == 1:
            _cli.print_help()
            sys.exit(1)

        try:
            _cli.start_parser()
        except NixError as _error:
            print("Error: {}".format(_error.get_message()), file=sys.stderr)
            if _error.get_exception() is not None:
                print("Original error: {}".format(_error.get_exception()), file=sys.stderr)
            sys.exit(1)

    # @staticmethod
    # def init_log():
    #     """Set up the program logging.
    #     """
    #     _util_path = util_path.UtilPath(constants.DIRECTORY)
    #     _base_directory = _util_path.get_base_directory()
    #
    #     _name = os.path.splitext(os.path.basename(sysfs.argv[0]))[0]
    #
    #     _log_file = os.path.join(_base_directory, _name + ".log")
    #
    #     if not os.path.exists(_base_directory):
    #         os.makedirs(_base_directory)
    #
    #     _rootLogger = logging.getLogger()
    #
    #     _logFormatter = logging.Formatter("%(asctime)s " +
    #                                       "%(levelname)-5.5s " +
    #                                       "%(name)s - %(message)s")
    #     _file_handler = logging.FileHandler(_log_file)
    #     _file_handler.setFormatter(_logFormatter)
    #     _rootLogger.addHandler(_file_handler)
    #
    #     _rootLogger.setLevel(level=logging.INFO)
    #
    #     _rootLogger.info("**********")
    #
    #     _rootLogger.info("{}".format(' '.join(map(str, sysfs.argv))))
    #     _rootLogger.info("")
    #
    #     _rootLogger.setLevel(level=logging.INFO)


def main():
    """Start the Nix config program.
    """
    Nix()


if __name__ == '__main__':
    main()
