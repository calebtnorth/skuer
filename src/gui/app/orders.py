# Current Orders widget

from typing import Self

from PySide6.QtWidgets import (
    QGroupBox, QWidget,
    QGridLayout, QHBoxLayout, QVBoxLayout,
    QDockWidget, QLabel, QPushButton
)

from ..widgets import (
    SKUerListWidget, SKUerListWidgetItem,
    SKUerTreeWidget, SKUerTreeWidgetItem
)

class OrdersListWidgetOrderItem(SKUerListWidgetItem):
    """
    The child-level QTreeWidgetItem containing the individual transactions modifying the stock
    """

    def widget(self: Self) -> QWidget:
        return self.order_widget

    
    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        self.order_widget               = QWidget()
        self.order_widget_layout        = QHBoxLayout(self.order_widget)

        self.order_widget_number_label              = QLabel("Order # NK000000")
        self.order_widget_date_label                = QLabel("01/01/1970")
        self.order_widget_expense_label             = QLabel("$0.00")
        self.order_widget_income_label              = QLabel("$0.00")

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.order_widget_expense_label)
        vertical_layout.addWidget(self.order_widget_income_label)

        self.order_widget_layout.addWidget(self.order_widget_number_label)
        self.order_widget_layout.addStretch(1)
        self.order_widget_layout.addWidget(self.order_widget_date_label)
        self.order_widget_layout.addStretch(1)
        self.order_widget_layout.addLayout(vertical_layout)

        self.setSizeHint(self.order_widget.sizeHint())


class ShippedPartsListWidgetShippedPartItem(SKUerListWidgetItem):
    """
    The QListWidgetItem constaining a single part used in the product
    """

    def widget(self: Self) -> QWidget:
        return self.shipped_part_widget

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        self.shipped_part_widget            = QWidget()
        self.shipped_part_widget_layout     = QHBoxLayout(self.shipped_part_widget)

        self.shipped_part_widget_sku_label        = QLabel("SKU")
        self.shipped_part_widget_used_label       = QLabel("0")
        self.shipped_part_widget_value_label      = QLabel("$0")

        self.shipped_part_widget_layout.addWidget(self.shipped_part_widget_sku_label)
        self.shipped_part_widget_layout.addStretch(1)
        self.shipped_part_widget_layout.addWidget(self.shipped_part_widget_used_label)
        self.shipped_part_widget_layout.addStretch(1)
        self.shipped_part_widget_layout.addWidget(self.shipped_part_widget_value_label)

        self.setSizeHint(self.shipped_part_widget_layout.sizeHint())


class OrdersDockWidget(QDockWidget):
    """
    Displays the current inventory, regardless of estimate card
    """       

    def __init__(self: Self, *arg) -> None:
        super().__init__("Orders", *arg)
        self.setWidget(QWidget())
        
        # Adjust dock features
        self.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures | QDockWidget.DockWidgetFeature.DockWidgetMovable)

        # List widgets
        self.orders_list_widget                 = SKUerListWidget()
        self.shipped_parts_list_widget          = SKUerListWidget()

        # Buttons
        self.orders_list_push_button_layout     = QHBoxLayout()

        self.orders_list_add_push_button        = QPushButton("Add")
        self.orders_list_delete_push_button     = QPushButton("Delete")

        self.orders_list_push_button_layout.addWidget(self.orders_list_add_push_button)
        self.orders_list_push_button_layout.addWidget(self.orders_list_delete_push_button)
        self.orders_list_push_button_layout.addStretch(1)

        # Main layout
        self.stock_widget_layout = QGridLayout(self.widget())
        self.stock_widget_layout.addWidget(self.orders_list_widget, 0, 0, 1, 1)
        self.stock_widget_layout.addWidget(self.shipped_parts_list_widget, 0, 1, 1, 1)
        self.stock_widget_layout.addLayout(self.orders_list_push_button_layout, 1, 0, 1, 1)

        o = OrdersListWidgetOrderItem()
        self.orders_list_widget.addItem(o)

        s = ShippedPartsListWidgetShippedPartItem()
        self.shipped_parts_list_widget.addItem(s)