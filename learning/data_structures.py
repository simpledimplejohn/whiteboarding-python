## List [like arrays]
list = [1,2,3]

# print(list)


## sets {distinct}
my_set = {1,3,9,5,1}
# print(my_set)

## Dictionaryies {like objects}
my_dictionary = {
    'name' : 'john',
    'age' : 25,
    'stance' : 'open',
    'upsidedown' : False
}

# print(my_dictionary)

# temp = my_dictionary.update('name','joe')

my_dictionary['name'] = 'fred'
temp = my_dictionary['name']

# print('itmes:')
# print(my_dictionary.items())
# print('keys')
# print(my_dictionary.keys())
# print('values')
# print(my_dictionary.values())
# print("get")
# print(my_dictionary.get('name'))


# loop through the dictionary, keys, values, pairs
print("key loop")
for key in my_dictionary.keys():
    print("  ",key)
print("value loop")
for value in my_dictionary.values():
    print("  ",value)
print("pairs loop")
for key,value in my_dictionary.items():
    print("  ", key,value)