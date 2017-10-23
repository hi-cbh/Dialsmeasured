import unittest




class MyTest(unittest.TestCase):


    @classmethod
    def setUpClass(self):
        print("setUp.....")
        self.testRun = False

    @classmethod
    def tearDownClass(self):
        print("tearDown......")


    def testCase01(self):
        print("testCase01")
        self.testRun = True
    #
    # @unittest.skipIf(unittest.testRun , "当条件为True跳过测试")
    # def test_skip_if(self):
    #     print("test bbb")
    #
    # @unittest.skipUnless(testRun, "当条件为True执行测试")
    # def test_skip_unless(self):
    #     print("test ccc")



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(MyTest('test_skip_if'))
    suite.addTest(MyTest('test_skip_unless'))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)