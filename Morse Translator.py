# Python program to implement Morse Code Translator

'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

from tkinter import *
Screen = Tk()
Screen.title("Morse Code Translator")
# specify size of window.
Screen.geometry("500x150")


# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
					'C':'-.-.', 'D':'-..', 'E':'.',
					'F':'..-.', 'G':'--.', 'H':'....',
					'I':'..', 'J':'.---', 'K':'-.-',
					'L':'.-..', 'M':'--', 'N':'-.',
					'O':'---', 'P':'.--.', 'Q':'--.-',
					'R':'.-.', 'S':'...', 'T':'-',
					'U':'..-', 'V':'...-', 'W':'.--',
					'X':'-..-', 'Y':'-.--', 'Z':'--..',
					'1':'.----', '2':'..---', '3':'...--',
					'4':'....-', '5':'.....', '6':'-....',
					'7':'--...', '8':'---..', '9':'----.',
					'0':'-----', ',':'--..--', '.':'.-.-.-',
					'?':'..--..', '/':'-..-.', '-':'-....-',
					'(':'-.--.', ')':'-.--.-'}

# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':

			# Looks up the dictionary and adds the
			# corresponding morse code
			# along with a space to separate
			# morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
			# 1 space indicates different characters
			# and 2 indicates different words
            cipher += ' '

    text2.insert(END, cipher)
	#return cipher


# Function to decrypt the string
# from morse to english
def decrypt(message):

	# extra space added at the end to access the
	# last morse code
	message += ' '

	decipher = ''
	citext = ''
	for letter in message:

		# checks for space
		if (letter != ' '):

			# counter to keep track of space
			i = 0

			# storing morse code of a single character
			citext += letter

		# in case of space
		else:
			# if i = 1 that indicates a new character
			i += 1

			# if i = 2 that indicates a new word
			if i == 2 :

				# adding space to separate words
				decipher += ' '
			else:

				# accessing the keys using their values (reverse of encryption)
				decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
				.values()).index(citext)]
				citext = ''

	return decipher

# Function to clear the text
def clearText():
	text.delete("1.0", "end-1c")
	text2.delete("1.0", "end-1c")


#Frame
Label(Screen, text='Enter Morse Code').grid(row=1)
text = Text(Screen,height=3,width=20)
text.grid(row=4,column=0,padx=20)
Label(Screen, text='Result').grid(row=1,column=7)
text2 = Text(Screen,height=3,width=20)
text2.grid(row=4,column=7)

# Drop-Down Menu
# Dropdown menu options
options = [
    "Select",
	"Language Translator",
	"Morse Translator"
]
# datatype of menu text
clicked = StringVar()  
# initial menu text
clicked.set( "Select" )
# Create Dropdown menu
drop = OptionMenu( Screen , clicked , *options )
drop.grid(row=5,column=3)


#Translate Button
transButton = Button(Screen, text='Translate', width=10, command = lambda:encrypt(message=text.get("1.0", "end-1c").upper()))
transButton.grid(row=7,column=3,padx=10,pady=10)

#Clear Button
clearButton = Button(Screen, text='Clear', width=10, command = lambda:clearText())
clearButton.grid(row=8,column=3,padx=10,pady=10)


mainloop()

# Hard-coded driver function to run the program
#def main():
    #message = text.get("1.0", "end-1c")
    #result = encrypt(message.upper())
    #print (result)
    

	#message = "--. . . -.- ... -....- ..-. "
	#result = decrypt(message)
	#print (result)

# Executes the main function
#if __name__ == '__main__':
	#main()