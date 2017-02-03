from libnix.raw.raw import Raw
from libnix.utility.print_table import PrintTable


_raw = Raw()
sys_class_net_stat = _raw.get_sys_class_net_stat()

_rows = []

for _interface in sys_class_net_stat.get_interfaces():
    _column = [_interface,
               sys_class_net_stat.get_stat_rx_packets(_interface),
               sys_class_net_stat.get_stat_collisions(_interface),
               sys_class_net_stat.get_stat_rx_crc_errors(_interface),
               sys_class_net_stat.get_stat_rx_dropped(_interface),
               sys_class_net_stat.get_stat_rx_errors(_interface),
               sys_class_net_stat.get_stat_rx_fifo_errors(_interface),
               sys_class_net_stat.get_stat_rx_frame_errors(_interface),
               sys_class_net_stat.get_stat_rx_length_errors(_interface),
               sys_class_net_stat.get_stat_rx_missed_errors(_interface),
               sys_class_net_stat.get_stat_rx_nohandler(_interface),
               sys_class_net_stat.get_stat_rx_over_errors(_interface)]

    _rows.append(_column)

_print_table = PrintTable("Interface",
                          "Packets",
                          "Collisions",
                          "CRC",
                          "Dropped",
                          "Errors",
                          "Fifo Errors",
                          "Frame Errors",
                          "Length Errors",
                          "Missed Errors",
                          "No Handler",
                          "Over Errors")

_print_table.add_data(_rows)
_print_table.print()
