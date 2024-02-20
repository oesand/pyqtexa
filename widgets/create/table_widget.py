from typing import Unpack, NotRequired
from PyQt5.QtWidgets import QTableWidget, QHeaderView
from PyQt5.QtCore import Qt

from .widget_wrap import WidgetKwargs, widget as wrap_widget

TableColumnResizeMode = QHeaderView.ResizeMode


class TableKwargs(WidgetKwargs):
    resizeModes: NotRequired[list[TableColumnResizeMode | None]]
    readonly: NotRequired[bool]
    fullsize: NotRequired[bool]


def table(
    columns: list[str],
    **kwargs: Unpack[TableKwargs]
):
    table = QTableWidget()
    table.setColumnCount(len(columns))
    table.setHorizontalHeaderLabels(columns)
    
    fullsize = kwargs.pop('fullsize', None)
    readonly = kwargs.pop('readonly', None)
    resizeModes = kwargs.pop('resizeModes', None)
    
    if readonly: table.setEditTriggers(QTableWidget.NoEditTriggers)
    if resizeModes:
        header = table.horizontalHeader()
        for i, mode in enumerate(resizeModes):
            if mode is None: continue
            header.setSectionResizeMode(i, mode)
            
    if fullsize:
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
    if kwargs: wrap_widget(**kwargs, widget=table)
    return table
