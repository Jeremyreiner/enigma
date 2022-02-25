class RoterObject:
    def __init__(self, model_name, ring_setting=0, stepping=None):
        self.model_name = model_name
        self.ring_setting = ring_setting
        self.stepping = stepping
        self.config_letter = ''
        self.config_num = ''
        self.letters = ''
        self.letter_values= {} #letter returns a number
        self.position_values = {} #number returns a letter
        self.rotation = 0
        '''
        step 0: model_name: (string) ex; 'I', 'II', 'III'
        step 1: wiring: (string) 26 uppercase characters A-Z that represent
                    the internal wiring transformation of the signal
        step 2: ring_setting: (integer) 0-25, inclusive, which indicates the offset.
                    0 means there is no offset, ex; the letter A is fixed 
                    top in 0.
        step 3: stepping: This argument specifies when rotors turn their neighbors. 
                    A value of None means this rotor does not rotate.
                    for example a string such as 'Q', this indicates that when 
                    the rotor transitions from 'Q' to 'R'
        '''
        wiring = {
            'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
        }

        # steps 0 & 1
        if wiring[model_name] == wiring['I']:
            self.wiring = wiring[model_name]
            for i,v in enumerate(wiring[model_name]):
                self.letter_values[v] = i
                self.position_values[i] = v
                self.letters += ''.join(v)
        # steps 0 & 1
        elif wiring[model_name] == wiring['II']:
            self.wiring = wiring[model_name]
            for i,v in enumerate(wiring[model_name]):
                self.letter_values[v] = i
                self.position_values[i] = v
                self.letters += ''.join(v)
        # steps 0 & 1
        elif wiring[model_name] == wiring['III']:
            self.wiring = wiring[model_name]
            for i,v in enumerate(wiring[model_name]):
                self.letter_values[v] = i
                self.position_values[i] = v
                self.letters += ''.join(v)
        # if steps 0 & 1 failed model name and or wiring was misenterred/ misconfigured
        else:
            print("The wiring model name was entered incorrectly. Please Enter a correct Model. ex: 'I', 'II' or 'III'")
            return False
        # step 2
        if ring_setting == str(ring_setting):
            if ring_setting in self.letter_values:
                ring_setting = self.letter_values[ring_setting]
                self.ring_setting = ring_setting
        else:
            ring_setting
            if 0 <= int(ring_setting) <= 25:
                self.ring_setting = ring_setting
            else:
                print("The Ring setting must be a number between 0 - 25")
                return False

    def set_display(self, rotar_position):
        '''
        Set the rotator to a specific position
        '''
        self.config_letter = ''
        if rotar_position > 25:
            rotar_position = 0

        if rotar_position == int(rotar_position):
            letter = self.position_values[rotar_position]
            self.config_letter += letter
            return self.config_letter
        else:
            self.config_letter += rotar_position
            return self.config_letter

    def get_display(self):
        '''
        returns the rotors visible position
        '''
        return self.config_letter

    def signal_from_right(self, num_contact):
        '''
        Simulate a signal entering the rotor 
        from the right at a given contact at position num_output.
        '''
        if 0 <= num_contact <= 25:
            shift = num_contact - int(self.ring_setting)
            index = (num_contact - ord('A')) % 26
            contact = (shift + index) % 26
            rotor_generated = self.wiring[contact]
            next_letter_value = self.letter_values[rotor_generated]
            self.signal_contact = next_letter_value
            return self.signal_contact
        else:
            print("Your signal value seems to be out of the expected range. Re-calculate your signal")


    def signal_from_left(self, num_pin):
        '''
        Simulate a signal entering the rotor 
        from the left at a given pin at position num_output.
        '''
        if 0 <= self.config_num <= 25:
            shift = int(self.ring_setting)
            index = self.wiring[num_pin]
            index_value = self.letter_values[index]
            contact = (shift + index_value) % 26
            rotor_generated = self.wiring[contact]
            next_letter_value = self.letter_values[rotor_generated]
            self.signal_pin = next_letter_value
            return self.signal_pin
        else:
            print("Your signal value seems to be out of the expected range. Re-calculate your signal")

    def step_notch(self):
        '''
        If a stepping position is given, return True
        other wise return false
        '''
        if self.stepping == None:
            return False
        else: 
            return True
    
    def rotate(self):
        '''
        Rotates the rotor forward.
        '''
        self.rotation += 1
        view = self.get_display()
        if view == str(view) and view != '':
            rotate_value= self.letter_values[view]
            rotate_value += 1
            new_view = self.set_display(rotate_value)
            print(f"{self.model_name} just rotated, I have {self.rotation} total rotations. View:{new_view}")
        else: 
            if view == '':
                view += '1'
                num = int(view)
            else:
                view+=1
            new_view = self.set_display(num)
            print(f"{self.model_name} just rotated, I have {self.rotation} total rotations. View:{new_view}")
        return new_view # returns int

    def letters_to_nums(self):
        def __dict__(self):
            conversion = self.position_values
            return conversion 

    def nums_to_letters(self):
        def __dict__(self):
            conversion = self.position_values
            return conversion

    def __str__(self):
        '''
        return object value in readable format
        '''
        context = f'''
                {self.model_name} 
                '''
        ## For developing perposes
        print(f'''Rotor Model: {self.model_name} 
        Rotor Wiring: {self.letters} 
        Rotor Ring Settings: {self.ring_setting} 
        Rotor Stepping: {self.stepping}''')
        return context


