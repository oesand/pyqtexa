from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem


def tableRow(table: QTableWidget, cells: list[str]):
    index = table.rowCount()
    table.insertRow(index)
        
    for i, el in enumerate(cells):
        if isinstance(el, str):
            table.setItem(index, i, QTableWidgetItem(el))
        elif isinstance(el, QWidget):
            table.setCellWidget(index, i, el)
