import requests

# Step 1: Get the JWT token
url_token = "http://127.0.0.1:8000/api/auth/login/"
data = {
    "username": "user1",
    "password": "securepassword"
}

response = requests.post(url_token, data=data)
if response.status_code == 200:
    token = response.json()['access']  # Get the JWT token
    print(f"Token received: {token}")

    # Step 2: Use the token to add an AWB
    url_awb = "http://127.0.0.1:8001/api/category_1_service/awb/add/"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    awb_data = {
        "awb_number": "AWB1234567890",
        "sender_name": "John Doe",
        "receiver_name": "Jane Smith",
        "status": "shipped",
        "weight": "5kg"
    }

    awb_response = requests.post(url_awb, headers=headers, json=awb_data)
    if awb_response.status_code == 201:
        print("AWB Added Successfully:", awb_response.json())
    else:
        print("Failed to add AWB:", awb_response.status_code, awb_response.text)
else:
    print("Failed to get token:", response.status_code, response.text)
