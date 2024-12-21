import requests

response = requests.post(
    "http://localhost:52049/api/recommend",
    json={"songs": ["Yesterday", "Bohemian Rhapsody"]},
    headers={"Content-Type": "application/json"}
)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print(f"Request failed with status code {response.status_code}")