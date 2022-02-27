from enig3 import Enigma
from string import ascii_uppercase

def check_encription(before, after):
    string = ''

    for i,letter in enumerate(before):
        #I YY AM YY GOINT
        if letter == 'y' and i > 0 and i+1:
            if letter == 'y':
                string += 'Y'
        #step 2
        elif letter == ' ':
            string += 'YY'
        else:
            string += letter.upper()

    new_string = string.replace('YYY', 'YY')


    if new_string == after:
        print(f"Congratulations your code is working!!!")
        return True
    else:
        print(new_string)
        print(after)
        print("Whoops, looks like something went wrong. The two lists dont match")
        return False

if __name__ == '__main__':
    before = 'hello world this is my enigma machine'
    middle = 'GFKKPYYVPQKCYYSGJXYYJZYYNYYFMJHNRYYNTDGJMF'
    after = 'HELLOYYWORLDYYTHISYYISYYMYYENIGMAYYMACHINE'

    check_encription(before, after)


    'HELLOYYWORLDYYTHISYYISYYMYYENIGMAYYMACHINE'
    'HELLOYYWORLDYYTHISYYISYYMYYENIGMAYYMACHINE'