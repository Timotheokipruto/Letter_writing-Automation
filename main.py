#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Letters/starting_letter.txt") as starting_letter_file:
    template = starting_letter_file.read()

with open("./Input/Names/invited_names.txt") as invited_names_file:
    names_file = invited_names_file.readlines()

    for name in names_file:
        stripped_name = name.strip()
        with open(f"letter_for_{stripped_name}.txt",mode="w") as letters:
            new_letter=template.replace(PLACEHOLDER,stripped_name)
            letters.write(new_letter)


