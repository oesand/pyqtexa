from typing import Unpack

from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import QMainWindow, QLayout

from .overlay_feature import OverlayFeature
from pyqtexa import widgets
from pyqtexa.widgets.box_layout import BoxLayoutKwargs
from pyqtexa.widgets.scroll import ScrollAreaKwargs


class OverlayModal:
    def __init__(self, **kwargs: Unpack[BoxLayoutKwargs]) -> None:
        self.parent: 'OverlayMixin' = None
        self.layout = widgets.boxLayout(**kwargs)

    def overlay(self, _parent: 'OverlayMixin', **kwargs) -> QLayout:
        self.parent = _parent
        return self.layout

    def hide(self, *, every: bool = False):
        self.parent.hideOverlay(every=every)


class OverlayMixin:
    def __init__(self) -> None:
        assert isinstance(self, QMainWindow), "Mixin must be extends from QMainWindow"
        self.overlayFeature = OverlayFeature(self)

    def showOverlay(
        self,
        content: QLayout | type[OverlayModal] | OverlayModal, *,
        closeManually: bool = True,
        closeEvery: bool = False,
        scrollKwargs: ScrollAreaKwargs | None = None,
        signal: dict = None
    ):
        if isinstance(content, type(OverlayModal)):
            content = content()
        if isinstance(content, OverlayModal) and signal:
            content = content.overlay(self, **(signal or {}))

        self.overlayFeature.show(
            content,
            closeManually=closeManually,
            closeEvery=closeEvery,
            scrollKwargs=scrollKwargs,
        )

    def hideOverlay(self, *, every: bool = False):
        self.overlayFeature.hide(every=every)

    def showTextMessage(self, text: str, *, okayText: str = "OK"):
        self.showOverlay(
            widgets.boxLayout(
                widgets=[
                    widgets.label(text=text),
                    widgets.button(text=okayText, onClicked= lambda _: self.hideOverlay())
                ]
            )
        )

    @property
    def overlayShown(self):
        return self.overlayFeature.shown

    def resizeEvent(self, event: QResizeEvent):
        super(QMainWindow, self).resizeEvent(event)
        if self.overlayFeature.shown:
            self.overlayFeature.onResizeWindow(event)
