import httpx

from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
access_token = f'Bearer {login_response_data["token"]["accessToken"]}'
print('Login data:', login_response_data)

headers = {"Authorization": access_token}
patch_payload = {
    "email": get_random_email(),
    "password": "string1",
    "lastName": "string1",
    "firstName": "string1",
    "middleName": "string1"
}
patch_response = httpx.patch(f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
                             json=patch_payload, headers=headers)
print(patch_response.status_code)
print(patch_response.json())
