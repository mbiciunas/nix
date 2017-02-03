from libnix.raw.raw import Raw
from libnix.utility.print_table import PrintTable


_raw = Raw()
sys_class_net_stat = _raw.get_sys_class_net_stat()

_rows = []

for _interface in sys_class_net_stat.get_interfaces():
    _column = [_interface,
               sys_class_net_stat.get_stat_tx_packets(_interface),
               sys_class_net_stat.get_stat_tx_aborted_errors(_interface),
               sys_class_net_stat.get_stat_tx_carrier_errors(_interface),
               sys_class_net_stat.get_stat_tx_dropped(_interface),
               sys_class_net_stat.get_stat_tx_errors(_interface),
               sys_class_net_stat.get_stat_tx_fifo_errors(_interface),
               sys_class_net_stat.get_stat_tx_heartbeat_errors(_interface),
               sys_class_net_stat.get_stat_tx_window_errors(_interface)]

    _rows.append(_column)

_print_table = PrintTable("Interface",
                          "Packets",
                          "Aborted Errors",
                          "Carrier Errors",
                          "Dropped",
                          "Errors",
                          "Fifo Errors",
                          "Heartbeat Errors",
                          "Window Errors")

_print_table.add_data(_rows)
_print_table.print()
