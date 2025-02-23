import firebase_admin
from firebase_admin import credentials, db  

def initialize_firebase():
    # Path to your service account key
    cred = credentials.Certificate('teenguidenew-firebase-admin.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://teenguidenew-default-rtdb.europe-west1.firebasedatabase.app/'  # Your Realtime Database URL
    })
    
    # Realtime Database reference
    realtime_db = db.reference()
    return realtime_db
