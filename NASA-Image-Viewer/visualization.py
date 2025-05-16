from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QTextBrowser
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
import requests
from io import BytesIO

class NASAImageViewer(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("NASA Image Gallery")
        self.setMinimumSize(800, 600)  # Minimum window size
        self.setMaximumSize(1600, 1200)  # Maximum window size

        self.data = data  # List of NASA images
        self.index = 0  # Track current image

        # Create UI elements
        self.image_label = QLabel(self)
        self.title_label = QLabel(self)
        self.explanation_label = QTextBrowser(self)  # Scrollable explanation box
        self.explanation_label.setFixedHeight(100)  # Prevent window resizing
        self.explanation_label.setOpenExternalLinks(True)  # Enable clickable links

        # Read More button (toggles explanation text)
        self.read_more_button = QPushButton("Read More", self)
        self.read_more_button.clicked.connect(self.toggle_explanation)

        # Navigation buttons (previous & next image)
        self.prev_button = QPushButton("Previous", self)
        self.prev_button.clicked.connect(self.prev_image)
        self.next_button = QPushButton("Next", self)
        self.next_button.clicked.connect(self.next_image)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.title_label)
        layout.addWidget(self.explanation_label)
        layout.addWidget(self.read_more_button)
        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.display_image()  # Show the first image

    def display_image(self):
        """Update GUI to show the current image."""
        entry = self.data[self.index]

        # Set title and truncated explanation
        self.title_label.setText(f"Title: {entry['title']}")
        self.explanation_label.setText(entry["explanation"][:200] + "...")
        self.read_more_button.setText("Read More")  # Reset button label

        # Fetch and display the image
        response = requests.get(entry["image_url"])
        pixmap = QPixmap()
        pixmap.loadFromData(BytesIO(response.content).read())
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

    def toggle_explanation(self):
        """Toggle between short and full explanation."""
        entry = self.data[self.index]
        if self.explanation_label.toPlainText() == entry["explanation"][:200] + "...":
            self.explanation_label.setText(entry["explanation"])  # Show full text
            self.read_more_button.setText("Show Less")
        else:
            self.explanation_label.setText(entry["explanation"][:200] + "...")  # Show short text
            self.read_more_button.setText("Read More")

    def prev_image(self):
        """Show the previous image."""
        if self.index > 0:
            self.index -= 1
            self.display_image()

    def next_image(self):
        """Show the next image."""
        if self.index < len(self.data) - 1:
            self.index += 1
            self.display_image()

def launch_gui(data):
    """Launch NASA Image Viewer GUI."""
    app = QApplication([])
    window = NASAImageViewer(data)
    window.show()
    app.exec_()