import unittest
from enigma_code import  *
from string import ascii_uppercase

class TestAssertEqual(unittest.TestCase):
    def testString(self):
        list = []
        for i in text_to_encrypt.upper():
            if i not in ascii_uppercase:
                list.append(' ')
            else:
                list.append(i)
        new_string = ''.join(list)

        a = new_string
        b = decryption
        self.assertEqual(a, b)

    def testUnicode(self):
        list = []
        for i in text_to_encrypt.upper():
            if i not in ascii_uppercase:
                list.append(' ')
            else:
                list.append(i)
        new_string = ''.join(list)

        a = new_string
        b = message
        c = decryption
        print(a)
        print(b)
        print(c)
        self.assertNotEqual(a, b)
        self.assertNotEqual(b, c)

if __name__ == '__main__':
    unittest.main()