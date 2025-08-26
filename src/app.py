# SKUer Product and Inventory Software
# MIT (c) 2025 Caleb North

from sys import exit
from gui.gui_core import SKUApplication

sku_app = SKUApplication()

if __name__ == "__main__":
    exit(sku_app.exec())