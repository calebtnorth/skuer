# Main GUI window for SKUer

from typing import Self

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QMainWindow, QTabWidget, QWidget, QGroupBox,
    QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy,
    QLabel
)

from .current_estimate import * 
from .inventory import *
from .running_expenses import *


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
        self.current_estimate_card:CurrentEstimateCardWidget        = CurrentEstimateCardWidget("Estimates")
        self.running_expenses:RunningExpensesWidget                 = RunningExpensesWidget("Running Expenses")
        self.current_estimate_toolbar:CurrentEstimateToolbarWidget  = CurrentEstimateToolbarWidget()

        self.current_inventory:InventoryWidget                      = InventoryWidget()
        self.currents:QTabWidget                                    = QTabWidget()
        self.currents.addTab(self.current_inventory, "Current Inventory")
        self.currents.addTab(QWidget(), "Current Stock")


        layout:QGridLayout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.current_estimate_card, 0, 0, 2, 1)
        layout.addWidget(self.current_estimate_toolbar, 2, 0, 1, 2)
        layout.addWidget(self.running_expenses, 0, 1, 1, 1)
        layout.addWidget(self.currents, 1, 1, 1, 1)

        # This ensures that the bottom row stays its size and will not stretch
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)
        layout.setRowStretch(2, 0)

        # TEMP TODO
        