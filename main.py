import os
from tqdm import tqdm
from colorama import init
from colorama import Fore

init(autoreset=True)

def combo_finder():
    tempList = []
    countFiles = 0
    directory = 'data'
    files = os.listdir(directory)
    result1 = open('result/Full.txt', 'w')
    result2 = open('result/UrlLoginPassword.txt', 'w')
    result3 = open('result/LoginPassword.txt', 'w')
    result4 = open('result/MailPassword.txt', 'w')

    for i in tqdm(files):
        try:
            pwdFile = open(f'data/{files[countFiles]}/Passwords.txt', encoding='utf-8').read().split('\n')
            for line in pwdFile:
                try:
                    if 'URL' in line or 'HOST' in line or 'Link' in line or 'Site' in line:
                        url = line.split('//')[1].strip()
                    if 'Username:' in line or 'LOGIN' in line or 'USER' in line or 'Login' in line:
                        login = line.split(':')[1].strip()
                    if 'Password:' in line or 'PASSWORD' in line or 'PASS' in line:
                        password = line.split(':')[1].strip()
                        result1.write(f'{login}:{password}\n')
                        tempList.append(f'{login}:{password}\n')
                        result2.write(f'{url}:{login}:{password}\n')
                        result1.flush()
                        result2.flush()


                        del url
                        del login
                        del password

                except NameError: continue
                except UnicodeEncodeError: continue
                except IndexError: continue
            countFiles += 1
        except FileNotFoundError:
            countFiles += 1
            continue
    print(f'Collected unique rows: {len(set(tempList))}')
    result1.close()
    result2.close()

    # Sort data.
    for account in set(tempList):
        if '@' in account:
            result4.write(f'{account}')
            result4.flush()
        else:
            result3.write(f'{account}')
            result3.flush()
    del tempList[:]
    result3.close()
    result4.close()

    # Clean first file.
    fileClean = open('result/Full.txt').readlines()
    open('result/Full_cleaned.txt', 'w').writelines(set(fileClean))
    print(Fore.LIGHTGREEN_EX + 'Done! The results are saved in the "result" folder.')
    input('Press "Enter" for quit..')


if __name__ == '__main__':
    print('-------------------------------------------------------------------------------------------')
    print(Fore.LIGHTRED_EX + '██████╗░░█████╗░░██████╗███████╗' + Fore.LIGHTMAGENTA_EX + '  ░█████╗░██████╗░███████╗░█████╗░████████╗░█████╗░██████╗░')
    print(Fore.LIGHTRED_EX + '██╔══██╗██╔══██╗██╔════╝██╔════╝' + Fore.LIGHTMAGENTA_EX + '  ██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗')
    print(Fore.LIGHTRED_EX + '██████╦╝███████║╚█████╗░█████╗░░' + Fore.LIGHTMAGENTA_EX + '  ██║░░╚═╝██████╔╝█████╗░░███████║░░░██║░░░██║░░██║██████╔╝')
    print(Fore.LIGHTRED_EX + '██╔══██╗██╔══██║░╚═══██╗██╔══╝░░' + Fore.LIGHTMAGENTA_EX + '  ██║░░██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░██║░░██║██╔══██╗')
    print(Fore.LIGHTRED_EX + '██████╦╝██║░░██║██████╔╝███████╗' + Fore.LIGHTMAGENTA_EX + '  ╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║')
    print(Fore.LIGHTRED_EX + '╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝' + Fore.LIGHTMAGENTA_EX + '  ░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝')
    print('----------------------------------------------------------------------->DECODED BY przxxx<---')

    input('\nPress "Enter" for start..')
    print(Fore.LIGHTGREEN_EX + '[OK] Processing in progress..\n')
    combo_finder()