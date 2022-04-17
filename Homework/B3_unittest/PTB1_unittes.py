import unittest
import PTB1.PTB1 as PTB1

class Test_value(unittest.TestCase):
    def  Find_value_x(self):
        test = (3,4)
        self.assertEqual(PTB1.find_x(*test),-1)
        test = (0,0)
        self.assertEqual(PTB1.find_x(*test),"ALL")
        test = (0,3)
        self.assertEqual(PTB1.find_x(*test),"NONE")
if __name__ == "__main__":
    unittest.main(verbosity=2)
        
        
        
        