from libnix.sys.sys import Sys
# from libnix.utility.print_table import PrintTable

print("Getting users")

_users = Sys.get_users(load=True)

print("Building list of user id's")

_user_ids = list()

for _user_name in _users.get_users():
    _user_ids.append(_users.get_user_by_name(_user_name).get_user_id())

print("Loading filesystem")

_filesystem = Sys.get_filesystem()

_files = _filesystem.load()

print("Checking files")

for _file in _files.get_files():
    if _file.get_user_id() not in _user_ids:
        _permission = ""
        _permission += 'd' if _file.get_type() is _file.TYPE_DIR else '-'
        _permission += 'r' if _file.get_user_read() else '-'
        _permission += 'w' if _file.get_user_write() else '-'
        _permission += 'x' if _file.get_user_execute() else '-'
        _permission += 'r' if _file.get_group_read() else '-'
        _permission += 'w' if _file.get_group_write() else '-'
        _permission += 'x' if _file.get_group_execute() else '-'
        _permission += 'r' if _file.get_other_read() else '-'
        _permission += 'w' if _file.get_other_write() else '-'
        _permission += 'x' if _file.get_other_execute() else '-'

        print("{} - {}".format(_permission, _file.get_path()))
