# Expense Card widget

from typing import Self

from PySide6.QtWidgets import (
    QGroupBox,
    QGridLayout, QHBoxLayout,
    QComboBox, QLabel, QListWidget, QListWidgetItem, QPushButton, QWidget
)


class ProductListWidgetItemWidget(QWidget):
    """
    
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        self.product_list_widget_item_layout = QHBoxLayout(self)
        
        self.product_list_widget_item_combobox          = QComboBox()
        self.product_list_widget_item_sold_label        = QLabel("0")
        self.product_list_widget_item_in_stock_label    = QLabel("0")
        self.product_list_widget_item_total_label       = QLabel("0")

        self.product_list_widget_item_layout.addWidget(self.product_list_widget_item_combobox)
        self.product_list_widget_item_layout.addStretch(1)
        self.product_list_widget_item_layout.addWidget(self.product_list_widget_item_sold_label)
        self.product_list_widget_item_layout.addWidget(self.product_list_widget_item_in_stock_label)
        self.product_list_widget_item_layout.addWidget(self.product_list_widget_item_total_label)


class InventoryWidget(QGroupBox):
    """
    Displays the current inventory, regardless of estimate card
    """

    def add_product_list_widget_item(self: Self, item_widget: ProductListWidgetItemWidget) -> QListWidgetItem:
        """
        Add a new QListWidgetItem with an InventoryListWidgetItemWidget assigned to it
        """

        new_qlist_widget_item = QListWidgetItem()

        self.product_list_widget.addItem(new_qlist_widget_item)
        self.product_list_widget.setItemWidget(new_qlist_widget_item, item_widget)
        
        new_qlist_widget_item.setSizeHint(item_widget.sizeHint())
        return new_qlist_widget_item
    

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

        # Main layout
        self.inventory_widget_layout = QGridLayout(self)
        self.inventory_widget_layout.addWidget(self.product_list_widget, 0, 0, 1, 1)
        self.inventory_widget_layout.addWidget(self.parts_list_widget, 0, 1, 1, 1)
        self.inventory_widget_layout.addLayout(self.product_list_push_button_layout, 1, 0, 1, 1)

        self.add_product_list_widget_item(ProductListWidgetItemWidget())