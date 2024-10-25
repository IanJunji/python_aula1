a = 80000
b = 200000
txa = 1.03
txb = 1.015
anos = 1
while b >= a:
    anos += 1
    a *= txa
    b *= txb
print(anos)