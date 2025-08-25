# Estimate Card widget

from typing import Self

from PySide6.QtWidgets import (
    QWidget, QGroupBox,
    QGridLayout, QVBoxLayout, QSizePolicy,
    QLabel, QListWidget
)
from PySide6.QtCore import (
    QRect
)


class CurrentEstimateCardWidget(QGroupBox):
    """
    
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        # List Widgets
        self.estimated_products_list_widget     = QListWidget()
        self.estimated_expenses_list_widget     = QListWidget()
        self.estimated_fees_list_widget         = QListWidget()

        # Labels
        self.estimate_card_numbers_layout       = QGridLayout()

        self.estimated_cost_label       = QLabel("$0.00")
        self.estimated_income_label     = QLabel("$0.00")
        self.estimated_expense_label    = QLabel("$0.00")
        
        self.actual_cost_label          = QLabel("$0.00")
        self.actual_income_label        = QLabel("$0.00")
        self.actual_expense_label       = QLabel("$0.00")

        self.estimate_card_numbers_layout.addWidget(self.estimated_cost_label, 0, 0, 1, 1)
        self.estimate_card_numbers_layout.addWidget(self.estimated_income_label, 2, 0, 1, 1)
        self.estimate_card_numbers_layout.addWidget(self.estimated_expense_label, 2, 1, 1, 1)

        self.estimate_card_numbers_layout.addWidget(self.actual_cost_label, 1, 0, 1, 1)
        self.estimate_card_numbers_layout.addWidget(self.actual_income_label, 3, 0, 1, 1)
        self.estimate_card_numbers_layout.addWidget(self.actual_expense_label, 3, 1, 1, 1)

        self.estimate_card_numbers_layout.setColumnStretch(0, 0)
        self.estimate_card_numbers_layout.setColumnStretch(1, 0)
        self.estimate_card_numbers_layout.setColumnStretch(2, 1)

        # Main Layout
        self.estimate_card_widget_layout = QVBoxLayout(self)
        self.estimate_card_widget_layout.addLayout(self.estimate_card_numbers_layout)
        self.estimate_card_widget_layout.addWidget(self.estimated_products_list_widget)
        self.estimate_card_widget_layout.addWidget(self.estimated_expenses_list_widget)
        self.estimate_card_widget_layout.addWidget(self.estimated_fees_list_widget)

class CurrentEstimateToolbarWidget(QWidget):
    """
    
    """
    
    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setMinimumHeight(10)