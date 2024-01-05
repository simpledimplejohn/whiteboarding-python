## for in loop
list = [1,2,5,8,2,6,4,0]
movelist = []

for item in list:
    # print(item + 1)
    movelist.append(item)

# print(movelist)

## dictionary loops
my_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 5,
    'd' : 8
}

for key in my_dict:
    print(key, my_dict[key])

