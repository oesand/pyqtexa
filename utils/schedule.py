from typing import Callable
from PyQt5.QtCore import QTimer


def scheduleTimer(ms_delay: int, handle: Callable):
    QTimer.singleShot(ms_delay, handle)
