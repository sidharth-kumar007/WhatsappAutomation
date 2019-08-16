from selenium import webdriver

Driver = webdriver.Chrome()  # To open Firefox through webdriver
Driver.get('https://web.whatsapp.com')  # Use the driver to get to the URL


Name = input('Enter the Name : ')  # The Name of the Contact(to be searched)

Message = input('Enter the Message : ')  # The Message to be sent

Count = int(input('Count : '))  # Number of times to be sent

input('Start')  # To wait for Scanning for delaying , so that we have to press enter to continue the program

ContactElement = Driver.find_element_by_xpath('//span[@title = "{}"]'.format(Name))  # To get to the Contact Element

ContactElement.click()  # To click on that Contact

MessageBoxElement = Driver.find_element_by_xpath(
    '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')  # To get to the Message Box Element

for i in range(Count):  # Loop

    MessageBoxElement.send_keys(Message)  # To send the Message to the Message Box

    SendButtonElement = Driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[3]/button/span')  # To get to the Send Button Element

    SendButtonElement.click()  # To Click on the Send Button

