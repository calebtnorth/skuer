# SKUer Core Functionality

from abc import abstractmethod
from typing import Self

from PySide6.QtWidgets import (
    QApplication, QWidget,
    QListWidget, QListWidgetItem, QTreeWidget, QTreeWidgetItem
)

from .app.main_window import SKUMainWindow
                

class SKUApplication(QApplication):
    """
    Creates a wrapped QApplication and "kicks off" the rest of SKUer
    """

    def __init__(self, *arg):
        super().__init__(*arg)

        # Create main window
        self.sku_main_window = SKUMainWindow()
        self.sku_main_window.show()