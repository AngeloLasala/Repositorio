"""qualcosa
"""
imput_book=input('Enter the path of book:')
f=open(imput_book,'r')
book=f.read()

alphabet = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0,
             'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0,
              'y': 0, 'z': 0}
alp =[['a','A'],['b','B'],['c','C'],['d','D'],['e','E'],['f','F'],['g','G'],['h','H'],['i','I'],['j','J'],['k','K'],['l','L']]

for lett_alp in alp:
    for lett_book in book:
        if lett_book==lett_alp[0] or lett_book==lett_alp[1]:
            alphabet[lett_alp[0]]+=1
    print(lett_alp[0],alphabet[lett_alp[0]])



