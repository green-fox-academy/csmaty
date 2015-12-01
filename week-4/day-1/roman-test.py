
def test(expected, actual, meaasage):
    if expected == actual:
        print('check')
    else:
        print(message)

def arabic2roman(arabic):
    return 'I' * arabic



test(arabic2roman(0), '', 'it should handle 0')
test(arabic2roman(1), 'I', 'it should handle 1')
test(arabic2roman(2), 'II', 'it should handle 2')
test(arabic2roman(4), 'IV', 'it should handle 4')
