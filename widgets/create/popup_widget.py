from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtCore import Qt, QPoint, QTimer
from .label_widget import label


def errorPopup(parent: QWidget, text: str, *, ms_delay: int = 2000):
    assert parent and text and ms_delay > 100
    widget: QLabel = label(
        text, 
        parent=parent, 
        stylesheet="border: 2px solid #e31a17; border-radius: 5px;" \
        "padding: 2px; background-color: white; font-size: 14px;"
    )
    widget.setWindowFlags(Qt.ToolTip)
    widget.move(parent.mapToGlobal(QPoint()))
    widget.show()
    QTimer.singleShot(ms_delay, widget.hide)
