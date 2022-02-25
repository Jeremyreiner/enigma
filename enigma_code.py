from pyexpat import model
from rotor_plugboard import RoterObject, ReflectorObject, PlugBoardObject

class Enigma_machine:
    def __init__(self, rotor1, rotor2, rotor3, reflector_config, plugboard_config):
        super().__init__()
        self.rotorL = rotor1
        self.rotorM = rotor2
        self.rotorR = rotor3
        self.reflector = reflector_config
        self.plug_board = plugboard_config
        self.configs = ''
    
    def update_from_file(self, file):
        '''
        update machine with inbound encrypted messege
        '''
        with open('my_enigma_keys.txt', 'r') as f:
            if f:
                print("Incoming Transmission: ")
                #f.readline()
                self.configs += f.readline()

        string = self.configs
        list = string.split()

        self.plugboard = ''

        '''
        step 0: Initialize for loop for the length of the inbound message
        step 1: For each x amount of iterations a predetirmined 
                configurations have been sent Update configs according
        step 2: now that configs have been recieved update the machine
        step 3: Close the file and return configurations
        '''
        #step 0
        for i in range(len(list)):
            # step 1
            if i == 0:
                self.day = list[i]
            # step 1
            elif 1 <= i <=3:
                if i == 1:
                    self.rotorL = list[i]
                elif i == 2:
                    self.rotorM = list[i]
                else:
                    self.rotorR = list[i]
            # step 1
            elif 4 <= i <= 6:
                if i == 4:
                    self.ringsetting_rotorL = list[i]
                if i == 5:
                    self.ringsetting_rotorM = list[i]
                else:
                    self.ringsetting_rotorR = list[i]
            # step 1
            elif 7 <= i <= 16:
                for j in list[i]:
                    if j == list[i][-1]:
                        self.plugboard += list[i]
                        self.plugboard += ' '
            # step 1
            elif i == 17:
                self.reflector = list[i]
            else:
                return f'''
                    The inbound message did not fit the code encryption style and can not be converted into this machine
                '''
        
        # step 2
        # self.rotorL, self.rotorM, self.rotorR = self.r1, self.r2, self.r3
        # self.reflector = self.reflector_config
        self.plug_board = self.plugboard
        
        #step 2
        context = f'''
                Date: {self.day}
                Left, Middle, Right Rotors: {self.rotorL} {self.rotorL} {self.rotorL}
                Ring Set LMR Rotors: {self.ringsetting_rotorL} {self.ringsetting_rotorM} {self.ringsetting_rotorR}
                Plug Board: {self.plugboard}
                Reflector: {self.reflector}
                '''
        #step 3
        self.configs += context
        f.close()
        return self.configs
        
    def set_display(self, l, m, r):
        '''
        establishes a new starting position for a subsequent
        encrypt or decrypt operation
        '''
        rotorL.rotation,rotorM.rotation, rotorR.rotation = 0,0,0

        # rotorL.config_letter = ''
        # rotorM.config_letter = ''
        # rotorR.config_letter = ''

        rotorL.config_letter = str(l)
        rotorM.config_letter = str(m)
        rotorR.config_letter = str(r)

        context = f'''
                The rotors have been set to positions: 
                [{rotorL.config_letter} {rotorM.config_letter} {rotorR.config_letter}]
        '''
        print(context)
        return context

    def get_display(self):
        '''
        returns the current position of the rotors as a string
        '''

        left = rotorL.config_letter
        mid = rotorM.config_letter
        right = rotorR.config_letter

        context = f'''
                The rotors are currently in positions: 
                [{left} {mid} {right}]
        '''
        print(context)
        return context
    
    def count_rotors(self):
        '''
        Returns a list of integers that represent the rotation counts for each rotor.
        '''
        l = rotorL.rotation
        m = rotorM.rotation
        r = rotorR.rotation
        
        list = [l,m,r]
        context = f'''
            Left Roter Rotations: {rotorL.rotation}
            Middle Roter Rotations: {rotorM.rotation}
            Right Roter Rotations: {rotorR.rotation}
        '''
        print(context)
        return list


    def key_press(self, key):
        '''
        First the rotors are stepped by simulating the mechanical action of the
        machine. Next a simulated current is run through the machine. The lamp that is lit by this key press is
        returned as a string
        '''

        letter_values1 = rotorL.letter_values
        letter_values2 = rotorM.letter_values
        letter_values3 = rotorR.letter_values
        '''
        use the built in signal functions from each rotor to follow
        signal as inputted key starts from left and moves right towards
        the reflector. Signals again track the input from right to left'''
        self.l_value_of_key1, self.l_value_of_key2, self.l_value_of_key3  = 0,0,0

        if key in letter_values1:
            self.l_value_of_key1 += (letter_values1[key] + 1) #letter returns a number
            if self.l_value_of_key1 > 25:
                self.l_value_of_key1 += 0
            if key == rotorL.stepping:
                rotorM.rotate()
            rotorL.rotate()

        if key in letter_values2:
            self.l_value_of_key2 += (letter_values2[key] + 1) 
            if self.l_value_of_key2 > 25:
                self.l_value_of_key2 += 0
            if key == rotorM.stepping:
                rotorR.rotate()
            rotorM.rotate()

        if key in letter_values3:
            self.l_value_of_key3 += (letter_values3[key]+ 1)
            if self.l_value_of_key3 > 25:
                self.l_value_of_key3 += 0
            if key == rotorR.stepping:
                rotorL.rotate()
            rotorR.rotate()
        
        print(self.l_value_of_key1, self.l_value_of_key2, self.l_value_of_key3)

        conversion1, conversion2, conversion3 = self.l_value_of_key1, self.l_value_of_key2, self.l_value_of_key3

        num_values1, num_values2, num_values3 = rotorL.position_values, rotorM.position_values, rotorR.position_values
        
        self.n_value_of_key1, self.n_value_of_key2, self.n_value_of_key3 = '', '', ''

        if conversion1 in num_values1:
            self.n_value_of_key1 += num_values1[conversion1]
        if conversion2 in num_values2:
            self.n_value_of_key2 += num_values2[conversion2]
        if conversion3 in num_values3:
            self.n_value_of_key3 += num_values3[conversion3]

        print(self.n_value_of_key1, self.n_value_of_key2, self.n_value_of_key3)
        return self.n_value_of_key1, self.n_value_of_key2, self.n_value_of_key3





    def process_txt(self,text, replace_char = 'YY'):
        '''
        step 0: All input is converted to uppercase. 
        Step 1: The parameter replace_char controls what is done to input characters that are not A-Z. 
        Step 2: If the input text contains a character not on the keyboard, it is replaced with replace_char. 
        step 3: If replace_char is None the character is dropped from the input.
        step 4: Replace_char defaults to X.
        '''
        pass

    def __str__(self):

        context = f'''
            Rotors Models: [{self.rotorL}, {self.rotorM}, {self.rotorR}]
            Reflector Model: {self.reflector}
            PlugBoard Configurations: {self.plug_board}
            '''
        
        return context

