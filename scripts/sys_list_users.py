from libnix.sys.sys import Sys
from libnix.utility.print_table import PrintTable

_users = Sys.get_users(load=True)

_rows = []

for _user_name in _users.get_users():
    _user = _users.get_user_by_name(_user_name)

    _column = [_user.get_user(),
               _user.get_user_id(),
               _user.get_group_id(),
               _user.get_comment(),
               _user.get_directory(),
               _user.get_shell()]

    _rows.append(_column)

_print_table = PrintTable("User", "User Id", "Group Id", "Comment", "Directory", "Login Shell")
_print_table.add_data(_rows)
_print_table.print()
