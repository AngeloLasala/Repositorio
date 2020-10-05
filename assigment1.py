"""qualcosa
"""
imput_book=input('Enter the path of book:')
f=open(imput_book,'r')
book=f.read()

alphabet = {('a','A'): 0, ('b'): 0, ('c'): 0, ('d'): 0}

for elements in alphabet:
    print(type(elements))
    for letters in book:
        if letters==elements :
            alphabet[elements]+=1
    print(elements,alphabet[elements])



