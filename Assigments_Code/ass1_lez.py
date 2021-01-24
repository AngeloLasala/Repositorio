""" First assigment
"""

import argparse  #modulo che permette di dare comandi sulla linea di comando
import logging
import time
import string

logging.basicConfig(level=logging.DEBUG)

def process(file_path):
    """Read text file and compile the basic statistic
    """
    start_time=time.time()

    logging.info('Reading input file %s...', file_path)
    with open(file_path) as input_file:   #meglio con il with perchè il file è automaticamente chiuso all'uscita dal with, content management
        text=input_file.read()
    num_chars=len(text)
    logging.info('Done, %d charachters found',num_chars)


    #char_dict={chr(x): 0 for x in range(ord('a'),ord('z')+1)}  #alfabeto con tutti i valori 0
    char_dict= {ch:0 for ch in string.ascii_lowercase}
    for ch in text:
        # try:
        #     char_dict[ch.lower()]+=1
        # except KeyError:
        #     pass
        ch=ch.lower()
        if ch in char_dict:
            char_dict[ch]+=1


    elapsed_time=time.time()-start_time
    logging.info('Done in %.3f seconds',elapsed_time)
    num_letters=sum(char_dict.values())
    for ch, num in char_dict.items():
        print(f"{ch}->{num/num_letters:.3%}")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('infile',type=str,help='Path to the imput file')
    args=parser.parse_args()

    process(args.infile)

# queste sono le prime righe di codice che tutti i programmi devono vedere
