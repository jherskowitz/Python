from sys import argv
# execute program by giving it the script name and the filename you want it to read
script, filename = argv
# uses open command
txt = open (filename)
# confirm the filename
print "Here's your file %r:" % filename
# print the text in the document
print txt.read()

# prompt the user for the filename again (it could be a different file if desired)
print "I'll also ask you to type it again:"
# prompt user
file_again = raw_input ("> ")

# opens the file 
txt_again = open (file_again)
# prints contents of file
print txt_again.read()
