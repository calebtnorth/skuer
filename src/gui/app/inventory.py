# Expense Card widget

from typing import Self

from PySide6.QtWidgets import (
    QGroupBox,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton, QTreeWidget, QTreeWidgetItem, QWidget
)


class ProductTreeWidgetTransactionItem(QTreeWidgetItem):
    """
    The child-level QTreeWidgetItem containing the individual transactions modifying the stock
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


class ProductTreeWidgetStockItem(QTreeWidgetItem):
    """
    The top-level QTreeWidgetItem containing the primary details of the product
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


class PartsListWidgetPartItem(QListWidgetItem):
    """
    The QListWidgetItem constaining a single part used in the product
    """

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


class ProductTreeWidget(QTreeWidget):
    """
    
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

    
    def addStockItem(self: Self, stock_item: ProductTreeWidgetStockItem) -> None:
        """
        Add a ProductTreeWidgetStockItem to the product list and assign its widget to itself
        """

        super().addTopLevelItem(stock_item)
        self.setItemWidget(stock_item, 0, stock_item.stock_widget)

    
    def addTransactionItem(self: Self, transaction_item: ProductTreeWidgetTransactionItem, stock_item: ProductTreeWidgetStockItem) -> None:
        """
        Add a ProductTreeWidgetTransactionItem to this ProductTreeWidgetStockItem and assign its widget to itself,
        if this ProductTreeWidgetStockItem has a parent. Otherwise it will fail and log an error, which should never happen.
        """

        if not stock_item.treeWidget():
            print("[!] No ProductTreeWidgetStockItem treeWidget when adding ProductTreeWidgetTransactionItem")
            return

        stock_item.addChild(transaction_item)
        self.setItemWidget(transaction_item, 0, transaction_item.transaction_widget)


class PartsListWidget(QListWidget):
    """
    
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

    
    def addPartsItem(self: Self, parts_item: PartsListWidgetPartItem) -> None:
        """
        Add a PartsListWidgetPartItem to the parts list and assign its widget to itself
        """

        super().addItem(parts_item)
        self.setItemWidget(parts_item, parts_item.part_widget)


class InventoryWidget(QGroupBox):
    """
    Displays the current inventory, regardless of estimate card
    """       

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        # List widgets
        self.product_tree_widget    = ProductTreeWidget()
        self.parts_list_widget      = PartsListWidget()

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

        self.parts_list_widget.addPartsItem(PartsListWidgetPartItem())