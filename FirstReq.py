import requests

# r = requests.get('https://reqres.in/api/users?page=2')
# print(r.text)
# print(r.json())
# json_data = r.json()
# print(json_data['data']['first_name'])
r = requests.post("https://reqres.in/api/users")
print(r)


