# Basic classe for Currents section

from typing import Self

from PySide6.QtWidgets import (
    QTabWidget, QWidget
)

from .stock import *
from .orders import *

## TABS
class CurrentTabWidget(QTabWidget):
    """
    
    """

    def __init__(self: Self, widgets:dict[str, QWidget], *arg) -> None:
        super().__init__(*arg)

        for name, widget in widgets.items():
            self.addTab(widget, name)
