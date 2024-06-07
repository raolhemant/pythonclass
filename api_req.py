import requests
r = requests.get(
    url="https://jsonplaceholder.typicode.com/posts"
)
print(r)
for x in r.json():
    print(x['title'])
    break