class ReflectorObject:
    '''
    Using the same concepts as a rotor, and returns a simple reflector object, with
    a name wiring combo, ring setting, and stepping parameters
    step 0: model_name: (string) ex; 'B', 'C'
    step 1: wiring: (string) 26 uppercase characters A-Z that represent
                the internal wiring transformation of the signal
    step 2: ring_setting: (integer) 0-25, inclusive, which indicates the offset.
                0 means there is no offset, ex; the letter A is fixed 
                top in 0.
    '''
    def __init__(self, model_name, ring_setting=0, stepping=None):
        self.model_name = model_name
        self.ring_setting = ring_setting
        self.letters = ''
        self.letter_values = {}
        #step 0, 1
        reflecter_wiring = {
            'B': 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
            'C':'BQPAIUOYEDXZRWCGTKJVSMFNHL'
        }
        #step 0, 1
        if reflecter_wiring[model_name] == reflecter_wiring['B']:
            self.wiring = reflecter_wiring[model_name]
            for i,v in enumerate(reflecter_wiring[model_name]):
                self.letter_values[v] = i
                self.letters += ''.join(v)
        #step 0, 1
        elif reflecter_wiring[model_name] == reflecter_wiring['C']:
            self.wiring = reflecter_wiring[model_name]
            for i,v in enumerate(reflecter_wiring[model_name]):
                self.letter_values[v] = i
                self.letters += ''.join(v)
        # if steps 0 & 1 failed model name and or wiring was misenterred/ misconfigured
        else:
            print("The wiring model name was entered incorrectly. Please Enter a correct Model. ex: 'B' or 'C'")
            return False
        # step 2
        if int(ring_setting) > 25:
            print("The Ring setting must be a number between 0 - 25")
            return False
        else:
            pass
    
    def __str__(self) :
        '''
        return object value in readable format
        '''
        context = f'''
                {self.model_name} 
                '''
        # For developing perposes
        print(f'''Reflector Model: {self.model_name} 
        Reflector Wiring: {self.letters} 
        Reflector Ring Settings: {self.ring_setting} 
        Reflector Stepping: {self.stepping}''')
        return context


