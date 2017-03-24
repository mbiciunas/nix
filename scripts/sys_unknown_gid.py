from libnix.sys.sys import Sys
# from libnix.utility.print_table import PrintTable

print("Getting groups")

_groups = Sys.get_groups(load=True)

print("Building list of group id's")

_group_ids = set()

for _group_name in _groups.get_groups():
    _group_ids.add(_groups.get_group_by_name(_group_name).get_group_id())

print("Loading filesystem")

_filesystem = Sys.get_filesystem()

_files = _filesystem.load()

print("Checking files")

for _file in _files.get_files():
    if _file.get_group_id() not in _group_ids:
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
