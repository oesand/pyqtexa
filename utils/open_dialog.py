from PyQt5.QtWidgets import QFileDialog
from .top_level import getMainWindow


def openExplorerDialog(*,
    title: str | None = None,
    initial: str | None = None,
    filter: str | None = None,
    file: bool = True,
    multiple: bool = False
):
    parent = getMainWindow()
    if not parent: return
    
    if file:
        if multiple:
            return QFileDialog.getOpenFileNames(
                parent=parent,
                caption=title,
                directory=initial,
                filter=filter
            )[0]
            
        return QFileDialog.getOpenFileName(
            parent=parent,
            caption=title,
            directory=initial,
            filter=filter
        )[0]
    
    return QFileDialog.getExistingDirectory(
        parent=parent,
        caption=title,
        directory=initial,
    )
