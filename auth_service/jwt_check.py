import jwt

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzM1MzMyMjQ0LCJpYXQiOjE3MzUzMzE5NDQsImp0aSI6IjM4YWNiMjIwMWFmZDQzOTJiMzFkMzg5YzRkNjViYzZlIiwidXNlcl9pZCI6MX0.wYJa8EGSTmK65BoI-TDKys03prIz5A35eYEZ6H9NiZk"
decoded_token = jwt.decode(token, options={"verify_signature": False})
print(f"Token Expiry Time: {decoded_token.get('exp')}")
