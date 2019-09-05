""" Clipboard_Storer.

A simple python script that records all items to the clipboard and stores as text file.

"""

__author__ = 'Anthony T Nguyen'
__version__ = '---'
__date__ = '05.09.2019'

import win32clipboard
import time

def clipboard_validation(file):
    clipboard = win32clipboard
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardText('')
    clipboard.CloseClipboard()
    current_value = ('')
    while True:
        clipboard.OpenClipboard()
        clipboard_value = clipboard.GetClipboardData()
        clipboard.CloseClipboard()
        try:
            if (clipboard_value != current_value):
                current_value = clipboard_value
                print("[+] Successful Copy")
                file.write(current_value)
            time.sleep(0.1)
        except Exception as errorMsg:
            print('[-] Exact error message: ' + str(errorMsg))

def main():
    """
    Begin
    """
    file = open("clipboardlog.txt", "w")
    clipboard_validation(file)

if __name__ == '__main__':
    main()
