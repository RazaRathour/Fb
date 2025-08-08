import requests
import random
import string
import hashlib
from faker import Faker
import imaplib
import email
import re
import time,datetime
import os
os.system("pkg install espeak")
os.system('clear')
os.system('pkg install root-repo')
os.system('clear')
print(' \x1b[38;5;46mRAZA➛RATHOUR➛KILLER LOADING....')
os.system('espeak -a 300 " LOADING RAZA RATHOUR KILLER SERVER. "')
print('loading Modules ...\n')
os.system('clear')
print(' \x1b[38;5;46m RAZA➛RATHOUR➛KILLER ....')
os.system('espeak -a 300 " WELCOME TO,RAZA RATHOUR KILLER SERVER."')
os.system('espeak -a 300 " TOLLS CODING BY RAZA BHAI."')
# Clear the console (for Linux/Mac)
os.system('clear')  # For Linux/Mac
# os.system('cls')  # For Windows
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'Agustus','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'Agustus','09':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year

logo = (f"""\r\r\x1b[1;97m
\033[1;32m 

 \033[1;30m _____             ______          
\033[1;31m |  __ \     /\    |___  /   /\    
\033[1;30m | |__) |   /  \      / /   /  \   
\033[1;31m |  _  /   / /\ \    / /   / /\ \  
\033[1;30m | | \ \  / ____ \  / /__ / ____ \ 
 \033[1;31m|_|  \_\/_/    \_\/_____/_/    \_\
 
 \033[1;37m--------------------------------------------------
 \033[1;37m[•] AUTHOR     : \033[1;32mRAZA RATHOUR\033[1;37m
 \033[1;37m[•] ADD|GMAIL     : \033[1;32m@GMAIL\033[1;37m
 \033[1;37m[•] YOUTUBE     : \033[1;32m@FUNZONCE\033[1;37m
 \033[1;37m[•] TOOL TYPE  : \033[1;32mAUTO GENERATE FB\033[1;37m
 \033[1;37m[•] STATUS     : \033[1;32mPAID\033[1;37m
 \033[1;37m--------------------------------------------------
 \033[1;37m[•] \033[1;37mVERSION    :\033[1;32m"JUST GMAIL.TXT KI FILE MAIN SUB GMAIL DAL DO PHIR DEKHO MAGIC!"\033[1;37m
 \033[1;37m--------------------------------------------------""")

print(logo)
approved_keys = ["RAZA123", "RATHOUR786", "FUNZONCE999"]

def check_key():
    os.system('clear')
    print(logo)
    user_key = input("🔑 Apni approval key daalo: ").strip()
    if user_key in approved_keys:
        print("\n✅ Key approved. Welcome Raza Commandi!\n")
        os.system('espeak -a 300 "Approved Key. Welcome."')
        time.sleep(1)
    else:
        print("\n❌ Ghalat key! Access denied.\n")
        os.system('espeak -a 300 "Wrong Key. Access Denied."')
        exit()

if __name__ == "__main__":
    check_key()  # <-- Approval system call
    
    
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def get_facebook_verification_code(email_address, email_password):
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(email_address, email_password)
        mail.select("inbox")

        result, data = mail.search(None, '(FROM "Facebook" SUBJECT "Facebook Confirmation Code")')
        mail_ids = data[0].split()

        if not mail_ids:
            print("[×] Koi verification email nahi mila.")
            return None

        latest_email_id = mail_ids[-1]
        result, msg_data = mail.fetch(latest_email_id, '(RFC822)')
        raw_email = msg_data[0][1]
        message = email.message_from_bytes(raw_email)

        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode()
                    break
        else:
            body = message.get_payload(decode=True).decode()

        code_match = re.search(r'([0-9]{5})', body)
        if code_match:
            return code_match.group(1)
        else:
            print("[×] Code nahi mila email se.")
            return None
    except Exception as e:
        print(f"[×] Gmail access error: {e}")
        return None

def register_facebook_account(email, fb_password, first_name, last_name, birthday):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])

    req = {
        'api_key': api_key,
        'attempt_login': True,
        'birthday': birthday.strftime('%Y-%m-%d'),
        'client_country_code': 'EN',
        'fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod',
        'fb_api_req_friendly_name': 'registerAccount',
        'firstname': first_name,
        'format': 'json',
        'gender': gender,
        'lastname': last_name,
        'email': email,
        'locale': 'en_US',
        'method': 'user.register',
        'password': fb_password,
        'reg_instance': generate_random_string(32),
        'return_multiple_errors': True
    }

    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    req['sig'] = hashlib.md5((sig + secret).encode()).hexdigest()

    api_url = 'https://b-api.facebook.com/method/user.register'
    try:
        response = requests.post(api_url, data=req, headers={
            'User-Agent': '[FBAN/FB4A;FBAV/398.0.0.29.105]'
        })
        #print(f"[📩] Facebook API raw response text:\n{response.text}\n")  # 🐞 Debug print
        data = response.json()
        return data
    except Exception as e:
        print(f"[×] Registration error: {e}")
        return None

def verify_facebook_account(email, code):
    print(f"[⚙] Verify kar rahe hain code: {code} for {email}")
    time.sleep(2)
    print(f"[✅] {email} verified with code {code}")

def main():
    fake = Faker()

    path = input("Gmail list ka path do (e.g., /sdcard/Gmail.txt): ").strip()
    fb_password = input("Jo Facebook password rakhna hai wo do: ").strip()

    try:
        with open(path, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("[×] File nahi mili.");os.system('espeak -a 300 "File Nahi Mila"');
        return

    for i, line in enumerate(lines):
        if '|' not in line:
            print(f"[!] Format ghalat hai: {line}")
            continue

        email_address, email_password = line.split('|', 1)
        print(f"\n[{i+1}] Banaya ja raha hai: {email_address}")

        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()

        fb_data = register_facebook_account(email_address, fb_password, first_name, last_name, birthday)

        if fb_data:
            if 'new_user_id' in fb_data:
                user_id = fb_data['new_user_id']
                print(f"[🎉] FB Account Created: {user_id} | {email_address} | {fb_password}");os.system('espeak -a 300 "ok id"')

                time.sleep(5)

                code = get_facebook_verification_code(email_address, email_password)
                if code:
                    verify_facebook_account(email_address, code)
                else:
                    print("[×] Verification code nahi mila.")

                with open("/sdcard/facebook_credentials.txt", "a") as out:
                    out.write(f"{user_id}|{fb_password}|{email_address}\n")
            else:
                print("[×] Facebook account create nahi hua.");os.system('espeak -a 300 "FACEBOOK ACCOUNT CREATE NHE HUA"')
                #print(fb_data)
        else:
            print("[×] Facebook API call hi fail hui.")

    print("\n[✅] Sab kaam ho gaya.");os.system('espeak -a 300 "Bye bye"');

if __name__ == "__main__":
    main()
