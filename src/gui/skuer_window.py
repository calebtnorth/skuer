# Main GUI window for SKUer

from typing import Self

from PySide6.QtCore import QSize
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QGroupBox,
    QHBoxLayout, QGridLayout

)

class SKUMainWindow(QMainWindow):
    """
    Configure a QMainWindow with SKUer details to clean up code
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        # Configure window properties
        self.setWindowTitle("SKUer")
        self.setMinimumSize(QSize(800, 500))
        self.setCentralWidget(SKUMainWidget())


class SKUMainWidget(QWidget):
    """
    Parent widget for SKUer's main interface
    """

    def __init__(self: Self, *arg) -> None:        
        super().__init__(*arg)

        # Create all the major widget groups, set, and arrange them together 
        self.current_estimate_card_group:QGroupBox  = QGroupBox("Estimates")
        self.current_estimate_toolbar:QWidget       = QWidget()
        self.running_expenses_group:QGroupBox       = QGroupBox("Running Expenses")
        self.current_inventory_group:QGroupBox      = QGroupBox("Current Inventory")

        self.setLayout(QGridLayout())

        self.layout().addWidget(self.current_estimate_card_group, 0, 0, 2, 1)
        self.layout().addWidget(self.current_estimate_toolbar, 2, 0, 1, 2)
        self.layout().addWidget(self.running_expenses_group, 0, 1, 1, 1)
        self.layout().addWidget(self.current_inventory_group, 1, 1, 1, 1)

        


