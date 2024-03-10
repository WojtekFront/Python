import json
file = '{"name": "Jan", "age": 18, "city": "Szczecin", "country": "Poland"}'
file_parse = json.loads(file)
# print(file_parse["age"])


file_to_json ={
    "name": "Rudolf",
    "age": 22,
    "city": "Berlin",
    "country": "Germany"
}
file_json= json.dumps(file_to_json)
parsed_json = json.loads(file_json)
print(parsed_json["age"])