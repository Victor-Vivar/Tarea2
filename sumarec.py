
list = [1,2,3,4,5,6,7,8,9,10]
def addition(list):
    if len(list) == 0:
        return 0
    return list.pop(-1) + addition(list)
print(addition(list))