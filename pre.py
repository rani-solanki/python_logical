person={
    'name':'jack',
    'age':20,
    'gender':'male',
    4:'organisation'}

result = person['age']
adict=person.copy()
print(adict)
person["school"]="Gov.school.morena(m.p)"
x = person.get("gender")
y=person['name']="rani"
print(person['name'])
print(person[4])
print(x)
print(result)
print(person)


CAR_DETAILS={
    "brand": "Ford",
    "model": "jason",
    "year": 1964
}
CAR_DETAILS.pop("year")
print(CAR_DETAILS)

person={
    'name':'jack',
    'id':22,
    'place':'dharamsala'
}
person.popitem()
print(person)
