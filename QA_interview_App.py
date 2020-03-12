"""
The script is an example of automating Qxf2's QA interview app implemented in Selenium Python 
In this we test functinality of factorial, verify the obatained factorial value with expected value, verify Terms, Privacy and Qxf2 links.

Verifying the factorila is done by, converting the value to exponential e form and then compareing the 1st 4 digit and last 3 digit.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import math
import conf

def setUp():
    "This functions launched the browser and navigats to QA interview app page"
    global driver
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1400,1500")
    driver = webdriver.Chrome()
    #driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://qainterview.pythonanywhere.com/")
    
def tearDown():
    "This functions closes the browser"
    driver.quit()

def test_factorial_function():
    "This function verifies whether it is navigated toexpected screen, takes the input from user, checks whether the value is in range, calculates the factorial from the web page and from inbuilt module, compares the actual and obtained value and gives the result"
    
    #Checks whether it is in right page
    actual_title=driver.title
    expected_title='Factoriall'

    if actual_title==expected_title:
        print("Successfully launched the Factorial Page")
    else:
        print("Failed to launch Factorial page")


    while True:
        try:
            #Takes the input value from user
            #fact_value=int(input("Enter the digit for which you want to obatain the Factorial Value: "))
            fact_value=conf.fact_value
            u_input=driver.find_element_by_xpath("//input[@id='number']")
            u_input.clear()
            u_input.send_keys('%d'%fact_value)
            driver.find_element_by_xpath("//button[@id='getFactorial']").click()
            time.sleep(3)
            #If Loop based on the user input
            if (fact_value>=0 and fact_value<171):

                #Python code using inbuilt module to obatain factorial value for the given input"
                p_fact_value=math.factorial(fact_value)
                

                #Formats the interger to exponential e, so that it can be compared with Web App result
                p_formatted=format(p_fact_value,'e')
                print("The factorial value using by factorial function via math module is ",p_formatted)
                p_output=p_formatted.split(" ")
                p_value=p_output[-1]
                
                #Takes the 1st 4 digit and stores to compare with the Web App result
                p_biginning=p_value[0:5]
                
                #Takes the last 3 digit and stores to compare with the Web App result
                p_ending=p_value[-3:]
                

                #Extracts the factorial value from the Web Application
                result=driver.find_element_by_xpath("//p[@id='resultDiv']").text
                print(result)
                result_list=result.split(" ")
                factorial_value=result_list[-1]
                try:
                    #If the obtained value is in decimal, this will convert to to exponential e form to compare
                    factorial_value=int(result_list[-1])
                    formatted_fact=format(factorial_value,'e')
                    converted_string=str(formatted_fact)
                except ValueError:
                    converted_string=factorial_value
                biginning_digit=converted_string[0:5]
                ending_digit=converted_string[-3:]

                #If loop to comapre the Web App result with the factorial function result.
                if (biginning_digit==p_biginning and ending_digit==p_ending):
                    print("Pass: Actual Factorial Value and Obtained Factorial Value are matched")
                else:
                    print("Fail: Mismatch between Actual Factorial Value and Obtained Factorial Value")
                break

            elif (fact_value>170  and fact_value<990):
                result=driver.find_element_by_xpath("//p[@id='resultDiv']").text
                print(result)
                break

            elif (fact_value<0 or fact_value>989):
                result=driver.find_element_by_xpath("//p[@id='resultDiv']")
                print("Please enter the valid integer less than 990 to get the factorial value")
                print(result.text)

        except ValueError:
                print('Invalid input. Please insert a valid integer')
    
def test_terms():
    "This function used to verify the Terms link"
    driver.find_element_by_xpath("//a[contains(text(),'Terms')]").click()
    
    try:
        driver.find_element_by_xpath("//body[contains(text(),'This is the terms')]")
    except Exception as e:
        #This pattern of catching all exceptions
        result_flag = False 
    else:
        result_flag = True
    if result_flag is True:
        print("Pass: The page navigated to Terms screen")
    else:
        print("Fail: The page did Not navigate to Terms screen")
    driver.back()
    

def test_privacy():
    
    "This function used to verify the Privacy link"
    driver.find_element_by_xpath("//a[contains(text(),'Privacy')]").click()
    time.sleep(2)   
    if driver.current_url=='https://qainterview.pythonanywhere.com/privacy':
        print("Pass: The page navigated to Privacy screen")
    else:
        print("Fail: The page did Not navigate to Privacy screen")
    driver.back()
    

def test_qxf2link():
    "This functions used to verify the Qxf2 link"
    driver.find_element_by_xpath("//a[contains(text(),'Qxf2')]").click()
    
    expected_title="Qxf2 Services: Outsourced Software QA for startups"
    actual_title=driver.title
    if expected_title==actual_title:
        print("Successufully navigated to Qxf2 Home Page")
    else:
        print("Failed to navigate to Qxf2 Home Page")

if __name__=='__main__':
    # This calling function launches browser and navigates to the required web page
    setUp()

    # This calling function tests and verifies the functionality of the factorial 
    test_factorial_function()
    
    # This calling function verifies the Terms link
    test_terms()
    
    # This calling function verifies the Privacy link
    test_privacy()
    
    # This calling function verifies the Qxf2 link
    test_qxf2link()
    
    # This calling function will close the browser
    tearDown()
