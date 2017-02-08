from libnix.raw.raw import Raw
from libnix.utility.print_table import PrintTable


_raw = Raw()
_modules = _raw.get_proc_modules()

_rows = []


_modules.load()

for _name in _modules.get_modules():
    _module = _modules.get_module(_name)

    _column = [_module.get_name(),
               _module.get_size(),
               _module.get_instances(),
               _module.get_dependencies(),
               _module.get_state(),
               _module.get_memory_offset()]

    _rows.append(_column)

_print_table = PrintTable("Name", "Size", "Instances", "Dependencies", "State", "Memory Offset")
_print_table.add_data(_rows)
_print_table.print()
