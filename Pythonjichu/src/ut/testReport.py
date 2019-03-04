import unittest
from ut import ut_democlass
import HTMLTestRunner


report_title = '执行报告'
desc = '测试用例执行报告'
report_file = 'ExampleReport.html'
testsuite = unittest.TestSuite()
testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ut_democlass.Demo))

with open(report_file,'wb') as report:
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=report,
        title='My unit test',
        description='This demonstrates the report output by HTMLTestRunner.'
    )
    print("I am running")
    runner.run(testsuite)