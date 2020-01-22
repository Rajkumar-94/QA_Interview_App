from selenium import webdriver
import time
import unittest
import conf

class test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://qainterview.pythonanywhere.com/")
        
    def tearDown(self):
        self.driver.close()

    def test_factorial_function(self):
        actual_title=self.driver.title
        expected_title='Factoriall'
        if actual_title==expected_title:
            print("Launched the Factorial Page")
        else:
            print("Failed to launch Factorial page")
        while True:
            try:
                #fact_value=int(input("Enter the digit for which you want to obatain the Factorial Value: "))
                fact_value=conf.fact_value
                u_input=self.driver.find_element_by_xpath("//input[@id='number']")
                u_input.clear()
                u_input.send_keys('%d'%fact_value)
                self.driver.find_element_by_xpath("//button[@id='getFactorial']").click()
                time.sleep(3)
                if (0>=fact_value<171):
                    result=self.driver.find_element_by_xpath("//p[@id='resultDiv']")
                    print(result.text)
                    break
                elif (fact_value<0 or fact_value>989):
                    result=self.driver.find_element_by_xpath("//p[@id='resultDiv']")
                    print("Please enter a valid input to obatin the factorial")
                    print(result.text)
                else:
                    result=self.driver.find_element_by_xpath("//p[@id='resultDiv']").text
                    print(result)
                    break
            except ValueError:
                    print('Invalid input. Please provide a number')

    def test_terms(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Terms')]").click()
        try:
            self.driver.find_element_by_xpath("//body[contains(text(),'This is the terms')]")
        except Exception as e:
            #This pattern of catching all exceptions
            result_flag = False 
        else:
            result_flag = True
        if result_flag is True:
            print("The page navigated to Terms screen")
        else:
            print("The page did Not navigate to Terms screen")

    def test_privacy(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Privacy')]").click()
        if self.driver.current_url=='https://qainterview.pythonanywhere.com/privacy':
            print("The page navigated to Privacy screen")
        else:
            print("The page did Not navigate to Privacy screen")

    def test_qxf2link(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Qxf2')]").click()
        expected_title="Qxf2 Services: Outsourced Software QA for startups"
        actual_title=self.driver.title
        if expected_title==actual_title:
            print("Successufully navigated to Qxf2 Home Page")
        else:
            print("Failed to navigate to Qxf2 Home Page")
