import json

bigger_json = {
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

def print_deep_value(value):
    if isinstance(value,(list, tuple)):
        for item in value:
            print(item)
    elif isinstance(value, dict):
        print(json.dumps(value))
    else:
        print(value)


for key, value in bigger_json.items():
    print(f"{key}:")
    print_deep_value(value)
    print("--------------------------------")
    # if islist(value):
    #     print(f"{key}: {value}")



# print(json.dumps(bigger_json))

# file = '{"name": "Jan", "age": 18, "city": "Szczecin", "country": "Poland"}'
# file_parse = json.loads(file)
# # print(file_parse["age"])


# file_to_json ={
#     "name": "Rudolf",
#     "age": 22,
#     "city": "Berlin",
#     "country": "Germany"
# }
# file_json= json.dumps(file_to_json)
# parsed_json = json.loads(file_json)
# print(parsed_json["age"])