import sys
from PySide6 import QtWidgets

from homepage import ExcelFileImporter

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ExcelFileImporter()
    window.show()
    sys.exit(app.exec())