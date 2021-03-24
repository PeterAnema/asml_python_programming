
def banner1(text):
    n = len(text)
    print('***' + '*' * n + '***')
    print('*  ' + text    + '  *')
    print('***' + '*' * n + '***')


def banner2(text):
    n = len(text)
    s  = '***' + '*' * n + '***\n'
    s += '*  ' + text    + '  *\n'
    s += '***' + '*' * n + '***'
    return s

# ----------------------------------------------------------

banner1('Peter')

print(banner2('Peter'))