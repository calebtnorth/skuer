# Custom widget overrides

from abc import abstractmethod
from typing import Self

from PySide6.QtCore import (
    Qt
)
from PySide6.QtWidgets import (
    QWidget,
    QDockWidget, QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem
)


## DOCKS
class SKUerDockWidget(QDockWidget):
    """
    Automatically assigns a widget to itself and sets some basic features
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        self.setWidget(QWidget())
        self.setFeatures(
            QDockWidget.DockWidgetFeature.NoDockWidgetFeatures | \
            QDockWidget.DockWidgetFeature.DockWidgetMovable
        )
        self.setAllowedAreas(
            Qt.DockWidgetArea.AllDockWidgetAreas & \
            ~Qt.DockWidgetArea.TopDockWidgetArea
        )


## LISTS 
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


## TREES
class SKUerTreeWidgetItem(QTreeWidgetItem):
    @abstractmethod
    def widget(self: Self) -> QWidget: ...

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