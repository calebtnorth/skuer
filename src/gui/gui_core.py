# SKUer Core Functionality

# Imports
from PySide6.QtWidgets import QApplication

from .app.main_window import SKUMainWindow

# Classes
class SKUApplication(QApplication):
    """
    Creates a wrapped QApplication and "kicks off" the rest of SKUer
    """

    def __init__(self, *arg):
        super().__init__(*arg)

        # Create main window
        self.sku_main_window = SKUMainWindow()
        self.sku_main_window.show()