import requests

logo = ("""
 __        ___  __  
/__`  /\  |__  |  \ 
.__/ /~~\ |___ |__/ 
""")
print(logo)

number = input("Enter Target Number: ")
url = "https://cpp.bka.sh/external-services/referral/report/otp/request"
data = {"referrerWallet": number}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("OTP request successful!")
    print("Response:", response.json())
else:
    print("Error requesting OTP. Status code:", response.status_code)
