from playsound import playsound
import cipher
from time import sleep
long = '(LOCATION OF THIS FILE)/long.wav'
short = '(LOCATION OF THIS FILE)/short.wav'
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
morse = '*- -*** -*-* -** * **-* --* **** ** *--- -*- *-** -- -* --- *--* --*- *-* *** - **- ***- *-- -**- -*-- --** *---- **--- ***-- ****- ***** -**** --*** ---** ----* -----'
morsed = []
d = dict(zip(list(chars),morse.split()))

text = input('Enter the text to be morsed ')
hidden = cipher.encrypt(text.upper())
hidden_list = list(hidden)
for j in hidden_list:
    if j == ' ':
        morsed.append(' ')
    else:
        for k in d[j]:
            morsed.append(k)

print(morsed)
print('0.5s beep for each character of a word')
print('3s wait for beep between each word')

for i in morsed:
    if i == ' ':
        sleep(3)
    elif i == '*':
        playsound(short)
        sleep(0.5)
    elif i == '-':
        playsound(long)
        sleep(0.5)
