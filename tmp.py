
f = open("/Users/riccardocasciotti/Desktop/Prova/tmp/Relational Algebra in DBMS with Examples.txt", "r")
byte = " "

f.seek(18)
s = f.read()
print(s)
s= s.upper()
s = s.lower()
final = ""
for letter in s:
    #letter = str(letter.encode(encoding='UTF-8',errors='strict'))
    print(letter)
    print(ord(letter))
    if ord(letter) == 8:
        break
    final = final + letter
    
print(final)
f. close()
