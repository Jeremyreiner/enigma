from string import ascii_uppercase

class Enigma:
    def __init__(self, name, plugboard = {'':''}, config_settings = None, rotorL=None, rotorM=None, rotorR=None):
        self.letters = list(ascii_uppercase)
        self.name = name
        self.plugboard=plugboard
        self.config_settings = config_settings

        if self.config_settings != None:
            try:
                with open(config_settings, 'r') as f:
                    if f:
                        print("Incoming Transmission: ")
                        self.config_settings += f.readline()
            except:
                print('Enigma Error: No such setting configuration file found')

            finally:
                string = self.config_settings
                messenge = string.split()
                self.plugboard = {}
                self.rotorL = ''
                self.rotorM = ''
                self.rotorR = ''

                '''
                step 0: Initialize for loop for the length of the inbound message
                step 1: For each x amount of iterations a predetirmined 
                        configurations have been sent Update configs according
                step 2: If there is plugboard configurations, remove the configurations from 
                        the list of letters
                step 3: now that configs have been recieved update the machine
                step 4: Close the file and return configurations
                '''
                #step 0
                for i in range(len(messenge)):
                    # step 1
                    if i == 0:
                        pass
                    elif  i == 1:
                        self.day = messenge[i]
                    # step 1
                    elif 2 <= i <=4:
                        if i == 2:
                            self.rotorL += messenge[i]
                        elif i == 3:
                            self.rotorM += messenge[i]
                        else:
                            self.rotorR += messenge[i]
                    # step 1
                    elif 5 <= i <= len(messenge) -1:
                        for j in messenge[i]:
                            k = messenge[i][-1:]
                            if j not in self.plugboard:
                                self.plugboard[j] = k

                            if k not in self.plugboard:
                                self.plugboard[k] = j

                    else:
                        return f'''
                            The inbound message did not fit the code encryption style and can not be converted into this machine
                        '''
                #step 2
                for letter in list(self.plugboard.keys()):
                    '''
                    For the inputted pairs of plugboard numbers
                    Return the keys in list form and remove them from
                    from the list alphabet.
                    '''
                    if letter in self.letters:
                        self.letters.remove(letter)
                        self.letters.remove(self.plugboard[letter])
                        self.plugboard.update({self.plugboard[letter]: letter})
                        self.reflector = [letter for letter in self.letters[::-1]]
                #step 3
                context = f'''
                        {self.name} DECRYPTING TRANSMITION :

                        DATE: {self.day}
                        LEFT ROTOR: {self.rotorL} 
                        MIDDLE ROTOR: {self.rotorM}
                        RIGHT ROTOR: {self.rotorR}
                        PLUG BOARD CONFIGURATIONS: {self.plugboard}
                        '''
                #step 4
                self.config_settings += context
                f.close()
                self.rotorL = int(self.rotorL)
                self.rotorM = int(self.rotorM)
                self.rotorR = int(self.rotorR)

                print(self.config_settings)
        
        elif rotorL != None and rotorM != None and rotorR!= None and plugboard != None:
            '''
            If all files have been inputed,
            update the machine with the the given parameters.
            '''
            if type(plugboard) is not dict: 
                self.plugboard = {'':''}
            self.rotorL = rotorL
            self.rotorM = rotorM
            self.rotorR = rotorR
        
        else:
            '''
            If the machine has been manuelly filled but some parameter
            is either missing or filled out not as intended.
            '''
            if type(plugboard) is not dict: 
                    self.plugboard = {'':''}

            if rotorL != None:
                self.rotorL = rotorL
            else:
                self.rotorL = 0

            if rotorM != None:
                self.rotorM = rotorM
            else:
                self.rotorM = 0

            if rotorR != None:
                self.rotorR = rotorR
            else:
                self.rotorR = 0
            

            rotors = [self.rotorL,self.rotorM,self.rotorR]
            for rotor in rotors:
                if rotor == None or type(rotor) is not int or type(rotor) is not float:
                    rotor = 0
                else:
                    rotor = rotor % 26
            
            self.rotorL = rotors[0]
            self.rotorM = rotors[1]
            self.rotorR = rotors[2]

            for letter in list(self.plugboard.keys()):
                '''
                For the inputted pairs of plugboard numbers
                Return the keys in list form and remove them from
                from the list alphabet.
                '''
                if letter in self.letters:
                    self.letters.remove(letter)
                    self.letters.remove(self.plugboard[letter])
                    self.plugboard.update({self.plugboard[letter]: letter})
                    self.reflector = [letter for letter in self.letters[::-1]]



    def rotate_forward(self, rotor) -> list:
        new_letters = ''.join(self.letters)
        new_letters = list(new_letters)
        for i in range(rotor):
            '''
            return the last item of the alphebet to the begining of the list
            and remove the new last item/ ie current
            '''
            new_letters.insert(0, new_letters[-1])
            new_letters.pop(-1)
        return new_letters

    def rotate_reverse(self, rotor) -> list:
        new_letters = ''.join(self.letters)
        new_letters = list(new_letters)
        for i in range(rotor):
            new_letters.append(new_letters[0])
            new_letters.pop(0)

        return new_letters

    def view_rotor(self) -> int:
        context = f'''
            {self.name}'s ROTORS ARE CURRENTLY IN POSITIONS:

            LEFT ROTOR: {self.rotorL}
            MIDDLE ROTOR: {self.rotorM}
            RIGHT ROTOR: {self.rotorR}
            '''
        print(context)

    def decrypt_rotor_position(self, r1, r2, r3) -> int:
        '''
        Returns the Rotors actual position in number
        value IE. 012
        '''
        self.rotorL = self.letters.index(r1)
        self.rotorM = self.letters.index(r2)
        self.rotorR = self.letters.index(r3)

        context = f'''
            {self.name}'s ROTORS HAVE BEEN RECONFIGURED FROM:

            LEFT ROTOR: {r1}
            MIDDLE ROTOR: {r2}
            RIGHT ROTOR: {r3}

            {self.name}'s ROTORS HAVE BEEN RECONFIGURED TO:

            LEFT ROTOR: {self.rotorL}
            MIDDLE ROTOR: {self.rotorM}
            RIGHT ROTOR: {self.rotorR}
            '''
        print(context)
        return self.rotorL, self.rotorM, self.rotorR


    def encrypt_rotor_position(self) -> str:
        '''
        returns the rotors in positions ABC instead of
        number value of 012.
        '''
        l_position = self.rotorL % (len(self.letters) )
        M_position = self.rotorM % (len(self.letters) )
        R_position = self.rotorR % (len(self.letters) )

        rotorL = self.letters[l_position]
        rotorM = self.letters[M_position]
        rotorR = self.letters[R_position]
        #if self.letters[self.rotorL]:

        context = f'''
            {self.name}'s ROTORS OF HAVE BEEN ENCRYPTED TO:

            LEFT ROTOR: {rotorL}
            MIDDLE ROTOR: {rotorM}
            RIGHT ROTOR: {rotorR}
            '''
        print(context)
        return rotorL, rotorM, rotorR

    def set_rotors(self, r1, r2, r3):
        if r1 != None:
            self.rotorL = r1
        else:
            self.rotorL = 0

        if r2 != None:
            self.rotorM = r2
        else:
            self.rotorM = 0

        if r3 != None:
            self.rotorR = r3
        else:
            self.rotorR = 0

        context = f'''
                {self.name}'s ROTORS HAVE BEEN RE-SET TO POSITIONS:
                
                LEFT ROTOR: {self.rotorL}
                MIDDLE ROTOR: {self.rotorM}
                RIGHT ROTOR: {self.rotorR}
                '''
        print(context)

    def encryp_text(self, text) -> str:
        '''
        Using the same technique
        iterate throught the list and appends each value to a new list
        step 0: check to see if the letter will be flipped in the plugboard
        step 1: track the rotor location, and value. if the value exceeds the 
                index of the alphabet, reset and up the next rotor
                
        step 2: Check the string for spaces, or if decrypting, if the string has 
                the letter combo YY
        step 3: take the value of the rotor position, find the index within the alphabetm
                and return its letter value
        step 4: When the reflecter is hit, return the reflectors index value
        step 6: return the signal from the reflector to output. This will return your encryped/
                decrypted letter
        step 7:
        step 8:
        '''
        encrypted_txt = []
        text = text.upper()
        list1=list(text)
        p = 0
        for i, letter in enumerate(list1):
            #step 0 
            if letter in self.plugboard:
                encrypted_txt.append(self.plugboard[letter])
                self.rotorL += 1
                #step 1
                if self.rotorL % 26 == 0:
                    self.rotorM += 1
                    self.rotorL = 0
                #step 1
                if self.rotorM % 26 ==0 and self.rotorL % 26 ==0 and self.rotorM >= 25:
                    self.rotorR +=1
                    self.rotorM =1
            
            else:
                #step 2 because a space is one index, 

                p = i - 1
                r = i + 1
                length = len(text)
                # [p == 0 : p if p == -1] 
                if r >= length:
                    r = length - 1
                if p == -1:
                    p = 0

                if letter == ' ':
                    encrypted_txt.append('YY')

                elif letter == 'Y' and text[p] == 'Y':
                    encrypted_txt.append('Y')
                elif letter == 'Y' and text[r] == 'Y':
                    encrypted_txt.append('Y')

                else:
                    #step 4
                    temp_letter = self.rotate_forward(self.rotorL)[self.letters.index(letter)]
                    temp_letter = self.rotate_forward(self.rotorM)[self.letters.index(temp_letter)]
                    temp_letter = self.rotate_forward(self.rotorR)[self.letters.index(temp_letter)]
                    # step 5
                    temp_letter = self.reflector[self.letters.index(temp_letter)]
                    #step 6
                    temp_letter = self.rotate_reverse(self.rotorR)[self.letters.index(temp_letter)]
                    temp_letter = self.rotate_reverse(self.rotorM)[self.letters.index(temp_letter)]
                    temp_letter = self.rotate_reverse(self.rotorL)[self.letters.index(temp_letter)]

                    encrypted_txt.append(temp_letter)
            p = 0
        sting = ''.join(encrypted_txt)
        return sting



