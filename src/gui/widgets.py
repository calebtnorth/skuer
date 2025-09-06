# Custom widget overrides

from abc import abstractmethod
from typing import Self

from PySide6.QtWidgets import (
    QWidget,
    QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem
)


class SKUerListWidgetItem(QListWidgetItem):
    @abstractmethod
    def widget(self: Self) -> QWidget: ...


class SKUerListWidget(QListWidget):
    """
    Widget assignment functionality for QListWidgetItems
    """

    def addItem(self: Self, item: SKUerListWidgetItem) -> None:
        super().addItem(item)
        self.setItemWidget(item, item.widget())


class SKUerTreeWidgetItem(QTreeWidgetItem):
    @abstractmethod
    def widget() -> QWidget: ...

    def addChild(self: Self, item: Self):
        if not self.treeWidget():
            return

        super().addChild(item)
        self.treeWidget().setItemWidget(item, 0, item.widget())


class SKUerTreeWidget(QTreeWidget):
    """
    Widget assignment functionality for QTreeWidgetItems
    """

    def addTopLevelItem(self: Self, item: SKUerTreeWidgetItem) -> None:
        super().addTopLevelItem(item)
        self.setItemWidget(item, 0, item.widget())