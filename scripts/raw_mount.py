from libnix.raw.raw import Raw
from libnix.utility.print_table import PrintTable


_raw = Raw()
_mounts = _raw.get_proc_mounts()

_rows = []


_mounts.load()

for _mount_point in _mounts.get_mounts():
    _mount = _mounts.get_mount(_mount_point)

    _column = [_mount.get_device(),
               _mount.get_mount_point(),
               _mount.get_filesystem_type(),
               _mount.get_options()]

    _rows.append(_column)

_print_table = PrintTable("Device", "Mount Point", "File System", "Mount Options")
_print_table.add_data(_rows)
_print_table.print()
