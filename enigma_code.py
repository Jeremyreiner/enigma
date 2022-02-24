from turtle import write_docstringdict
from sympy import ring
import random

class Enigma_machine:
    def __init__(self, name):
        super().__init__(self, name)
        self.name = name
        self.rotors_list = []
        self.reflector = []
        self.plugboard = []


class Roter_object:
    def __init__(self, model_name, ring_setting=0, stepping=None):
        self.model_name = model_name
        self.rotors_dict = {}
        self.rotors_list = []
        self.ring_setting = ring_setting
        self.stepping = stepping
        '''
        step 0: model_name: (string) – e.g. “I”, “II”, “III”, “Beta”, “Gamma”
        step 1: wiring: (string) 26 uppercase characters A-Z that represent
                    the internal wiring transformation of the signal
        step 2: ring_setting: (integer) 0-25, inclusive, which indicates the offset.
                    0 means there is no offset; e.g. the letter A is fixed 
                    top in 0. A value of 1 means B is mapped to pin 0 
        step 3: stepping: This argument specifies when rotors turn their neighbors. 
                    A value of None means this rotor does not rotate.
                    for example a string such as “Q”, this 
                    indicates that when the rotor transitions from “Q” to “R”
        '''
        wiring = {
            'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
        }
        # steps 0 & 1
        if wiring[model_name] == wiring['I']:
            wiring[model_name] = wiring['I']
            #append model name to list of rotors
            self.rotors_list.append(model_name)
            #append model name back to class function
            self.rotors_dict[model_name] = wiring[model_name]

        # steps 0 & 1
        elif wiring[model_name] == wiring['II']:
            wiring[model_name] = wiring['II']
            self.rotors_list.append(model_name)
            self.rotors_dict[model_name] = wiring[model_name]

        # steps 0 & 1
        elif wiring[model_name] == wiring['III']:
            wiring[model_name] = wiring['III']
            self.rotors_list.append(model_name)
            self.rotors_dict[model_name] = wiring[model_name]

        # if steps 0 & 1 failed model name and or wiring was misenterred/ misconfigured
        else:
            print("The wiring model name was entered incorrectly. Please Enter a correct Model. ex: 'I', 'II' or 'III'")
            return False

        # step 2
        if int(ring_setting) > 25:
            print("The Ring setting must be a number between 0 - 25")
            return False
        else:
            pass


class Reflector:
    def __init__(self, model_name, ring_setting=0, stepping=None):
        self.model_name = model_name
        self.rotors_dict = {}
        self.rotors_list = []
        self.ring_setting = ring_setting
        self.stepping = stepping
        
        wiring = {
            'B': 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
            'C':'BQPAIUOYEDXZRWCGTKJVSMFNHL'
        }

        if wiring[model_name] == wiring['B']:
            wiring[model_name] = wiring['B']
            #append model name to list of rotors
            self.rotors_list.append(model_name)
            #append model name back to class function
            self.rotors_dict[model_name] = wiring[model_name]

        # steps 0 & 1
        elif wiring[model_name] == wiring['C']:
            wiring[model_name] = wiring['C']
            self.rotors_list.append(model_name)
            self.rotors_dict[model_name] = wiring[model_name]

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


class PlugBoard:
    '''
        User has the option to insert up to 10 letter pairs in list form
        These pairs cannot have repeated letters ie; ['HJ', 'JS', 'MN',...]
        The list of pair ex: ['HE', 'JS', 'MN',...]
    '''
    def __init__(self, wire_pairs):
        self.wiring_pairs = wire_pairs
        self.to = []
        self.fro = []
        self.plug_directons = {}

        for i in range(len(wire_pairs)):
            value = wire_pairs[i]
            v1 = value[0]
            v2 = value[-1]
            self.to.append(v2)
            self.fro.append(v1)
            self.plug_directons[v1] = v2
            self.plug_directons[v2] = v1

# pairs =  ['HJ', 'TS', 'MN', 'LP', 'QW', 'UI']
# p = PlugBoard(pairs)
# print(p.plug_directons)
# print(p.to)
# print(p.fro)

# r1 = Reflector('B', '12')
# r2 = Reflector('C', '7', 'J')

# print(r2.rotors_list)
# print(r2.rotors_dict)
# print(r2.ring_setting)
# print(r2.stepping)

# r1 = Roter_object('I', '12')
# r2 = Roter_object('II', '7', 'J')
# r3 = Roter_object('III', '5')

# print(r2.rotors_list)
# print(r2.rotors_dict)
# print(r2.ring_setting)
# print(r2.stepping)
    

# def encrypt_enigma(ui):
#     machine = EnigmaMachine.from_key_sheet(
#         rotors='II IV V',
#         reflector='B',
#         ring_settings='B U L',
#         plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'
#     )
#     machine.set_display('WXC')
#     msg_key = machine.process_text('BLA')
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
#     msg_key = machine.process_text('KCH')
#     machine.set_display(msg_key)
#     decrypt_text = machine.process_text('NIBLFMYMLLUFWCASCSSNVHAZ')
#     print(decrypt_text)

        # nu_values = {
        #     'A': 0, 'J': 9,  'S': 18,
        #     'B': 1, 'K': 10, 'T': 19,
        #     'C': 2, 'L': 11, 'U': 20,
        #     'D': 3, 'M': 12, 'V': 21,
        #     'E': 4, 'N': 13, 'W': 22,
        #     'F': 5, 'O': 14, 'X': 23,
        #     'G': 6, 'P': 15, 'Y': 24,
        #     'H': 7, 'Q': 16, 'Z': 25,
        #     'I': 8, 'R': 17, 
        # }
        # sum_of_pairs = {}
        # checked = True
        # '''
        # step 0: initiate while loop with an if checked true var
        # step 1: once inside while, begin for loop iteration over 
        #         wired pairs
        # step 2: initiate nested for for iterating over each index
        # step 3: check the first index of the value by using a pointer
        #         index 0: from letter
        #         index 1: to letter
        # step 4: check if the pointer exceeds the value, reset the pointer
        # step 5: using the index of the Letter, refer back to the numbers_values table
        #         and find the numerical value of the indexed Letter
        # step 6: take the new value and store it in a temp var
        # step 7: end of first iteration, move the pointer
        # step 8: When For Loop breaks, return the value of the temp var
        #         and use it as a key to store the value of the index at 
        #         wired pairs.
        # step 9: return that checked is now False breaking out of while loop
        # step 10: 
        # '''
        # # while checked:
        # #     for index, value in enumerate(wire_pairs):
        # #         p = 0
        # #         str_sum = 2

        # #         for i in value:
        # #             length = len(value)
        # #             if p == 0:
        # #                 self.fro.append(i)
        # #             else:
        # #                 self.to.append(i)
        # #             if p > length:
        # #                 str_sum = 2
        # #             elif i in nu_values:
        # #                 str_sum *= nu_values[i]
        # #             p += 1
        # #         sum_of_pairs[str_sum] = value
        # #     checked = False
        
        # # for i in sum_of_pairs:
        # #     value = sum_of_pairs[i]
        # #     v1 = value[0]
        # #     v2 = value[-1]
        # #     self.plug_directons[v1] = v2
        # #     self.plug_directons[v2] = v1