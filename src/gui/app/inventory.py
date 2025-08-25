# Expense Card widget

from typing import Self

from PySide6.QtWidgets import (
    QGroupBox,
    QGridLayout, QHBoxLayout,
    QPushButton, QListWidget
)


class InventoryWidget(QGroupBox):
    """
    Displays the current inventory, regardless of estimate card
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        # List widgets
        self.product_list_widget    = QListWidget()
        self.parts_list_widget      = QListWidget()

        # Buttons
        self.product_list_push_button_layout    = QHBoxLayout()

        self.product_list_add_push_button       = QPushButton("Add")
        self.product_list_delete_push_button    = QPushButton("Delete")
        self.product_list_estimate_push_button  = QPushButton("Estimate")

        self.product_list_push_button_layout.addWidget(self.product_list_add_push_button)
        self.product_list_push_button_layout.addWidget(self.product_list_delete_push_button)
        self.product_list_push_button_layout.addStretch(1)
        self.product_list_push_button_layout.addWidget(self.product_list_estimate_push_button)

        # Inventory block layout
        self.inventory_widget_layout = QGridLayout(self)
        self.inventory_widget_layout.addWidget(self.product_list_widget, 0, 0, 1, 1)
        self.inventory_widget_layout.addWidget(self.parts_list_widget, 0, 1, 1, 1)
        self.inventory_widget_layout.addLayout(self.product_list_push_button_layout, 1, 0, 1, 1)