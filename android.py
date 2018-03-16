android = "Marvin, the Paranoid Android"
letters = list(android)

for char in letters[:6]:
    print('\t', char )
print()

for char in letters[-7:]:
    print('\t'*2, char )
print()

for char in letters[12:21]:
    print('\t'*3, char )
print()