#!/usr/bin/python3

data = {
    "name": "John",
    "age": None,
    "email": "john.doe@example.com",
    "phone": None
}

result = {k: v for k, v in data.items() if v is not None}

print(result)

# {'name': 'John', 'email': 'john.doe@example.com'}
