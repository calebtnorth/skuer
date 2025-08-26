# Expense Card widget

from typing import Self

from PySide6.QtWidgets import (
    QGroupBox,
    QGridLayout, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton, QTreeWidget, QTreeWidgetItem, QWidget
)


class ProductListWidgetTransactionItem(QTreeWidgetItem):
    """
    The _widget_ that is added to a child-level QTreeWidgetItem
    and contains the individual transactions modifying the stock
    """


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


class ProductListWidgetStockItem(QTreeWidgetItem):
    """
    The _widget_ that is added to a top-level QTreeWidgetItem
    and contains the primary details of the product
    """


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


class InventoryTreeWidget(QGroupBox):
    """
    Displays the current inventory, regardless of estimate card
    """

 
    # Inventory Management Functions #

    def add_StockItem(self: Self, product_item: ProductListWidgetStockItem) -> None:
        """
        Add this ProductListWidgetStockItem to the given product list and assign its widget to itself
        """

        self.product_list_widget.addTopLevelItem(product_item)
        self.product_list_widget.setItemWidget(product_item, 0, product_item.stock_widget)


    def add_TransactionItem(self: Self, transaction_item: ProductListWidgetTransactionItem, product_item: ProductListWidgetStockItem) -> None:
        """
        Add a ProductListWidgetTransactionItem to this ProductListWidgetStockItem and assign its widget to itself,
        if this ProductListWidgetStockItem has a parent. Otherwise it will fail and log an error, which should never happen.
        """

        if not product_item.treeWidget():
            print("[!] No ProductListWidgetStockItem treeWidget when adding ProductListWidgetTransactionItem")
            return

        product_item.addChild(transaction_item)
        self.product_list_widget.setItemWidget(transaction_item, 0, transaction_item.transaction_widget)


    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        # List widgets
        self.product_list_widget    = QTreeWidget()
        self.parts_list_widget      = QListWidget()

        self.product_list_widget.setHeaderHidden(True)

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
        self.inventory_widget_layout.addWidget(self.product_list_widget, 0, 0, 1, 1)
        self.inventory_widget_layout.addWidget(self.parts_list_widget, 0, 1, 1, 1)
        self.inventory_widget_layout.addLayout(self.product_tree_push_button_layout, 1, 0, 1, 1)