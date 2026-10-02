import requests

from .firebase_config import FIREBASE_CONFIG

def create_user_document(user_id, username, email, id_token):

    project_id = FIREBASE_CONFIG['projectId']
    url = f"https://firestore.googleapis.com/v1/projects/{project_id}/databases/(default)/documents/users?documentId={user_id}"

    headers = {
        "Authorization": f"Bearer {id_token}",
        "Content-Type": "application/json"
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

    if not response.ok:
        raise Exception(f"Firestore Error {response.status_code}: {response.text}")

    return response