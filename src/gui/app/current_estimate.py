# Estimate Card widget

from typing import Self

from PySide6.QtWidgets import (
    QWidget, QGroupBox,
    QHBoxLayout, QSizePolicy
)
from PySide6.QtCore import (
    QRect
)


class CurrentEstimateCardWidget(QGroupBox):
    """
    
    """

    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)


class CurrentEstimateToolbarWidget(QWidget):
    """
    
    """
    
    def __init__(self: Self, *arg) -> None:
        super().__init__(*arg)

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setMinimumHeight(10)