class PlugBoardObject(RoterObject):
    '''
        User has the option to insert up to 10 letter pairs in string form
        These pairs cannot have repeated letters ie; 'H'J' 'J'S MN OP QW...'
        and must be capitalized. an example of a proper wire pairing is:  
        'PO ML IU KJ ... '
    step 0: If no wire pairings were provided, set the value to None
    step 1: If wire pairings were provided initialize empty dicrionary to 
            store all pairing values.
    step 2: initialize while loop through pairing values as well as 
            initialize pointers to track progress through values.
    step 3: if the lower value was not inside of the initial dictionary
            add both the values for A = B, as well as the reverse B = A.
    step 4: Add a number value using the rotor letter values/ position values.
    step 5: Using the pointers, add the low and high values back into dictionary
            as the keys:value pairing.
    TODO: NEED TO CONFIGURE USING INHERITENCE ON ROTOR VALUES
    '''
    def __init__(self, wire_pairings):
        self.keys = ''
        self.signal_to = ''
        self.signal_from = ''
        self.plug_directons = {}

        # #TODO
        # self.letter_values = RoterObject.letters_to_nums
        # self.position_values = RoterObject.nums_to_letters
        self.letter_values = {
            'A': 0, 'J': 9,  'S': 18,
            'B': 1, 'K': 10, 'T': 19,
            'C': 2, 'L': 11, 'U': 20,
            'D': 3, 'M': 12, 'V': 21,
            'E': 4, 'N': 13, 'W': 22,
            'F': 5, 'O': 14, 'X': 23,
            'G': 6, 'P': 15, 'Y': 24,
            'H': 7, 'Q': 16, 'Z': 25,
            'I': 8, 'R': 17, 
        }
        self.position_values = {
            0: 'A', 9: 'J',  18: 'S',
            1: 'B', 10: 'K', 19: 'T',
            2: 'C', 11: 'L', 20: 'U',
            3: 'D', 12: 'M', 21: 'V',
            4: 'E', 13: 'N', 22: 'W',
            5: 'F', 14: 'O', 23: 'X',
            6: 'G', 15: 'P', 24: 'Y',
            7: 'H', 16: 'Q', 25: 'Z',
            8: 'I', 17: 'R', 
        }

        #step 0
        if wire_pairings != None:
            #step 1
            self.wiring_pairs = {}
            lp,rp = 0, 1
            wire_pairings.strip()
            length =len(wire_pairings)

            #step 2
            while rp <= length -1:
                low = wire_pairings[lp]
                high = wire_pairings[rp]
                if length >= 1:
                    
                    #step 3
                    if low not in self.wiring_pairs:
                        self.wiring_pairs[low] = high
                        self.wiring_pairs[high] = low

                    #step 4
                    if low in self.letter_values:
                        self.signal_to += low

                    #step 4
                    if high in self.letter_values:
                        self.signal_from += high

                    #step 5
                    self.plug_directons[low] = high
                    self.plug_directons[high] = low

                    lp = rp + 2
                    rp = lp + 1
                else:
                    print("There was an error, enter in the wire pairings as from the example in the instructions.")
        else:
            wire_pairings = None

    def key_sheet(self, *args):
        '''
        Build a plugboard according to a settings string as you may find on a key
        sheet. For no plugboard connections, settings can be None or an empty string.
        example input: ['JS', 'AD', 'FR', ...]

        step 0: Check that the supplied list fits within the length of the plugboard
        step 1: Initialize pointers, and while loop to iterate through the list supplied.
        step 2: for each iteration, add the letter to a string. p pointer marking the index
                of the current list item, and l pointer marking the total iteration of the str
                item.
        step 3: If the l pointer is not divisible by to, add a space to the str var. Creating
                the desired key configuration.
        step 4: If the input is longer than the neccesary length for the plugboard return error.
        step 5: If settings were not entered, return the value as none or an empty string.
        '''
        list_to_string = ''.join(args)
        p,l=0,0
        length =len(list_to_string)
        str = ''
        # step 0
        if 0 < length <= 20:
            # step 1
            while l < length -1:
                # step 2
                for i in list_to_string:
                    low = i[p]
                    str += low
                    l +=1

                    # step 3
                    if l % 2 == 0:
                        str += ' '
            self.keys += str
            return str

        # step 4
        elif length > 20:
            print(f"{length}")
            print("There was an error, enter in the wire pairings as from the example in the instructions.")
            return False
        
        # step 5
        else:
            str = ''
            return str 

    def signal(self, n):
        '''
        Simulates a signal entering the plugboard on wire n, 
        where n must be an integer between 0 and 25.

        step 0: take input letter value n and convert to letter
        step 1: use plugboard to swap letter if theres a swap
        step 2: convert to letter to value
        step 3: return new letter value pin
        step 4:
        '''
        if 0 <= n <= 25:
            #step 0
            input_letter = self.position_values[n]
            # step 1
            index = self.plug_directons[input_letter]
            # step 2
            index_value = self.letter_values[index]
            
            # step 3
            self.signal = index_value
            
            context = f'''
                        Input letter: {input_letter}
                        letter Value: {n}
                        Plug Switch: {index}
                        Plug Switch Value: {index_value}
                        '''
            ## For Developing Purposes
            print(context)
            return self.signal
        else:
            print("Your signal value seems to be out of the expected range. Re-calculate your signal")
            return False
    
    def __str__(self) -> str:
        '''
        return object value in readable format
        '''
        context = f'''
                PlugBoard Pairs: {self.wiring_pairs} 
                '''
        ## For Developing Purposes
        print(f'''PlugBoard Pairs: {self.wiring_pairs} 
        PlugBoard Pairing To: {self.signal_to} 
        PlugBoard Pairing From: {self.signal_from} 
        PlugBoard keys: {self.keys} ''')
        return context
