from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout,
    QLayout, QWidget
)
from ..layout_wrap import LayoutWrap
from ..utils import applyAlignment


def lineLayout(*,
    items: list[QLayout | QWidget | LayoutWrap] | None = None,
    vertical: bool = True,
    id: str | None = None,
    alignment: str | None = None,
    stretch: dict[int, int] | None = None,
    padding: tuple[int, int, int, int] | None = None,
    spacing: int | None = None,
) -> QVBoxLayout | QHBoxLayout:
    layout = QVBoxLayout() if vertical else QHBoxLayout()
    if id: layout.setObjectName(id)
    if items:
        for item in items:
            if isinstance(item, LayoutWrap):
                item = item._extract()
            if isinstance(item, QLayout):
                layout.addLayout(item)
            elif isinstance(item, QWidget):
                layout.addWidget(item)
    
    if padding: layout.setContentsMargins(*padding)
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
