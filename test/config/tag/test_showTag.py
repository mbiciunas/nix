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

from config.tag.show_tag import ShowTag
from utility.nix_error import NixError


class TestShowTag:
    def test_show(self, config_valid, capsys):
        _show_tag = ShowTag()

        _show_tag.show(config_valid.TAG_VALID_1)

        out, err = capsys.readouterr()

        assert config_valid.SCRIPT_VALID_1 in out

    def test_show_invalid_name(self, config_valid):
        _show_tag = ShowTag()

        with pytest.raises(NixError):
            _show_tag.show(config_valid.TAG_INVALID_1)
