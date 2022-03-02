from string import ascii_uppercase
import json

class Enigma():
    def __init__(self, name, plug_board={'':''}, config_file=None, rotorL=None, rotorM=None, rotorR=None, reflector= None, date=None):
        super().__init__()
        self.name = name
        self.alphabet = list(ascii_uppercase)
        self.config_file = config_file

        if config_file != None:
            try:
                # convert into JSON:
                f = open(config_file)
                data = json.load(f)
            except:
                print("Enigma Error 1: No such settings file has been found.")
            
            finally:
                # the result is a JSON string:
                json_string = data['settings']
                self.date = json_string['date']
                self.plugboard = json_string['plugboard']
                self.rotorL = json_string['rotorL']
                self.rotorM = json_string['rotorM']
                self.rotorR = json_string['rotorR']
                f.close()

                for letter in list(self.plugboard.keys()):
                    if letter in self.alphabet:
                        self.alphabet.remove(letter)
                        self.alphabet.remove(self.plugboard[letter])
                        self.plugboard.update({self.plugboard[letter]:letter})
                        self.reflector = [letter for letter in self.alphabet[::-1]]
                    else:
                        self.reflector = [letter for letter in self.alphabet[::-1]]
                
                context = f'''
                    {self.name}'S DECRYPTING TRANSMITION:
                    
                    DATE: {self.date}
                    PLUGBOARD CONFIGURATION: {self.plugboard}
                    LEFT ROTOR: {self.rotorL}
                    MIDDLE ROTOR: {self.rotorM}
                    RIGHT ROTOR: {self.rotorR}
                    '''
                print(context)

        elif rotorL != None and rotorM != None and rotorR != None and plug_board != None and reflector != None and date != None:
            '''
            All objects have been inputed correctly
            '''
            if type(date) is not int and type(date) is not float:
                self.date = 0
            else:
                self.date = date

            if type(plug_board) is not dict:
                self.plugboard = {'': ''}
            else:
                self.plugboard = plug_board
            
            for letter in list(self.plugboard.keys()):
                if letter in self.alphabet:
                    self.alphabet.remove(letter)
                    self.alphabet.remove(self.plugboard[letter])
                    self.plugboard.update({self.plugboard[letter]:letter})
                    self.reflector = [letter for letter in self.alphabet[::-1]]
                else:
                    self.reflector = [letter for letter in self.alphabet[::-1]]
            
            if rotorL == None and type(rotorL) is not int  and type(rotorL) is not float:
                self.rotorL = 0
            else:
                self.rotorL = rotorL % 26

            if rotorM == None and type(rotorM) is not int  and type(rotorM) is not float:
                self.rotorM = 0
            else:
                self.rotorM = rotorM % 26

            if rotorR == None and type(rotorR) is not int  and type(rotorR) is not float:
                self.rotorR = 0
            else:
                self.rotorR = rotorR % 26

            context = f'''
                    {self.name}'S SETTINGS HAVE BEEN CONFIGURED TO:
                    
                    DATE: {self.date}
                    PLUGBOARD CONFIGURATION: {self.plugboard}
                    LEFT ROTOR: {self.rotorL}
                    MIDDLE ROTOR: {self.rotorM}
                    RIGHT ROTOR: {self.rotorR}
                    '''
            print(context)

    def encrypt_rotors(self) -> list:
        '''
        Take rotors from: 123 and convert to: ABC
        '''
        left = self.rotorL % (len(self.alphabet))
        middle = self.rotorM % (len(self.alphabet))
        right = self.rotorR % (len(self.alphabet))

        rotorL = self.alphabet[left]
        rotorM = self.alphabet[middle]
        rotorR = self.alphabet[right]

        context = f'''
            {self.name}'s ROTORS HAVE BEEN ENCRYPTED TO

            LEFT ROTOR: {rotorL}
            MIDDLE ROTOR: {rotorM}
            RIGHT ROTOTR: {rotorR}
        '''
        print(context)
        self.rotors = [rotorL, rotorM, rotorR]
        return self.rotors

    def decrypt_rotors(self, rotors):
        for rotor in range(len(rotors)):
            if rotor == 0:
                r1 = rotors[rotor]
            elif rotor == 1:
                r2 = rotors[rotor]
            else:
                r3 = rotors[rotor]

        self.rotorL = self.alphabet.index(r1)
        self.rotorM = self.alphabet.index(r2)
        self.rotorR = self.alphabet.index(r3)

        context = f'''
            {self.name} HAS DECRYPTED ROTORS FROM:

            LEFT ROTOR: {r1} -> {self.rotorL}
            MIDDLE ROTOR: {r2} -> {self.rotorM}
            RIGHT ROTOTR: {r3} -> {self.rotorR}
        '''
        print(context)

    def set_rotors(self, left=None, middle=None, right=None):
        if left != None or type(left) is not str:
            self.rotorL = left
        else:
            self.rotorL = self.rotorL
        
        if middle != None or type(middle) is not str:
            self.rotorM = middle
        else:
            self.rotorM = self.rotorM
        
        if right != None or type(right) is not str:
            self.rotorR = right
        else:
            self.rotorR = self.rotorR

        context = f'''
            {self.name}'s ROTORS HAVE BEEN SET TO POSITIONS:
            
            LEFT ROTOR: {self.rotorL}
            MIDDLE ROTOR: {self.rotorM}
            RIGHT ROTOR: {self.rotorR}
            '''
        #print(context)
        return context

    def view_rotors(self):
        context = f'''
            {self.name}'s ROTORS CURRENT POSITIONS:
            
            LEFT ROTOR: {self.rotorL}
            MIDDLE ROTOR: {self.rotorM}
            RIGHT ROTOR: {self.rotorR}
            '''
        #print(context)
        return context
    
    def rotate_rotor_forward(self, rotor) -> list:
        new_letters = ''.join(self.alphabet)
        new_letters = list(new_letters)
        for i in range(rotor):
            new_letters.insert(0, new_letters[-1])
            new_letters.pop(-1)
        return new_letters
    
    def rotate_rotor_backward(self, rotor) ->list:
        new_letters = ''.join(self.alphabet)
        new_letters = list(new_letters)
        for i in range(rotor):
            new_letters.append(new_letters[0])
            new_letters.pop(0)
        return new_letters

    def encrypt_text(self, string) -> str:
        encrypted_text = []
        upper = string.upper()
        string_list = []
        for i in upper:
            string_list.append(i)
        
        for letter in string_list:
            if letter in self.plugboard:
                encrypted_text.append(self.plugboard[letter])
                self.rotorL +=1
                
                if self.rotorL % 26 == 0:
                    self.rotorM +=1
                    self.rotorL = 0

                if self.rotorM % 26 == 0 and self.rotorL % 26 == 0 and self.rotorM >= 25:
                    self.rotorR += 1
                    self.rotorM = 1

            elif letter not in ascii_uppercase:
                encrypted_text.append(' ')
            
            else:
                temp_letter = self.rotate_rotor_forward(self.rotorL)[self.alphabet.index(letter)]
                temp_letter = self.rotate_rotor_forward(self.rotorM)[self.alphabet.index(temp_letter)]
                temp_letter = self.rotate_rotor_forward(self.rotorR)[self.alphabet.index(temp_letter)]
                
                temp_letter = self.reflector[self.alphabet.index(temp_letter)]
                
                temp_letter = self.rotate_rotor_backward(self.rotorL)[self.alphabet.index(temp_letter)]
                temp_letter = self.rotate_rotor_backward(self.rotorM)[self.alphabet.index(temp_letter)]
                temp_letter = self.rotate_rotor_backward(self.rotorR)[self.alphabet.index(temp_letter)]

                encrypted_text.append(temp_letter)
        
        for item in range(0, len(encrypted_text)-1):
            if encrypted_text[item] not in ascii_uppercase:
                encrypted_text[item] = ' '
            # elif:
                
        self.encryption = ''.join(encrypted_text)
        #print(self.encryption)
        return self.encryption
    
    def read_encryption(self, text) -> str:
        string = text

        new_string = string.replace(' ', 'YY')
        return new_string


