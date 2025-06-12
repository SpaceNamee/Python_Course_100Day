import requests
from urllib.parse import urlencode
import base64
import webbrowser
import pprint

# ___________________ Spotify API Authentication ____________________
client_id = "a6e97d44cd504b52b724a9eddb4d1cb0"
client_secret = "f572b24aef98408c932fe02749b8ff96"

def get_token(client_id, client_secret):
    auth_headers = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": "http://127.0.0.1:8888/callback",
        "scope": "user-library-read"
    }

    webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

    code = "AQAfa1mKJ3JZCF75_oUqOZ2R9slhyDr4AIgUSkZBGmQpw4JqlEwqYppar4h-nBrFMFDQ6PWdVjn8Yecxjjw038sYnid6n13hjKLx6-gfsTKEt9mMcrYGy0gYOS8qmvaB32bvWgtwQ3D4oorWpfqXbxeSL6QVlyYQnPczuaIVCjZkkB5G7cY4LyGKMUzQvBq8VTBOD40"

    encoded_credentials = base64.b64encode(client_id.encode() + b':' + client_secret.encode()).decode("utf-8")

    token_headers = {
        "Authorization": "Basic " + encoded_credentials,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    token_data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://127.0.0.1:8888/callback"
    }

    r = requests.post("https://accounts.spotify.com/api/token", data=token_data, headers=token_headers)

    token = r.json()['access_token']
    return token

token = get_token(client_id, client_secret)

# ___________________ Spotify API Request ____________________
user_headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json"
}

user_params = {
    "limit": 5,
}

user_tracks_response = requests.get("https://api.spotify.com/v1/playlists/4Oomihal3911fU0S6Htp0x", params=user_params, headers=user_headers)

pprint.pprint(user_tracks_response.json())