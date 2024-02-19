from typing import Unpack
from PyQt5.QtWidgets import QTableWidget, QHeaderView
from PyQt5.QtCore import Qt

from .widget_wrap import WidgetKwargs, widget as wrap_widget

TableColumnResizeMode = QHeaderView.ResizeMode


def table(
    columns: list[str], *,
    readonly: bool = True,
    resizeModes: list[TableColumnResizeMode | None] = None,
    fullsize: bool = False,
    **extra: Unpack[WidgetKwargs]
):
    table = QTableWidget()
    table.setColumnCount(len(columns))
    table.setHorizontalHeaderLabels(columns)
    if readonly: table.setEditTriggers(QTableWidget.NoEditTriggers)
    if resizeModes:
        header = table.horizontalHeader()
        for i, mode in enumerate(resizeModes):
            if mode is None: continue
            header.setSectionResizeMode(i, mode)
    if fullsize:
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
    if extra: wrap_widget(**extra, widget=table)
    return table