# ##todo IMPORTING MACHINE SETTINGS ENCRYPTION
# print(f"CONFIGURING ENIGMA SETTINGS...")
# encrypt = Enigma('Machine1',config_settings='my_enigma_keys.txt')

# ##todo ROTOR ENCRYPTIOIN
# print('ENCRYPTING ROTOR POSITIONS...')
# encrypt.encrypt_rotor_position()

# print('ENCRYPTING MESSAGE...')
# string_to_encrypt = 'hello world'
# message = encrypt.encryp_text(string_to_encrypt)
# print(f'ENCRYPTED MESSAGE: {message}')

# print(f"SECOND ENIGMA MACHINE INITIALIZED...")
# print(f"CONFIGURING ROTOR POSITIONS:")
# decrypt = Enigma('Machine2', config_settings='my_enigma_keys.txt')

# ##todo TAKE INPUT FROM ROTOR ENCRYPTION FOR THIS STEP
# decrypt.decrypt_rotor_position('B', 'S', 'Y')
# decrypt.set_rotors(1, 4, 10)

# print('DECRYPTING MESSAGE...')
# decrypt = decrypt.encryp_text(message)
# print(f'DECRYPTED MESSAGE: {decrypt}')




# todo HARD PUSHING CONFIGURATION SETTINGS
print(f"CONFIGURING ENIGMA SETTINGS...")
machine1 = Enigma('Machine1',{'A':'B', 'R':'S', 'E':'Z'}, rotorL=5, rotorM=17)

##todo ROTOR ENCRYPTION
machine1.view_rotor()
print('ENCRYPTING ROTOR POSITIONS...')
rotor_position = machine1.encrypt_rotor_position()

print('ENCRYPTING MESSAGE...')
string_to_encrypt = 'hello it'
message = machine1.encryp_text(string_to_encrypt)
print(f'ENCRYPTED MESSAGE: {message}')


##todo TAKE INPUT FROM ROTOR ENCRYPTION FOR THIS STEP
print(f"SECOND ENIGMA MACHINE INITIALIZED...")
machine2 = Enigma('Machine2',{'A':'B', 'R':'S', 'E':'Z'}, rotorL=5, rotorM=17)

print("CONFIGURING ROTOR POSITIONS:")
machine2.decrypt_rotor_position('I', 'W', 'C')
machine2.set_rotors(5, 17, 0)

print('DECRYPTING MESSAGE...')
decrypt = machine2.encryp_text(message)
print(f'DECRYPTED MESSAGE: {decrypt}')