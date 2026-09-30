import requests

from .firebase_config import FIREBASE_CONFIG

def create_user_document(user_id, username, email, id_token):
    url = (
        f"https://firestore.googleapis.com/v1/projects",
        f"{FIREBASE_CONFIG['project_id']}/databases/(default)/document/users",
        f"?documentId={user_id}"
    )

    headers = {
        "Authorization": f"Bearer {id_token}",
        "Content-Type": "applications/json"
    }

    data = {
        "fields": {
            "username": {
                "stringValue": username
            },
            "email": {
                "stringValue": email
            }
        }
    }

    response = requests.post(
        url,
        json=data,
        headers=headers
    )

    return response