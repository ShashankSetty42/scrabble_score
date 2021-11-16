from bs4 import BeautifulSoup
import requests

def get_text(fname):
    ret_str = ''
    with open(fname,'r') as ip:
        for line in ip:
            line = line.strip().replace(' ', '')
            line = (''.join([i for i in line if i.isalpha()])).upper()
            ret_str += line

    return ret_str

def get_points():
    return {
    'A':1,
    'B':3,
    'C':3,
    'D':2,
    'E':1,
    'F':4,
    'G':2,
    'H':4,
    'I':1,
    'J':8,
    'K':5,
    'L':1,
    'M':3,
    'N':1,
    'O':1,
    'P':3,
    'Q':10,
    'R':1,
    'S':1,
    'T':1,
    'U':1,
    'V':4,
    'W':4,
    'X':8,
    'Y':4,
    'Z':10
    }

def main():

    scores = get_points()
    raw_str = get_text('ip.txt')

    final_score = 0

    for item in raw_str:
        final_score += scores[item]

    print('final score is : ' + str(final_score))

if __name__ == "__main__":

    main()