# Main GUI window for SKUer

from typing import Self

from PySide6.QtCore import (
    Qt
)
from PySide6.QtWidgets import (
    QMainWindow, QTabWidget
)

from ..widgets import *

from .estimate import *
from .stock import *
from .orders import * 
from .expenses import *


## MAIN WINDOW
class SKUMainWindow(QMainWindow):
    """
    Configure a QMainWindow with SKUer details to clean up code
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        # Configure window properties
        self.setWindowTitle("SKUer")
        self.setTabPosition(Qt.DockWidgetArea.AllDockWidgetAreas, QTabWidget.TabPosition.North)

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


        