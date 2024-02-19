from typing import Unpack
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMovie

from .label_widget import label
from .widget_wrap import WidgetKwargs


def gifView(
    path: str,
    **extra: Unpack[WidgetKwargs]
):
    container: QLabel = label(
        **extra,
        scaled=True,
        alignment="center",
    )
    
    movie = QMovie(path)
    container.setMovie(movie)
    movie.start()
    return container
