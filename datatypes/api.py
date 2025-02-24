import requests
print(requests.__version__)
url= "https://reqres.in/api/users"
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to JSON
    print(data)  # Print the JSON response
else:
    print(f"Error: {response.status_code}")