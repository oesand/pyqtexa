from typing import Unpack
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QImage, QPixmap

from .label_widget import label
from .widget_wrap import WidgetKwargs


def imageView(*,
    path: str = None,
    data: bytes = None, 
    **extra: Unpack[WidgetKwargs]
):
    assert path or data, "Source not specified"
    
    container: QLabel = label(
        **extra,
        text=None,
        scaled=True,
        alignment="center",
    )
    
    image = QImage()
    if path:
        image.load(path)
    elif data:
        image.loadFromData(data)
        
    pixmap = QPixmap.fromImage(image)
    del image
    container.setPixmap(pixmap)
    
    return container
