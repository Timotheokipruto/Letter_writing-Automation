PLACEHOLDER = "[name]"

with open("./starting_letter.txt") as starting_letter_file:
    template = starting_letter_file.read()

with open("./invited_names.txt") as invited_names_file:
    names_file = invited_names_file.readlines()

    for name in names_file:
        stripped_name = name.strip()
        with open(f"letter_for_{stripped_name}.txt",mode="w") as letters:
            new_letter=template.replace(PLACEHOLDER,stripped_name)
            letters.write(new_letter)


