#!/usr/bin/env python3
#
#  Nix
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

import logging.handlers
import sys

from cli_config import cli
from utility.nix_error import NixError

LOG = logging.getLogger(__name__)


class NixConfig(object):
    """Object which defines the main entry to Nix configuration.


    .. argparse::
        :module: cli.cli
        :func: make_parser
        :prog: NixConfig
    """

    def __init__(self) -> None:
        """
        """
        # self.init_log()

        LOG.debug("Create instance of {}".format(self.__class__.__name__))

        try:
            self._parser = cli.make_parser(sys.argv)
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
    NixConfig()


if __name__ == '__main__':
    main()
