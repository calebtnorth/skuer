# Expense Card widget

from typing import Self

from PySide6.QtWidgets import (
    QGroupBox, QWidget,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton
)

from ..widgets import (
    SKUerListWidget, SKUerListWidgetItem,
    SKUerTreeWidget, SKUerTreeWidgetItem
)

class ProductTreeWidgetTransactionItem(SKUerTreeWidgetItem):
    """
    The child-level QTreeWidgetItem containing the individual transactions modifying the stock
    """

    def widget(self: Self) -> QWidget:
        return self.transaction_widget

    
    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        self.transaction_widget         = QWidget()
        self.transaction_widget_layout  = QHBoxLayout(self.transaction_widget)

        self.transaction_widget_date_label      = QLabel("01/01/1970")
        self.transaction_widget_type_label      = QLabel("Restock")
        self.transaction_widget_sold_label      = QLabel("0")
        self.transaction_widget_in_stock_label  = QLabel("0")
        self.transaction_widget_total_label     = QLabel("0")

        self.transaction_widget_layout.addWidget(self.transaction_widget_date_label)
        self.transaction_widget_layout.addStretch(1)
        self.transaction_widget_layout.addWidget(self.transaction_widget_type_label)
        self.transaction_widget_layout.addStretch(1)
        self.transaction_widget_layout.addWidget(self.transaction_widget_sold_label)
        self.transaction_widget_layout.addWidget(self.transaction_widget_in_stock_label)
        self.transaction_widget_layout.addWidget(self.transaction_widget_total_label)

        self.setSizeHint(0, self.transaction_widget.sizeHint())


class ProductTreeWidgetStockItem(SKUerTreeWidgetItem):
    """
    The top-level QTreeWidgetItem containing the primary details of the product
    """

    def widget(self: Self) -> None:
        return self.stock_widget


    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        self.stock_widget           = QWidget()
        self.stock_widget_layout    = QHBoxLayout(self.stock_widget)
        
        self.stock_widget_sku_label         = QLabel("SKU")
        self.stock_widget_sold_label        = QLabel("0")
        self.stock_widget_in_stock_label    = QLabel("0")
        self.stock_widget_total_label       = QLabel("0")

        self.stock_widget_layout.addWidget(self.stock_widget_sku_label)
        self.stock_widget_layout.addStretch(1)
        self.stock_widget_layout.addWidget(self.stock_widget_sold_label)
        self.stock_widget_layout.addWidget(self.stock_widget_in_stock_label)
        self.stock_widget_layout.addWidget(self.stock_widget_total_label)

        self.setSizeHint(0, self.stock_widget.sizeHint())


class PartsListWidgetPartItem(SKUerListWidgetItem):
    """
    The QListWidgetItem constaining a single part used in the product
    """

    def widget(self: Self) -> QWidget:
        return self.part_widget

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        self.part_widget            = QWidget()
        self.part_widget_layout     = QHBoxLayout(self.part_widget)

        self.part_widget_name       = QLabel("Name")
        self.part_widget_sku        = QLabel("SKU")
        self.part_widget_used       = QLabel("0")
        self.part_widget_in_stock   = QLabel("0")

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.part_widget_name)
        vertical_layout.addWidget(self.part_widget_sku)

        self.part_widget_layout.addLayout(vertical_layout)
        self.part_widget_layout.addStretch(1)
        self.part_widget_layout.addWidget(self.part_widget_used)
        self.part_widget_layout.addWidget(self.part_widget_in_stock)

        self.setSizeHint(self.part_widget.sizeHint())


class InventoryWidget(QWidget):
    """
    Displays the current inventory, regardless of estimate card
    """       

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)
        
        # List widgets
        self.product_tree_widget    = SKUerTreeWidget()
        self.parts_list_widget      = SKUerListWidget()

        self.product_tree_widget.setHeaderHidden(True)

        # Buttons
        self.product_tree_push_button_layout    = QHBoxLayout()

        self.product_tree_add_push_button       = QPushButton("Add")
        self.product_tree_delete_push_button    = QPushButton("Delete")
        self.product_tree_estimate_push_button  = QPushButton("Estimate")

        self.product_tree_push_button_layout.addWidget(self.product_tree_add_push_button)
        self.product_tree_push_button_layout.addWidget(self.product_tree_delete_push_button)
        self.product_tree_push_button_layout.addStretch(1)
        self.product_tree_push_button_layout.addWidget(self.product_tree_estimate_push_button)

        # Main layout
        self.inventory_widget_layout = QGridLayout(self)
        self.inventory_widget_layout.addWidget(self.product_tree_widget, 0, 0, 1, 1)
        self.inventory_widget_layout.addWidget(self.parts_list_widget, 0, 1, 1, 1)
        self.inventory_widget_layout.addLayout(self.product_tree_push_button_layout, 1, 0, 1, 1)

        p = PartsListWidgetPartItem()
        self.parts_list_widget.addItem(p)
        p.part_widget_sku.setText("RSRY-059-MDL-WOOD")