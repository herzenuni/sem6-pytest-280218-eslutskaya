list1 = list('123456')
list2 = list('abcd')
#создаем списки разной длины

def dictionaryFromKeys(k, v):
    try:
        res = dict.fromkeys(k, None)
        res.update(zip(k, v))
    except TypeError:
        res = 'TypeError'
    return res

result = dictionaryFromKeys(list1, list2)
#получаме словарь
print (result)
