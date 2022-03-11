f = open('/home/jay/a.txt')
txt = f.read()
print(txt,type(txt))


def case_counter(string):
    lower_num = 0
    for char in string:
        if (char.islower()):
            lower_num = lower_num + 1
    print('This text has the number of lower case is: ',lower_num)

case_counter(txt)