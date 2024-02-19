from PyQt5.QtGui import QDoubleValidator, QIntValidator


def rangeValidator(*, double: bool = False, start: int = 0, end: int = None):
    val = QDoubleValidator() if double else QIntValidator()
    if start is not None: val.setBottom(start)
    if end is not None: val.setTop(end)
    return val
