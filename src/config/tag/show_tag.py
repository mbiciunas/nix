# Nix
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

from config.config import Config
from utility.nix_error import NixError
from utility.print_table import PrintTable


class ShowTag:
    def __init__(self) -> None:
        self._config = Config()
        self._tags = self._config.get_tags()

    def show(self, tag: str) -> None:
        if not self._tags.exist(tag):
            raise NixError("Unknown tag: {}".format(tag))

        _rows = []

        for _script in self._config.get_scripts().find_by_tag(tag):
            _rows.append([_script.get_name(),
                          _script.get_desc(),
                          ' '.join(_script.get_tags()),
                          _script.get_status()])

        _print_table = PrintTable("Script", "desc", "tags", "status")
        _print_table.add_data(_rows)
        _print_table.print()
