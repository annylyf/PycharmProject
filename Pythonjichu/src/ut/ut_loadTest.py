import unittest
import Testdemo2

class Demo(unittest.TestCase):
        def add(x,y):
            return x+y

if __name__=="__main__":
    print("run from main")
    suite = unittest.TestLoader().loadTestsFromTestCase(Testdemo2)
    unittest.TextTestRunner(verbosity=2).run(suite)

