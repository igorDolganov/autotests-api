import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
access_token = f'Bearer {login_response_data["token"]["accessToken"]}'

headers = {"Authorization": access_token}
me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
print(f'статус код: {me_response.status_code}')
print(f'server response: {me_response.json()}')
