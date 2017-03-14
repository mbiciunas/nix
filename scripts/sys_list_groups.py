from libnix.sys.sys import Sys
from libnix.utility.print_table import PrintTable

_sys = Sys()
_groups = _sys.get_user_groups()

_rows = []


_groups.load()

for _group_name in _groups.get_groups():
    _user = _groups.get_group(_group_name)

    _column = [_user.get_group(),
               _user.get_group_id(),
               _user.get_users()]

    _rows.append(_column)

_print_table = PrintTable("Group", "Group Id", "Users")
_print_table.add_data(_rows)
_print_table.print()
