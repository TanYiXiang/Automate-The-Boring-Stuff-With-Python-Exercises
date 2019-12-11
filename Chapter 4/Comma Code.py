spam = ['apples', 'bananas', 'tofu', 'pears', 'cats', 'dogs']


def comma_code(list_example):
    """"" Return String separated by comma based on list values """
    codeString = ''
    for i in range(len(list_example)):
        if i == 0:
            codeString += str(list_example[i])
        elif i == (len(list_example) - 1):
            codeString += ' and ' + str(list_example[i])
        else:
            codeString += ', ' + str(list_example[i])
    return codeString


print(comma_code(spam))
