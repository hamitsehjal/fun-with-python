from pathlib import Path

path = Path('pi_million_digits.txt')
contents=path.read_text()
lines = contents.splitlines() # to turn big string of contents into list of lines
pi_str=''
for line in lines:
    pi_str+=line.lstrip()

birthday=input("Pleasee enter your birthday in this format: (mmddyy):\t")
if birthday in pi_str:
    print(f"Congrats, your birthday does appears in the PI String {birthday}")
else:
    print(f"Oh no, your birthday doesn't appear")
