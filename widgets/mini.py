from typing import Callable, Dict, List, Optional, Tuple, Union
from PyQt5.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QLineEdit,
    QLayout, QWidget, QScrollArea,
    QTableWidget, QHeaderView
)
from PyQt5.QtCore import QSize, Qt, QPoint, QTimer
from PyQt5.QtGui import (
    QValidator, QDoubleValidator, QIntValidator,
    QIcon, QMovie, QImage, QPixmap
)


def applyAlignment(layout: QLayout, alignment: str):
    alignment = alignment.lower()
    if alignment == "top": layout.setAlignment(Qt.AlignTop)
    elif alignment == "right": layout.setAlignment(Qt.AlignRight)
    elif alignment == "left": layout.setAlignment(Qt.AlignLeft)
    elif alignment == "bottom": layout.setAlignment(Qt.AlignBottom)
    elif alignment == "center": layout.setAlignment(Qt.AlignCenter)
    return layout

def createVerticalLine():
    line = QFrame()
    line.setGeometry(0, 0, 50, 3)
    line.setFrameShape(QFrame.Shape.HLine)
    line.setFrameShadow(QFrame.Shadow.Sunken)
    return line


def createButton(*, 
    text: Optional[str] = None,
    id: Optional[str] = None,
    parent: Optional[QWidget] = None,
    size: Optional[Union[int, Tuple[int, int]]] = None,
    icon: Optional[Union[str, Tuple[str, int]]] = None,
    disabled: bool = False,
    handle: Optional[Callable] = None
):
    button = QPushButton(text, parent)
    if id: button.setObjectName(id)
    if icon:
        if isinstance(icon, tuple):
            icon_size = icon[1]
            icon = icon[0]
            button.setIconSize(QSize(icon_size, icon_size))
        if isinstance(icon, str):
            button.setIcon(QIcon(icon))
    if size is not None:
        if isinstance(size, int):
            button.setFixedSize(size, size)
        elif isinstance(size, tuple):
            button.setFixedSize(size[0], size[1])
    if handle is not None:
        button.pressed.connect(lambda: handle(), Qt.DirectConnection)
    if disabled: button.setDisabled(True)
    return button


def createLineLayout(
    items: Optional[List[Union[QLayout, QWidget]]], *,
    vertical: bool = True,
    id: Optional[str] = None,
    alignment: Optional[str] = None,
    stretch: Optional[Dict[int, int]] = None,
    content_margins: Optional[Tuple[int, int, int, int]] = None,
    spacing: Optional[int] = None,
):
    layout = QVBoxLayout() if vertical else QHBoxLayout()
    if id: layout.setObjectName(id)
    if items:
        for item in items:
            if isinstance(item, QLayout):
                layout.addLayout(item)
            elif isinstance(item, QWidget):
                layout.addWidget(item)
    
    if content_margins: layout.setContentsMargins(*content_margins)
    if not alignment: alignment = "top" if vertical else "left"
    applyAlignment(layout, alignment)
    
    if stretch: 
        for i, v in stretch.items(): layout.setStretch(i, v)
    
    if spacing: layout.setSpacing(spacing)
    
    def clean():
        if layout.count() == 0: return None
        while layout.count() > 0:
            el = layout.takeAt(0)
            if el is None: continue
            wid = el.widget()
            if wid is None: continue
            wid.setParent(None)
            wid.deleteLater()
            del wid
    layout.clean = clean
    return layout

def createLabel(
    text: str, *, 
    parent: Optional[QWidget] = None,
    stylesheet: Optional[str] = None,
    alignment: Optional[str] = None,
):
    label = QLabel(parent)
    label.setText(text)
    if stylesheet: label.setStyleSheet(stylesheet)
    if alignment: applyAlignment(label, alignment)
    return label

def createInput(*,
    initial_text: Optional[str] = None,
    placeholder: Optional[str] = None,
    input_mask: Optional[str] = None,
    validator: Optional[QValidator] = None,
    textChanged: Optional[Callable] = None,
    readonly: bool = False
):
    input = QLineEdit()
    if initial_text: input.setText(initial_text)
    if placeholder: input.setPlaceholderText(placeholder)
    if input_mask: input.setInputMask(input_mask)
    if validator: input.setValidator(validator)
    if textChanged: input.textChanged.connect(textChanged)
    if readonly: input.setReadOnly(True)
    return input

def rangeValidator(double: bool = False, start: int = 0, end: int = None):
    val = QDoubleValidator() if double else QIntValidator()
    if start is not None: val.setBottom(start)
    if end is not None: val.setTop(end)
    return val

def createWidget(*,
    id: Optional[str] = None,
    parent: Optional[QWidget] = None,
    layout: Optional[QLayout] = None,
    stylesheet: Optional[str] = None,
    unvisible: bool = False
):
    widget = QWidget(parent)
    if id: widget.setObjectName(id)
    if layout: widget.setLayout(layout)
    if stylesheet: widget.setStyleSheet(stylesheet)
    if unvisible: widget.setVisible(False)
    return widget

def createScrollarea(*,
    id: Optional[str] = None,
    parent: Optional[QWidget] = None,
    layout: Optional[QLayout] = None,
    vertical: bool = True,
):
    widget = QScrollArea(parent) 
    if id: widget.setObjectName(id)
    if layout: widget.setLayout(layout)
    if vertical:
        widget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    else:
        widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    return widget

def pasteGif(
    path: str, *, 
    parent: Optional[QWidget] = None,
    size: Optional[Union[int, Tuple[int, int]]] = None,
):
    container = QLabel(parent)
    container.setScaledContents(True)
    
    if size is not None:
        if isinstance(size, int):
            container.setFixedSize(size, size)
        elif isinstance(size, tuple):
            container.setFixedSize(size[0], size[1])
    
    mov = QMovie(path)
    container.setMovie(mov)
    mov.start()
    
    container.setAlignment(Qt.AlignCenter)
    return container

def pasteImage(
    data: bytes, *, 
    parent: Optional[QWidget] = None,
    size: Optional[Union[int, Tuple[int, int]]] = None,
    rounded: bool = False,
):
    container = QLabel(parent)
    container.setScaledContents(True)
    
    if size is not None:
        if isinstance(size, int):
            container.setFixedSize(size, size)
        elif isinstance(size, tuple):
            container.setFixedSize(size[0], size[1])
    
    img = QImage()
    img.loadFromData(data)
    px = QPixmap.fromImage(img)
    container.setPixmap(px)
    del img
    
    container.setAlignment(Qt.AlignCenter)
    if rounded:
        container.setStyleSheet("border-radius: 15%")
    return container

def createTableWidget(
    columns: List[str], *,
    readonly: bool = True,
    resizeModes: List[Optional[QHeaderView.ResizeMode]] = None,
    fullsize: bool = False
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
    return table

def showErrorMessage(parent: QWidget, text: str, *, ms_delay: int = 2000):
    widget = createLabel(text, parent=parent)
    widget.setWindowFlags(Qt.ToolTip)
    widget.move(parent.mapToGlobal(QPoint()))
    widget.setStyleSheet("border: 2px solid #e31a17; border-radius: 5px; \
        padding: 2px; background-color: white; font-size: 14px;")
    widget.show()
    QTimer.singleShot(ms_delay, widget.hide)
    