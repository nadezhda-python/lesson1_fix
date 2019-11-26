"""

list_ = ['a', 'b', 'c', 'a', 'g']

#print(list_)
list_.append('g')
#print(list_)
#print(list_.count('a'))
#print(list_.index('a'))
#print ('b' in list_)
del list_[0]
print(list_)


test_list = [ 3, 5, 7, 9, 10.5]
print (test_list)
test_list.append('Python')
print (test_list)

print (test_list[0], ' ', test_list[-1])
print (test_list[1:4])
test_list.remove('Python')
print (test_list)


dict = dict(city = 'Москва', temperature = '20')
print (dict['city'])
dict['temperature'] = str(int(dict['temperature']) - 5)
print (dict)
#print ('country' in dict)
print(dict.get('country', 'Россия'))
print(dict)
dict.setdefault('country', 'Украина')
print(dict.get('country', 'Россия'))
dict['date']= '27.05.2019'
print (dict)
print (len(dict))
"""
x = 0
while x < 10:
    print(x)
x += 1

print (x)