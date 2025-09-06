# Main GUI window for SKUer

from typing import Self

from PySide6.QtCore import QSize
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
        self.setCentralWidget(SKUMainWidget())


class SKUMainWidget(QWidget):
    """
    Parent widget for SKUer's main interface
    """

    def __init__(self: Self, *arg) -> None:        
        super().__init__(*arg)

        # Create all the major widget groups, set, and arrange them together 
        self.estimate_card_widget:CurrentEstimateCardWidget         = CurrentEstimateCardWidget()
        self.expenses_widget:RunningExpensesWidget                  = RunningExpensesWidget()
        self.stock_widget:StockWidget                               = StockWidget()
        self.orders_widget:OrdersWidget                             = OrdersWidget()
        self.current_tab_widget:CurrentTabWidget                    = CurrentTabWidget({
            "Orders": self.orders_widget,
            "Stock": self.stock_widget,
        })
        self.current_estimate_toolbar:CurrentEstimateToolbarWidget  = CurrentEstimateToolbarWidget()

        left_box:MainWindowGroupBox              = MainWindowGroupBox("Current Estimate", self.estimate_card_widget)
        upper_box:MainWindowGroupBox             = MainWindowGroupBox("Running Expenses", self.expenses_widget)
        lower_box:MainWindowGroupBox             = MainWindowGroupBox("Current Inventory", self.current_tab_widget)
        
        layout:QGridLayout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(left_box, 0, 0, 2, 1)
        layout.addWidget(upper_box, 0, 1, 1, 1)
        layout.addWidget(lower_box, 1, 1, 1, 1)
        layout.addWidget(self.current_estimate_toolbar, 2, 0, 1, 2)

        
        # This ensures that the bottom row stays its size and will not stretch
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 0)

        # TEMP TODO
        