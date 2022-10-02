import os

from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
WEBSITE_IP = os.getenv("WEBSITE_IP")
WEBSITE_PORT = os.getenv("WEBSITE_PORT")
WEBSITE_UPL = f"http://{WEBSITE_IP}:{WEBSITE_PORT}"


