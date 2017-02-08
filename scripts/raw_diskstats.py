from libnix.raw.raw import Raw
from libnix.utility.print_table import PrintTable


_raw = Raw()
_diskstats = _raw.get_proc_diskstats()

_rows = []

_diskstats.load()

for _disk in _diskstats.get_disks():
    _diskstat = _diskstats.get_disk(_disk)

    _column = [_diskstat.get_device_major(),
               _diskstat.get_device_minor(),
               _diskstat.get_device_name(),
               _diskstat.get_read_completed(),
               _diskstat.get_read_merged(),
               _diskstat.get_read_sectors(),
               _diskstat.get_read_time(),
               _diskstat.get_write_completed(),
               _diskstat.get_write_merged(),
               _diskstat.get_write_sectors(),
               _diskstat.get_write_time(),
               _diskstat.get_io_in_progress(),
               _diskstat.get_io_time(),
               _diskstat.get_io_time_weighted()]

    _rows.append(_column)

_print_table = PrintTable("Major",
                          "Minor",
                          "Name",
                          "Read Completed",
                          "Read Merged",
                          "Read Sectors",
                          "Read Time",
                          "Write Completed",
                          "Write Merged",
                          "Write Sectors",
                          "Write Time",
                          "IO In Progress",
                          "IO Time",
                          "IO Time Weighted")

_print_table.add_data(_rows)
_print_table.print()
