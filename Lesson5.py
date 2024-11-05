def func1():
    print('hello')

def func1(a):
    sum = 0
    for el in a:
        sum += el
    return sum

def func2(a, b):
    print(f'a = {str(a)}, b = {str(b)}')

def func3(a, b, c='default'):
    func2(a=a,b=b)
    print(f'c = {c}')

l1 = [1,5,2,6,8,2,1]
# print(func1(l1))

def sort(list):
    list_len = len(list)
    for j in range(list_len):
        isSorted = True
        for i in range(list_len - 1):
            if list[i] > list[i + 1]:
                tmp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = tmp
                isSorted = False
        if isSorted == True:
            break
    return list

print(sort(l1))