class Rotor:
    def __init__(self, position):
        '''
        A wheel of 26 values as seen throught the enigma object
        each number value returns a letter value.'''
        # self.name = name

        if position == None and type(position) is not int  and type(position) is not float:
            self.position = 0
        else:
            self.position = position % 26
    
    def current_position(self) -> int:
        #print(self.position)
        return self.position


class Plugboard:
    def __init__(self, plug_board = {'':''}) -> dict:
        '''
        dictionary object returns the value of the key stricken.
        '''
        if type(plug_board) is not dict:
            self.plug_board = {'':''}
        else:
            self.plug_board = plug_board
        #print(self.plug_board)
    
    def plugs(self):
        return self.plug_board


class Reflector:
    def __init__(self, plug_board=None):
        '''
        Recieves a letter durring encryption/ decryption and returns a different letter value
        '''
        self.alphabet = list(ascii_uppercase)
        
        if type(plug_board) is not dict:
            plug_board = {'':''}
            self.plugboard = plug_board
        else:
            self.plugboard = plug_board
            
        for letter in list(self.plugboard.keys()):
            if letter in self.alphabet:
                self.alphabet.remove(letter)
                self.alphabet.remove(self.plugboard[letter])
                self.plugboard.update({self.plugboard[letter]:letter})
                self.reflector = [letter for letter in self.alphabet[::-1]]
            else:
                self.reflector = [letter for letter in self.alphabet[::-1]]
    
    def reflecting_letters(self):
        return self.reflector

