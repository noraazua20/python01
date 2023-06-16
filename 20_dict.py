person= {
'name':'nora',
'last_name':'azua',
'langs': ['python', 'javascript'],
'age': 39
}
print(person)

person['name'] = 'maria'#reemplazar un nombre
person['age'] -= 50 #restarle a la edad 50
person['langs'].append ('rust') #añadir algo a la lista al final
print(person)

del person['last_name']
person.pop('age') #eliminar la llave que queremos

print(person)

print('items')
print(person.items()) #genera tupla clave y valor

print('keys')
print(person.keys()) #genera solo llaves

print('values')
print(person.values()) #genera solo valores

#print(list(person.keys())) esto imprime la lista de las llaves pero en emulador aqui no