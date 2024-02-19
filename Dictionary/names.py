names={'hamit':5,'mohit':10,'everlast':11}
print(f"Names are: {names}")
print(f"Value for KEY-HAMIT is: {names['hamit']}")
print(f"Value for KEY-paper(doesn't exist) is {names.get('paper','No key-paper found!!')}")
