import requests
import json

url = 'https://kickstarterbackend.herokuapp.com/model'
# body = '{"usd_goal": 10.0, "term":10, "category":0, "blurb":"text", "subcategory":0}'
u = 10
t = 10
c = 0
b = "text"
s = 1
body = {"usd_goal":u, "term":t, "category":, "blurb":b, "subcategory":s}
#b_json = json.loads(body)

response = requests.post(url, json=body, headers={'content-type':'application/json'})
print(response.json())

print(response.json()['prediction'])

