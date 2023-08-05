import os

f = open('C:\\Users\\User\\Desktop\\python-test\\slaveresult.txt', 'r')

result = int (f.readline())

print(result)

if result ==1:
    os.system('python C:\\Users\\User\\PycharmProjects\\helloworld\\print.py')

else:
    exit()
