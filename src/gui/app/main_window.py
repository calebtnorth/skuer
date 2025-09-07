# Main GUI window for SKUer

from typing import Self

from PySide6.QtCore import (
    QSize, Qt
)
from PySide6.QtWidgets import (
    QMainWindow, QGroupBox,
    QGridLayout, QHBoxLayout,
    QWidget
)

from ..widgets import *

from .estimate import *
from .current import * 
from .expenses import *


## GROUPBOX
class MainWindowGroupBox(QGroupBox):
    """
    Create a QGroupBox and add only a single widget
    """

    def __init__(self:Self, title:str, widget:QWidget, *args) -> None:
        super().__init__(title, *args)

        layout = QHBoxLayout(self)
        layout.addWidget(widget)


## MAIN WINDOW
class SKUMainWindow(QMainWindow):
    """
    Configure a QMainWindow with SKUer details to clean up code
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        # Configure window properties
        self.setWindowTitle("SKUer")

        # Create wdigets and docks and add them to the window
        self.estimate_widget        = CurrentEstimateCardDockWidget()
        self.expenses_widget        = RunningExpensesDockWidget()
        self.orders_widget          = OrdersDockWidget()
        self.stock_widget           = StockDockWidget()

        self.setCentralWidget(self.estimate_widget)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self.expenses_widget)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.orders_widget)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.stock_widget)
        self.tabifyDockWidget(self.orders_widget, self.stock_widget)


        