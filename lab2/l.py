
def brack(string):
    while '()' in string or '[]' in string or '{}' in string:
        string = string.replace('()', '')
        string = string.replace('[]', '')
        string = string.replace('{}', '')
    if len(string) == 0:
        return "Yes"
    else:
        return "No"
b = input()
print(brack(b))


