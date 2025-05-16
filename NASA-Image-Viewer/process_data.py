import json

def load_data(filename="nasa_data.json"):
    """Load and parse JSON data."""
    with open(filename, "r") as file:
        return json.load(file)

def extract_multiple_entries(data):
    """Extract list of image URLs, titles, and explanations."""
    extracted_entries = []
    for entry in data:
        extracted_entries.append({
            "title": entry.get("title", "N/A"),
            "date": entry.get("date", "N/A"),
            "explanation": entry.get("explanation", "N/A"),
            "image_url": entry.get("url", "N/A")
        })
    return extracted_entries