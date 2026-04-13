details={
    "name":"Irreef",
    "age":22,
    "role":"Full  stack developer",
    "address":{ "area":"chennai", "pimcode":600126},
    "salary":40000 
}

print(details)

details["company"] = "PN Global Enterprises"
print(details)

details.pop("salary")
print(details)

for key,value in details.items():
    print(key,value)