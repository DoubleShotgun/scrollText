from scrollText import scrollText 
from time import time as getTime

print("Ctrl-C to Exit")

# scrollText(text,step,maxCharacters)
st = scrollText("/home/Doubles/Project/Python/scrollText/example.py",2,24)
time = getTime()+0.5

while(1):
  if time<=getTime():
    time = getTime()+0.5
    print(st,end="") # Each time you print a scrollText, 
                     # The scrollText scrolls by how many steps you have given it    
                     
    print(str("\r"),end="") # Return the cursor to the first row
