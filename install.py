import os
from utils import db_path
import json

data = []

if os.path.exists(db_path):
    print("Database already exists. Database initiation skipped.")
else:
    with open(db_path, "w") as f:
        json.dump(data, f, indent=4)
        print(f"Database installed at '{db_path}'")
