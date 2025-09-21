import requests
from datetime import datetime
import os

# --------------------------
# Configuration via environment variables
# --------------------------
USERNAME = os.environ.get("PIXELA_USERNAME", "your_name")
TOKEN = os.environ.get("PIXELA_TOKEN") 
GRAPH_ID = os.environ.get("PIXELA_GRAPH_ID", "graphID")

if not TOKEN:
    raise ValueError("PIXELA_TOKEN environment variable not set!")

# --------------------------
# Pixela endpoints
# --------------------------
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_CREATION_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

HEADERS = {"X-USER-TOKEN": TOKEN}

# --------------------------
# Create a pixel (habit log)
# --------------------------
def log_habit(quantity: float):
    today = datetime.now()
    pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity": str(quantity)
    }
    try:
        response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=HEADERS)
        response.raise_for_status()
        print(f"Success: {response.text}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err} - {response.text}")
    except Exception as e:
        print(f"Other error occurred: {e}")

# --------------------------
# Example usage
# --------------------------
if __name__ == "__main__":
    log_habit(10.0)  # Change the value to log different quantities
