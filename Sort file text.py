# sort a file text alphabetical
user_input = raw_input("enter file name: ")
fhand = open(user_input)
data = fhand.read()                            # read file data
words = data.split()                           # convert file text to list
words.sort()                                   # sort list elements
ask_usr = raw_input("save in same file: (y) for 'yes' & (n) for 'no':  ")
if ask_usr == "y" or "yes":
    fhand = open(user_input, "w")
    for i in words:
        fhand.writelines(i)                     # write data in same file
        fhand.write("\n")                       # to insert new line
else:
    new = open("NewFile.txt", "w")              # create new file if user need to save in new file
    for i in words:
        new.writelines(i)
        new.write("\n")




