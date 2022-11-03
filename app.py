import json
import requests
import settings
import os


base_url = 'https://petstore.swagger.io/v2'

# GET /user/login  Logs user into the system

res = requests.get(f'{base_url}/user/login?login={settings.valid_email}&password={settings.valid_password}',
                   headers={'accept': 'application/json'})

print(' GET /user/login  Logs user into the system Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# GET /user/logout  Logs out current logged in user session

res = requests.get(f'{base_url}/user/logout', headers={'accept': 'application/json'})

print(' GET /user/logout  Logs out current logged in user session Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# POST /user  Create user

body = json.dumps(settings.new_user)

res = requests.post(f'{base_url}/user', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                    data=body)

print(' POST /user  Create user Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# GET /user/{username} Get user by user name

username = settings.new_user['username']

res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print(' GET /user/{username} Get user by user name Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')


# PUT /user/{username} Updated user

username = settings.new_user['username']
body = json.dumps(settings.updated_user)

res = requests.put(f'{base_url}/user/{username}',
                   headers={'accept': 'application/json', 'Content-Type': 'application/json'}, data=body)

print(' PUT /user/{username} Updated user Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# DELETE /user/{username} Delete user

username = settings.updated_user['username']

res = requests.delete(f'{base_url}/user/{username}', headers={'accept': 'application/json'})

print(' DELETE /user/{username} Delete user Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# POST /user/createWithList Creates list of users with given input array

body = json.dumps(settings.new_users)

res = requests.post(f'{base_url}/user/createWithList', headers={'accept': 'application/json',
                                                                'Content-Type': 'application/json'}, data=body)

print(' POST /user/createWithList Creates list of users with given input array Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')


# POST /store/order  Place an order for a pet

body = json.dumps(settings.order)

res = requests.post(f'{base_url}/store/order', headers={'accept': 'application/json',
                                                        'Content-Type': 'application/json'}, data=body)
order_id = res.json()['id']

print(' POST /store/order  Place an order for a pet Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# GET /store/order/{orderId}  Find purchase order by ID

res = requests.get(f'{base_url}/store/order/{order_id}', headers={'accept': 'application/json'})

print(' GET /store/order/{orderId}  Find purchase order by ID Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# DELETE /store/order/{orderId}  Delete purchase order by ID

res = requests.delete(f'{base_url}/store/order/{order_id}', headers={'accept': 'application/json'})

print(' DELETE /store/order/{orderId}  Delete purchase order by ID Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# GET /store/inventory  Returns pet inventories by status

res = requests.get(f'{base_url}/store/inventory', headers={'accept': 'application/json'})

print(' GET /store/inventory  Returns pet inventories by status Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')


# GET /pet/findByStatus  Finds Pets by status

status = 'available'

res = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

print(' GET /pet/findByStatus  Finds Pets by status Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# POST /pet  Add a new pet to the store

body = json.dumps(settings.new_pet)

res = requests.post(f'{base_url}/pet', headers={'accept': 'application/json',
                                                'Content-Type': 'application/json'}, data=body)

pet_id = res.json()['id']

print(' POST /pet  Add a new pet to the store Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# PUT /pet  Update an existing pet

body = settings.new_pet
body['id'] = pet_id
body['name'] = 'Gennadiy'
body = json.dumps(body)

res = requests.put(f'{base_url}/pet', headers={'accept': 'application/json',
                                               'Content-Type': 'application/json'}, data=body)

print(' PUT /pet  Update an existing pet Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')

# GET /pet/{petId}  Find pet by ID

res = requests.get(f'{base_url}/pet/{pet_id}', headers={'accept': 'application/json'})

print(' GET /pet/{petId}  Find pet by ID Статус запроса:', res.status_code)
print('  Ответ сервера:', res.json(), '\n')


# POST /pet/{petId}  Updates a pet in the store with form data

name = 'Genchek'
status = 'new_status'
body = f'name={name}&status={status}'

res = requests.post(f'{base_url}/pet/{pet_id}', headers={'accept': 'application/json',
                                                        'Content-Type': 'application/x-www-form-urlencoded'}, data=body)

print(' POST /pet/{petId}  Updates a pet in the store with form data Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')


# POST /pet/{petId}/uploadImage  Uploads an image

#pet_photo = os.path.join(os.path.dirname(__file__), 'photo.jpg')
#file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

#res = requests.post(f'{base_url}/pet/{pet_id}/uploadImage', headers={'accept': 'application/json', 'Content-Type': 'multipart/form-data'}, files=file)

#print(' POST /pet/{petId}/uploadImage  Uploads an image Статус запроса:', res.status_code)
#print('  Ответ сервера:', res.json(), '\n')
#Этотзапрос не получилось реализовать


# DELETE /pet/{petId}  Deletes a pet

res = requests.delete(f'{base_url}/pet/{pet_id}', headers={'accept': 'application/json'})

print(' DELETE /pet/{petId}  Deletes a pet Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')