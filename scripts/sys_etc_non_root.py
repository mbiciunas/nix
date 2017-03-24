from libnix.sys.sys import Sys
# from libnix.utility.print_table import PrintTable

print("Getting groups")

_groups = Sys.get_groups(True)
_users = Sys.get_users(True)
_filesystem = Sys.get_filesystem()
_filesystem.path_include("/etc")

print("Loading filesystem")

_files = _filesystem.load()

print("Found {} files".format(_files.get_file_count()))

for _file in _files.get_files():
    if _file.get_group_id() != 0 or _file.get_user_id() != 0:
        _user = _users.get_user_by_id(_file.get_user_id())
        _group = _groups.get_group_by_id(_file.get_group_id())

        print("{} {} - {}".format(_user.get_user(), _group.get_group(), _file.get_path()))
