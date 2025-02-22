#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_lines = letter.readlines()

with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()

i = 0
for name in names:
    i += 1
    name = name.strip()
    modify_line = letter_lines[0].replace("[name]", name)
    with open(f"./Output/ReadyToSend/{name}.txt", mode="w") as output_letter:
        output_letter.write(modify_line)

    with open(f"./Output/ReadyToSend/{name}.txt", mode="a") as output_letter:
        for letter_line in letter_lines[1:]:
            output_letter.write(letter_line)


