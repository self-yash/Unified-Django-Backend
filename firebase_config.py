import firebase_admin
from firebase_admin import credentials, firestore
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

cred = credentials.Certificate(
    os.path.join(BASE_DIR, r"firebase\secret_key.json")
)

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
