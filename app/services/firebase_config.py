import pyrebase

FIREBASE_CONFIG = {
  "apiKey": "AIzaSyD7Wr75immBajw0F1-JrTLdKDNXt_G4iGg",
  "authDomain": "pythongamehub.firebaseapp.com",
  "projectId": "pythongamehub",
  "storageBucket": "pythongamehub.firebasestorage.app",
  "messagingSenderId": "1050084360796",
  "appId": "1:1050084360796:web:9aa19b7d2c417a086edc99",
  "measurementId": "G-ZLD7NCG3D0"
}

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
auth = firebase.auth