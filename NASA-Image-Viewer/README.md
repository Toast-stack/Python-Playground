# 🚀 NASA Image Viewer

## Overview
NASA Image Viewer is a **Python GUI application** that fetches **live astronomy images** from NASA's API and displays them inside a **PyQt5-powered interface**. Users can:
- 📸 **Browse multiple APOD images** retrieved from NASA.
- 🖼 **View images inside the GUI** (no external browser needed).
- 📜 **Read explanations** with an interactive "Read More" button.
- 🔄 **Cycle through images** using navigation buttons.

## Features
✅ **NASA API Integration** – Automatically pulls fresh images from NASA's Astronomy Picture of the Day (APOD).  
✅ **Embedded GUI (PyQt5)** – Fully integrated interface with image display, navigation, and scrollable explanations.  
✅ **Interactive Controls** – Navigate between images, expand text, and explore detailed descriptions.  
✅ **Modular Code Structure** – Organized into multiple scripts for easier expansion and maintenance.  

## Installation
### **Prerequisites**
Ensure you have Python installed (**3.8+ recommended**).

### **Install Required Libraries**
Run the following command to install them manually:
```bash
pip install PyQt5 PyQtWebEngine requests plotly pandas
```

## Usage
Clone the repository:
```Bash
git clone https://github.com/your-username/nasa-image-viewer.git
cd nasa-image-viewer
```

### Run the program:
```Bash
python main.py
```
## Project Structure
```
nasa_image_viewer/
│── fetch_data.py       # Handles NASA API requests & JSON storage
│── process_data.py     # Parses and extracts key details
│── visualization.py    # Displays images & explanations inside PyQt5 GUI
│── main.py             # Orchestrates everything
│── config.py           # Stores API key & constants
│── requirements.txt    # List of dependencies
│── README.md           # Project documentation
```

Configuration
Edit `config.py` with your NASA API key:
```Python
API_KEY = "your_api_key_here"
BASE_URL = "https://api.nasa.gov/"
```

Future Enhancements
- Expand to Mars Rover Images – Fetch photos from Curiosity & Perseverance.
- Add an Image Saving Feature – Allow users to store NASA images locally.
- Generate Reports – Export PDFs summarizing the retrieved images.

## Contributing
Want to improve this project? Feel free to submit a pull request or open an issue!

### 🛰 Powered by NASA Open APIs & PyQt5
### ⭐️ Give this repository a star if you found it useful
