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
    
    def update_from_file(self, file) -> str:
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
                DECRYPTING TRANSMITION:

                Date: {self.day}
                Left, Middle, Right Rotors: {self.rotorL} {self.rotorL} {self.rotorL}
                Ring Set LMR Rotors: {self.ringsetting_rotorL} {self.ringsetting_rotorM} {self.ringsetting_rotorR}
                Plug Board: {self.plugboard}
                Reflector: {self.reflector}
                '''
        #step 3
        self.configs += context
        f.close()
        print(self.configs)
        return self.configs
        
    def set_display(self, x) -> str:
        '''
        establishes a new starting position for a subsequent
        encrypt or decrypt operation
        '''
        rotorL.rotation,rotorM.rotation, rotorR.rotation = 0,0,0
        for i,v in enumerate(x):
            if i == 0:
                l = v
            elif i == 1:
                m = v
            else: 
                r = v

        rotorL.config_letter = str(l)
        rotorM.config_letter = str(m)
        rotorR.config_letter = str(r)

        context = f'''
                The rotors have been set to positions: 
                [{rotorL.config_letter} {rotorM.config_letter} {rotorR.config_letter}]
        '''
        print(context)
        return context

    def get_display(self) -> str:
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
    
    def count_rotors(self) -> list:
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

    def key_press(self, key) -> str:
        '''
        First the rotors are stepped by simulating the mechanical action of the
        machine. Next a simulated current is run through the machine. The lamp that is lit by this key press is
        returned as a string
        step 0: convert letter to number value in left wheel
        step 1: letter enters to left wheel, outputs left signal
        step 2: middle wheel recieves left wheels output signal, outputs left signal
        step 3: right wheel recieves left signal, outputs left signal
        step 4: reflector recieves left signal, outputs right signal (flipped letter)
        step 5: right wheel recieves right signal, outputs left signal
        step 6: middle wheel recieves right signal, outputs left signal
        step 7: left wheel recieves right signal, outputs left signal
        step 8: print returning letter as the encrypted letter
        '''
        #step 0
        initial_input= rotorL.letter_values[key] 
        #step 1
        rL_sl = rotorL.signal_from_left(initial_input)
        rL_sr = rotorL.signal_from_right(rL_sl)
        #step 2
        rM_sl = rotorM.signal_from_left(rL_sr)
        rM_sr = rotorM.signal_from_right(rM_sl)
        #step 3
        rR_sl = rotorR.signal_from_left(rM_sr)
        rR_sr = rotorR.signal_from_right(rR_sl)
        #step 4
        b4_reflect_letter = rotorR.position_values[rR_sr]
        reflect_pin = reflector.letter_values[b4_reflect_letter] 
        
        after_reflect_letter = rotorR.position_values[reflect_pin] #Dev purposes
        #step 5
        rotorR.rotate()
        rR_sr = rotorR.signal_from_right(reflect_pin)
        rR_sl = rotorR.signal_from_left(rR_sr)
        #step 6
        rotorR.rotate()
        rM_sr = rotorM.signal_from_right(rR_sl)
        rM_sl = rotorM.signal_from_left(rM_sr)
        # step 7
        rotorL.rotate()
        rL_sr = rotorL.signal_from_right(rM_sl)
        rL_sl = rotorL.signal_from_left(rL_sr)

        encrypted_letter = rotorL.position_values[rL_sl] 
        
        context = {'''
        print(f"{key} was converted to {initial_input} inside of the left wheel")
        print(f"The signal ENTERING wheel {self.rotorL} was {rL_sl} and LEAVING: {rL_sr}. Letter = {rotorL.position_values[rL_sl]}")
        print(f"The signal ENTERING wheel {self.rotorM} was {rM_sl} and LEAVING: {rM_sr}. Letter = {rotorM.position_values[rM_sr]}")
        print(f"The signal ENTERING wheel {self.rotorR} was {rR_sl} and LEAVING: {rR_sr}. The letter BEFORE reflector: {b4_reflect_letter}")
        print(f" The signal LEAVING reflector {self.reflector} was {reflect_pin}. The letter AFTER reflector: {after_reflect_letter}")
        print(f"{self.rotorR} recieved the signal {rR_sr} from reflecter pin and sent {rR_sl} to the left. Letter = {rotorR.position_values[rR_sl]} ")
        print(f"{self.rotorM} recieved the signal {rM_sr} from the right and sent {rM_sl} to the left. Letter = {rotorM.position_values[rM_sl]}")
        print(f"{self.rotorL} recieved the signal {rL_sr} from the right and sent {rL_sl} to the left. Letter = {rotorL.position_values[rL_sl]} ")
        '''}
        print(f"We began at {key} and ENCRYPTION value is: {encrypted_letter}")
        return encrypted_letter

    def process_txt(self,text, replace_char = 'YY') -> str:
        '''
        step 0: All input is converted to uppercase. 
        Step 1: The parameter replace_char controls what is done to input characters that are not A-Z. 
        Step 2: If the input text contains a character not on the keyboard, it is replaced with replace_char. 
        step 3: If replace_char is None the character is dropped from the input.
        step 4: Replace_char defaults to X.
        '''
        text.upper()
        encryption = ''
        
        for i,v in enumerate(text):
            if v.isalpha():
                encrypted_letter = self.key_press(v)
                encryption += encrypted_letter
            else:
                j = 'YY'
                encryption += j
        return encryption

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
e.update_from_file('my_enigma_keys.txt')

print("Updating Machine...")
print(e)


print('Configuring Enigma...')
print("Sending TO: ")
e.set_display('WXC') # set initial rotor positions
enc_key = e.process_txt('BLU') # encrypt message key
print(f"Encrypt Display key : {enc_key}")

# e.set_display('BLU') # use message key BLA
# print('ENCRYPTING text...')
# ciphertext = e.process_txt('THE RUSSIANS ARE COMING!')
# print(ciphertext)

print('Configuring Enigma...')
print("Recieving from: ")
e.set_display('WXC')
msg_key = e.process_txt('BLU')
print(f"Encrypt Display key : {msg_key}")
# e.set_display(msg_key) # original message key is BLA
# print("DECRYPTING text...")
# plaintext = e.process_txt('SDOYYEXLLNCELYYCEOYYSVDNELYY')
# print(plaintext)