#        TODO originally line 263
#     msg_key = machine.process_text('BLA')

rotorL = RoterObject('I')
rotorM = RoterObject('II')
rotorR = RoterObject('III')
reflector = ReflectorObject('B')
plugboard_config = PlugBoardObject('AV BS CG DL FU HZ IN KM OW RX')


e = Enigma_machine(rotorL, rotorM, rotorR, reflector, plugboard_config)
e.get_display()

e.update_from_file('my_enigma_keys.txt')

print("Updating Machine...")
print(e)

e.set_display("L", 'O', 'F')

key_press = e.key_press('H')
key_press = e.key_press('E')
key_press = e.key_press('L')
rotations = e.count_rotors()
key_press = e.key_press('L')
key_press = e.key_press('O')


e.set_display("E", 'J', 'I')

rotations = e.count_rotors()



# def encrypt_enigma(ui):
#     machine = EnigmaMachine.from_key_sheet(
#         rotors='II IV V',
#         reflector='B',
#         ring_settings='B U L',
#         plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
#     )
#     machine.set_display('WXC')
#     machine.set_display(msg_key)
#     text_to_encrypt = 'THEXRUSSIANSXAREXCOMINGX'
#     encrypted_text = machine.process_text(text_to_encrypt)
#     print(encrypted_text)
#     print(text_to_encrypt)

# def decrypt():
#     machine = EnigmaMachine.from_key_sheet(
#         rotors='II IV V',
#         reflector='B',
#         ring_settings='B U L',
#         plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
#     )
#     machine.set_display('WXC')
#      TODO
#     msg_key = machine.process_text('KCH')
#     machine.set_display(msg_key)
#     decrypt_text = machine.process_text('NIBLFMYMLLUFWCASCSSNVHAZ')
#     print(decrypt_text)



'''
        letter_values1 = rotorL.letter_values

        self.l_value_of_key1=0

        if key in letter_values1:
            self.l_value_of_key1 += (letter_values1[key] + 1) 
            if self.l_value_of_key1 > 25:
                self.l_value_of_key1 += 0
            if key == rotorL.stepping:
                rotorM.rotate()
            rotorL.rotate()
        
        print(self.l_value_of_key1)

        conversion1= self.l_value_of_key1 #store in var

        num_values1= rotorL.position_values # returns Letter
        
        self.n_value_of_key1= 0

        if conversion1 in num_values1:
            self.n_value_of_key1 += num_values1[conversion1]

        print(self.n_value_of_key1)
        return self.n_value_of_key1'''