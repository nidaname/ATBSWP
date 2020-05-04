
def comma_code(someList):
    final_str = ''
    for item in someList[:-1]:
        final_str += str(item) + ', '
    final_str += 'and ' + str(someList[-1])
    return final_str

a = ['apples', 'bananas', 'tofu', 'cats']
b = comma_code(a)
print(b)