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

import pytest

from config.script.rename_script import RenameScript
from exception.nix_error import NixError


class TestRenameScript:
    def test_rename(self, config_valid):
        _rename_script = RenameScript()

        _rename_script.rename(config_valid.SCRIPT_VALID_1, config_valid.SCRIPT_INVALID_1)

    def test_rename_same_name(self, config_valid):
        _rename_script = RenameScript()

        with pytest.raises(NixError):
            _rename_script.rename(config_valid.SCRIPT_VALID_1, config_valid.SCRIPT_VALID_1)

    def test_rename_invalid_name(self, config_valid):
        _rename_script = RenameScript()

        with pytest.raises(NixError):
            _rename_script.rename(config_valid.SCRIPT_INVALID_1, config_valid.SCRIPT_INVALID_2)

    def test_rename_existing_name(self, config_valid):
        _rename_script = RenameScript()

        with pytest.raises(NixError):
            _rename_script.rename(config_valid.SCRIPT_VALID_1, config_valid.SCRIPT_VALID_2)
