""" Clipboard_Storer.

A simple python script that records all items to the clipboard and stores as text file.

"""

__author__ = 'Anthony T Nguyen'
__version__ = '---'
__date__ = '16.07.2019'

import win32clipboard
import time

def options():
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardText('')
    win32clipboard.CloseClipboard()
    current_value = ('')
    while True:
        win32clipboard.OpenClipboard()
        clipboard_value = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        if (clipboard_value != current_value):
            current_value = clipboard_value
            print("Completed")
        time.sleep(0.1)

def main():
    """
    Begin
    """
    options()

if __name__ == '__main__':
    main()
