from libnix.raw.raw import Raw
from libnix.utility.print_table import PrintTable


_raw = Raw()
_pids = _raw.get_proc_pids()

_rows = []
for pid in _pids.get_pids:
    _process = _pids.get_process(pid)

    if _process.get_status.get_uid_real == "1000":
        _column = [pid,
                   _process.get_comm.get_command,
                   _process.get_stat.get_nice,
                   _process.get_statm.get_size,
                   _process.get_environ.get_environment_count,
                   _process.get_io.get_char_read,
                   _process.get_status.get_uid_real]

        _rows.append(_column)

_print_table = PrintTable("Pid", "Command", "Nice", "Size", "Env Count", "IO read", "User id")
_print_table.add_data(_rows)
_print_table.print()
