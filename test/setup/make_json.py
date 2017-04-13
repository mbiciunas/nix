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
import typing


class MakeJson:
    def __init__(self) -> None:
        self._scripts = []
        self._tags = []

    def add_script(self, name: str, desc: str, code: str, status: int, tags: typing.List[str]) -> None:
        _tags = "["
        for _tag in tags[:-1]:
            _tags += "\"" + _tag + "\","
        _tags += "\"" + tags[-1] + "\""
        _tags += "]"

        _script = ""
        _script += '    {'
        _script += '      "name": "{}",'.format(name)
        _script += '      "description": "{}",'.format(desc)
        _script += '      "code": "{}",'.format(code)
        _script += '      "status": {},'.format(status)
        _script += '      "tag": {}'.format(_tags)
        _script += '    }'

        self._scripts.append(_script)

    def add_tag(self, name: str, desc: str) -> None:
        _tag = ""
        _tag += '    {'
        _tag += '      "name": "' + name + '",'
        _tag += '      "description": "' + desc + '"'
        _tag += '    }'

        self._tags.append(_tag)

    def make(self) -> str:
        _json = ""
        _json += '{'
        _json += '  "script": ['

        if len(self._scripts) > 0:
            for _script in self._scripts[:-1]:
                _json += _script
                _json += ","

            _json += self._scripts[-1]

        _json += '  ],'
        _json += '  "tag": ['

        if len(self._tags) > 0:
            for _tag in self._tags[:-1]:
                _json += _tag
                _json += ","

            _json += self._tags[-1]

        _json += '  ]'
        _json += '}'

        return _json