#todo initialize enigma machine using json
print('INITIALIZING ENIGMA MACHINE....')
m1 = Enigma(name='MACHINE 1', config_file='configs_file.json')

print('ENCRYPTING ROTOR POSITIONS....')
#todo encrypt rotor positions for other machine to decypher
rotors = Enigma.encrypt_rotors(m1)

print('ENCRYPTING MESSAGE....')
#todo initialize message for machine to encrypt
text_to_encrypt = 'hello world, check out this enigma code, encryption'
message = m1.encrypt_text(text_to_encrypt)
print(text_to_encrypt)

print('ENCRYPTED MESSAGE:')
#todo this removes all whitespace and non ascii values from string and replaces YY
encryption = m1.read_encryption(message)
print(encryption)



print('INITIALIZING ENIGMA MACHINE PARTS....')
print('INITIALIZING MACHINE ROTORS.....')
#todo initialize rotors
r = Rotor(1)
position1 = r.current_position()
r2 = Rotor(11)
position2 = r2.current_position()
r3 = Rotor(22)
position3 = r3.current_position()

print('INITIALIZING MACHINE PLUGBOARD OBJECT.....')
#todo initialize plugboard according to day transmition
p = Plugboard({"A": "B", "C": "D", "E": "F"})
plug_positions = p.plugs()

print('INITIALIZING MACHINE REFLECTOR OBJECT....')
#todo initialize reflector
reflect = Reflector(p.plug_board)

print('MACHINE READY FOR SERIALIZATION.')
#todo initialize enigma machine using initialized objects
m2 = Enigma('MACHINE 2',date=30, plug_board=plug_positions, rotorL=position1, rotorM=position2, rotorR=position3, reflector=reflect)

#todo recieve motor encryptions from machine 1 transmition
print('MACHINE RECIEVING ROTOR ENCRYPTIONS....')
rotor_decryption = m2.decrypt_rotors(rotors)

#todo set rotors to machine 1 positions
print('SETTING MACHINES ROTORS....')
set_rotors = m2.set_rotors(11, 3, 7)
view_rotors = m2.view_rotors()
print(view_rotors)

#todo decrypt message
print('PREPARING MACHINE FOR DECRYPTING MESSAGE....')
decryption = m2.encrypt_text(message)
read_text = m2.read_encryption(decryption)
print(read_text)