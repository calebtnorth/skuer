# Expense Card widget

from typing import Self

from PySide6.QtWidgets import (
    QWidget,
    QGridLayout, QHBoxLayout,
    QPushButton, QListWidget
)

class RunningExpensesWidget(QWidget):
    """
    Displays the running expenses, regardless of estimate card
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        # List widgets
        self.transactions_list_widget   = QListWidget()
        self.over_under_list_widget     = QListWidget()

        # Buttons
        self.transactions_list_push_button_layout   = QHBoxLayout()

        self.transactions_list_add_push_button      = QPushButton("Add")
        self.transactions_list_delete_push_button   = QPushButton("Delete")
        self.transactions_list_edit_push_button     = QPushButton("Edit")
        self.transactions_list_filter_push_button   = QPushButton("Filter")

        self.transactions_list_push_button_layout.addWidget(self.transactions_list_add_push_button)
        self.transactions_list_push_button_layout.addWidget(self.transactions_list_delete_push_button)
        self.transactions_list_push_button_layout.addWidget(self.transactions_list_edit_push_button)
        self.transactions_list_push_button_layout.addStretch(1)
        self.transactions_list_push_button_layout.addWidget(self.transactions_list_filter_push_button)

        # Main layout
        self.running_expenses_widget_layout = QGridLayout(self)
        self.running_expenses_widget_layout.addWidget(self.transactions_list_widget, 0, 0, 1, 1)
        self.running_expenses_widget_layout.addWidget(self.over_under_list_widget, 0, 1, 1, 1)
        self.running_expenses_widget_layout.addLayout(self.transactions_list_push_button_layout, 1, 0, 1, 1) 