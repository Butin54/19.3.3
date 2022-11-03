import os

from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()

valid_email = os.getenv('valid_email')
valid_password = os.getenv('valid_password')

new_user = {
  "id": 0,
  "username": "qqqqq",
  "firstName": "qqqq",
  "lastName": "qqq",
  "email": "qqq@qqq.com",
  "password": "123456",
  "phone": "+123456789",
  "userStatus": 0
}

updated_user = {
  "id": 0,
  "username": "aaaaa",
  "firstName": "aaaa",
  "lastName": "aaa",
  "email": "aaa@aaa.com",
  "password": "654321",
  "phone": "+987654321",
  "userStatus": 0
}

new_users = [
  {
    "id": 0,
    "username": "1111",
    "firstName": "1111",
    "lastName": "1111",
    "email": "1111@1111.com",
    "password": "111111",
    "phone": "+1111111111",
    "userStatus": 0
  },
  {
    "id": 0,
    "username": "2222",
    "firstName": "2222",
    "lastName": "2222",
    "email": "2222@2222.com",
    "password": "222222",
    "phone": "+2222222222",
    "userStatus": 0
  }
]

order = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": datetime.now(timezone.utc).isoformat(),
  "status": "placed",
  "complete": True
}

new_pet = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "crocodile"
  },
  "name": "Gena",
  "photoUrls": [
    "None"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Tags"
    }
  ],
  "status": "available"
}