import os
import json
import firebase_admin

service_account_info = json.loads(os.getenv('FIREBASE_SERVICE_ACCOUNT'))

cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred, {
    'storageBucket': 'baciti2.appspot.com'
})

bucket = storage.bucket()
