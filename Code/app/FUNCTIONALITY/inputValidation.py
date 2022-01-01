import re


# function to validate the inputs from the signup page
def signupVal(name, email, phone, password):

    # re for checking if the name is valid or not
    nameRe = re.compile(r'([a-z A-Z]{1,})(\s[a-z A-Z]{1,})*')

    # re for checking if the email is valid or not
    emailRe = re.compile(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # re for checking if the phone no. is valid or not
    phoneRe = re.compile(
        r'((\+*)((0[ -]*)*|((91 )*))((\d{12})+|(\d{10})+))|\d{5}([- ]*)\d{6}')

    # re for checking if the password is valid or not
    passwordRe = re.compile(r'.{8,20}')

    # checking if the name doesnt contain numbers and is valid
    if len(nameRe.findall(name.strip())) >= 1 and name.isdecimal() != True:
        print(name.isdecimal())
        print('Success')
    else:
        print(name.isnum())
        print(len(nameRe.findall(name.strip())))
        print('Invalid Name!!!')
    print(nameRe.findall(name.strip()))

    # checking if the email is valid
    if len(emailRe.findall(email)) >= 1:
        print('Success')
    else:
        print('Invalid Email!!!')

    # checking if the phone no. valid
    if len(phoneRe.findall(phone)) >= 1:
        print('Success')
    else:
        print('Invalid Phone!!!')

    # checking if the password is valid
    if len(passwordRe.findall(password)) >= 1:
        print('Success')
    else:
        print('Invalid Password!!!')


signupVal('Adithya K Shetty', '4s019cc@sjec.ac.in',
          '3242432422', 'asdfl213_$#22b ?')


def toaddrrValid(toaddress):  # function tto validate the input from send email page

    # re to check if the to address is valid or not
    emailRe = re.compile(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # checking if the to address is valid or not
    if len(emailRe.findall(toaddress)) >= 1:
        print('Success')
    else:
        print('Invalid Email!!!')


def toaddrrValid(toaddress):  # function tto validate the input from send email page

    # re to check if the to address is valid or not
    emailRe = re.compile(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # checking if the to address is valid or not
    if len(emailRe.findall(toaddress)) >= 1:
        print('Success')
    else:
        print('Invalid Email!!!')


toaddrrValid('4s019cc@sjec.ac.in')


# input validation for login
def loginVal(name, password):
    nameRe = re.compile(r'([a-z A-Z]{1,})(\s[a-z A-Z]{1,})*')
    passwordRe = re.compile(r'.{8,20}')
    loginCounter = 0
    if len(nameRe.findall(name.strip())) >= 1 and name.isdecimal() != True:
        loginCounter = loginCounter + 1
    else:
        return False

    if len(passwordRe.findall(password)) >= 1:
        loginCounter = loginCounter + 1
    else:
        return False
    if loginCounter == 2:
        return True

# input validation for scrappy


def scrappyVal(product_name):
    product_name = product_name.strip()
    productRe = re.compile(r'[A-Za-z0-9-]')
    productNameList = productRe.findall(product_name)
    numCounter = 0
    for name in productNameList:
        if name.isdecimal() == True:
            numCounter = numCounter + 1
        else:
            continue
    if numCounter == len(productNameList):
        return False
    else:
        return True


#scrappyVal("inch tv 20")
#loginVal('Adithya K Shetty', 'avigay4')
