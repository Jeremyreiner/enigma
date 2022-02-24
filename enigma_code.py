from rotor_plugboard import RoterObject, ReflectorObject, PlugBoardObject

class Enigma_machine:
    def __init__(self, rotor1, rotor2, rotor3, reflector_config, plugboard_config):
        self.rotorL = rotor1
        self.rotorM = rotor2
        self.rotorR = rotor3
        self.reflector = reflector_config
        self.plug_board = plugboard_config
    
    def from_key_file(self, file):
        self.configs = ''
        with open('my_enigma_keys.txt', 'r') as f:
            if f:
                print("Incoming Transmission: ")
                self.configs += f.readline()

        string = self.configs
        list = string.split()

        self.plugboard = ''

        for i in range(len(list)):
            if i == 0:
                self.day = list[i]

            elif 1 <= i <=3:
                if i == 1:
                    self.r1 = list[i]
                elif i == 2:
                    self.r2 = list[i]
                else:
                    self.r3 = list[i]

            elif 4 <= i <= 6:
                if i == 4:
                    self.ringsetting_rotorL = list[i]
                if i == 5:
                    self.ringsetting_rotorM = list[i]
                else:
                    self.ringsetting_rotorR = list[i]

            elif 7 <= i <= 16:
                for j in list[i]:
                    if j == list[i][-1]:
                        self.plugboard += list[i]
                        self.plugboard += ' '

            else:
                self.reflect = list[i]

        context = f'''
                Date: {self.day}
                Left, Middle, Right Rotors: {self.r1} {self.r2} {self.r3}
                Ring Set LMR Rotors: {self.ringsetting_rotorL} {self.ringsetting_rotorM} {self.ringsetting_rotorR}
                Plug Board: {self.plugboard}
                Reflector: {self.reflect}
                '''

        self.configs += context
        f.close()
        return self.configs
        
    

    def __str__(self):

        context = f'''
            Rotors Models: [{self.rotorL}, {self.rotorM}, {self.rotorR}]
            Reflector Model: {self.reflector}
            PlugBoard Configurations: {self.plug_board}
            '''
        
        return context

rotorL = RoterObject('I')
rotorM = RoterObject('II')
rotorR = RoterObject('III')

reflector = ReflectorObject('B')

plugboard_config = PlugBoardObject('AV BS CG DL FU HZ IN KM OW RX')

machine = Enigma_machine(rotorL, rotorM, rotorR, reflector, plugboard_config)
file = machine.from_key_file('my_enigma_keys.txt')

print(file)


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