"""qualcosa
"""
imput_book=input('Enter the path of book:')
f=open(imput_book,'r')
book=f.read()

alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
alp =[['a','A'],['b','B'],['c','C'],['d','D']]

for lett_alp in alp:
    for lett_book in book:
        if lett_book==lett_alp[0] or lett_book==lett_alp[1]:
            alphabet[lett_alp[0]]+=1
    print(lett_alp[0],alphabet[lett_alp[0]])



