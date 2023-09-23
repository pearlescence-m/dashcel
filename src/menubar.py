from PySide6 import QtWidgets, QtGui

class LeftPaneWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        left_pane_layout = QtWidgets.QVBoxLayout(self)

        # Create navigation buttons
        home_button = QtWidgets.QPushButton("Home", self)
        home_button.setIcon(QtGui.QIcon("../icons/home.svg"))
        dashboard_button = QtWidgets.QPushButton("Dashboard", self)
        dashboard_button.setIcon(QtGui.QIcon("../icons/pie-chart.svg"))
        info_button = QtWidgets.QPushButton("Info", self)
        info_button.setIcon(QtGui.QIcon("../icons/info.svg"))
        help_button = QtWidgets.QPushButton("Help", self)
        help_button.setIcon(QtGui.QIcon("../icons/help-circle.svg"))

        # Add navigation buttons to the left pane layout
        left_pane_layout.addWidget(home_button)
        left_pane_layout.addWidget(dashboard_button)
        left_pane_layout.addWidget(info_button)
        left_pane_layout.addWidget(help_button)