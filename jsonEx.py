import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
z = json.dumps(x)
print(z)

# Format the result
a = json.dumps(x, indent=4)
print(a)

b = json.dumps(x, indent=4, sort_keys=True)
print(b)

c = json.dumps(x, indent=4, separators=(". ", " = "))
print(c)
