from dotenv import load_dotenv
import os

load_dotenv()

print("DB:", os.getenv("DB_NAME"))
print("DATA:", os.getenv("DATA_DIR"))
print("OUTPUT:", os.getenv("OUTPUT_DIR"))