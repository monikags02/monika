str = 'a123'
#str = '123'
try:
    i = float(str)
except (ValueError, TypeError):
    print('\n no')
print()
