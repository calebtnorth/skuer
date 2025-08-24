# SKUer Product and Inventory Software
# MIT (c) 2025 Caleb North

from sys import exit
from gui.skuer_app import SKUApplication

sku_app = SKUApplication()

print(__name__)
if __name__ == "__main__":
    exit(sku_app.exec())