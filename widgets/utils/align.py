from PyQt5.QtWidgets import QLayout
from PyQt5.QtCore import Qt


def applyAlignment(layout: QLayout, alignment: str):
    if not alignment: return layout
    alignment = alignment.lower()
    if alignment == "top": layout.setAlignment(Qt.AlignTop)
    elif alignment == "right": layout.setAlignment(Qt.AlignRight)
    elif alignment == "left": layout.setAlignment(Qt.AlignLeft)
    elif alignment == "bottom": layout.setAlignment(Qt.AlignBottom)
    elif alignment == "center": layout.setAlignment(Qt.AlignCenter)
    return layout
