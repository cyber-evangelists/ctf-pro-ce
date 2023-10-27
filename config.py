from dotenv import load_dotenv
import os
load_dotenv()
os.getenv
USERNAME = os.getenv("U_NAME")
PASSWORD = os.getenv("PASSWORD")

print(USERNAME, PASSWORD)