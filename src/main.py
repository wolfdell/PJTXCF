import os
import sys
import platform
import argparse # TODO: Use the argparse module to check for provided arguments

# Method for cleaning the screen
def flush_screen():
    system_name = platform.system()
    executor = ''

    match system_name:
        case 'Linux' | 'Darwin':
            executor = 'clear'
        case 'Windows':
            executor = 'cls'

    os.system(executor)

# Method for printing the banner of the application
def print_banner():
    print(' /$$$$$$$   /$$$$$ /$$$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$')
    print('| $$__  $$ |__  $$|__  $$__/| $$  / $$ /$$__  $$| $$_____/')
    print('| $$  \ $$    | $$   | $$   |  $$/ $$/| $$  \__/| $$      ')
    print('| $$$$$$$/    | $$   | $$    \  $$$$/ | $$      | $$$$$   ')
    print('| $$____//$$  | $$   | $$     >$$  $$ | $$      | $$__/   ')
    print('| $$    | $$  | $$   | $$    /$$/\  $$| $$    $$| $$      ')
    print('| $$    |  $$$$$$/   | $$   | $$  \ $$|  $$$$$$/| $$      ')
    print('|__/     \______/    |__/   |__/  |__/ \______/ |__/      ')
    print('')
    print('==================== 2023 @ wolfdell =====================')

# Print the usage of the program
def print_use():
    print('\n\nIn order to convert, you need to provide some parameters.\n')
    print('-j                             - The provided format is JPG')
    print('-p                             - The provided format is PNG')
    print('-a                             - Auto detect the format')
    print('-c [chapter number]            - Number of the chapter')
    print('-v [volume number]             - Number of the volume')
    print('                                         not required')
    print('-t [translation group]         - The translation group')
    print('-m [manga name]                - The name of the manga')
    print('\nExample: ')
    print('pjtxcf -a -c 7 -v 2 -t wolfdell -m Gintama\n\n')
    
def create_name(raw):
    name = "_".join(raw.lower().split())

    create_path(name)

    print("The provided name is: ", name)

def create_path(name):

    if not os.path.exists(name):
        os.makedirs(name)
        print('[+] The path ', name, ' was created!')
        return
    
    print('[*] Using already existing path: ', name)


if __name__ == '__main__':
    flush_screen()
    print_banner()
    if len(sys.argv) == 1:
        print_use() 

    # For testing
    manga_name = input('Give me the manga name: ')
    create_name(manga_name)
