from fetch_data import fetch_nasa_data
from process_data import load_data, extract_multiple_entries
from visualization import launch_gui

def main():
    """Run NASA Image Gallery."""
    endpoint = "planetary/apod?start_date=2024-05-01&end_date=2024-05-07"
    fetch_nasa_data(endpoint)  # Fetch multiple images
    
    raw_data = load_data()  # Load JSON
    processed_data = extract_multiple_entries(raw_data)  # Extract multiple images
    
    launch_gui(processed_data)  # Show gallery GUI

if __name__ == "__main__":
    main()