from typing import Unpack
from PyQt5.QtWidgets import QWidget, QLayout, QTabWidget

from ..layout_wrap import LayoutWrap
from .widget_wrap import WidgetKwargs, widget as wrap_widget


def tabView(*,
    document_mode: bool | None = True,
    expanding: bool | None = True,
    tab_align: str | None = None,
    mapping: dict[str, QWidget | QLayout | LayoutWrap] | None = None,
    **extra: Unpack[WidgetKwargs]
):
    view = QTabWidget()
    
    if document_mode is not None:
        view.tabBar().setDocumentMode(document_mode)
    if expanding is not None:
        view.tabBar().setExpanding(expanding)
    
    if mapping:
        for title, child in mapping.items():
            if isinstance(child, LayoutWrap):
                child = child._extract()
            if isinstance(child, QLayout):
                child = wrap_widget(layout=child)
            if isinstance(child, QWidget):
                view.addTab(child, title)
    
    if tab_align:
        if tab_align == "top": view.setTabPosition(QTabWidget.TabPosition.North)
        elif tab_align == "bottom": view.setTabPosition(QTabWidget.TabPosition.South)
        elif tab_align == "left": view.setTabPosition(QTabWidget.TabPosition.West)
        elif tab_align == "right": view.setTabPosition(QTabWidget.TabPosition.East)
    
    if extra: wrap_widget(**extra, widget=view)
    return view
