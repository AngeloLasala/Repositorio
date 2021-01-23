""" Assigment 1 """
import argparse
import time
import logging
import string

logging.basicConfig(level=logging.DEBUG)

def process(file):
    """ Read a file.tex and compute the basic statistic
    """
    start_time = time.time()

    with open(file) as input_file:
        text=input_file.read()
        logging.info('Total characters: %i ', len(text))
        
        chr_dic = {ch:0 for ch in string.ascii_lowercase}
        for ch in text:
            ch=ch.lower()
            if ch in chr_dic:
                chr_dic[ch] += 1
            else:
                pass
        for ch, num in chr_dic.items():
            print(f'{ch}: {num/sum(chr_dic.values()):.3f}')
        

    elapsed_time = time.time() - start_time
    logging.info('Run time: %.4f seconds', elapsed_time)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Process some file.txt')
    parser.add_argument('infile', type=str, help='Path to the input file')
    args = parser.parse_args()
    
    process(args.infile)  #args.infile è la variabile infile creata attraverso il panser