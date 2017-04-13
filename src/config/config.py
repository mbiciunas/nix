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

import json

from config.config_scripts import ConfigScripts
from config.config_tags import ConfigTags
from utility.dir import Dir


class Config:
    CONFIG_TAG = "tag"
    CONFIG_SCRIPT = "script"

    def __init__(self) -> None:
        self._data = {self.CONFIG_TAG: ConfigTags(),
                      self.CONFIG_SCRIPT: ConfigScripts()}

        with open(Dir.get_script_tag(), 'r') as infile:
            _import = json.load(infile)

        self._data[self.CONFIG_TAG].import_data(_import[self.CONFIG_TAG])
        self._data[self.CONFIG_SCRIPT].import_data(_import[self.CONFIG_SCRIPT])

    def get_tags(self) -> ConfigTags:
        return self._data[self.CONFIG_TAG]

    def get_scripts(self) -> ConfigScripts:
        return self._data[self.CONFIG_SCRIPT]

    def write(self) -> None:
        _export = {self.CONFIG_TAG: self.get_tags().export_data(),
                   self.CONFIG_SCRIPT: self.get_scripts().export_data()}

        with open(Dir.get_script_tag(), 'w') as outfile:
            json.dump(_export, outfile, sort_keys=False, indent=2)

    # def _read(self) -> None:
    #     with open(Dir.get_script_tag(), 'r') as infile:
    #         _import = json.load(infile)
    #
    #     self._data[self.CONFIG_TAG].import_data(_import[self.CONFIG_TAG])
    #     self._data[self.CONFIG_SCRIPT].import_data(_import[self.CONFIG_SCRIPT])
