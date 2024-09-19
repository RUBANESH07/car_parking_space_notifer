import os
from firebase_admin import credentials, initialize_app, storage

# Path to your Firebase Admin SDK JSON file
firebase_admin_sdk_path = os.path.join(os.path.dirname(__file__), 'login-97da6-firebase-adminsdk-96hga-2e8cef28a7.json')

# Initialize Firebase Admin SDK
cred = credentials.Certificate(firebase_admin_sdk_path)
initialize_app(cred, {
    'storageBucket': 'your-bucket-name.appspot.com'
})

# Get a reference to the storage service
bucket = storage.bucket()
