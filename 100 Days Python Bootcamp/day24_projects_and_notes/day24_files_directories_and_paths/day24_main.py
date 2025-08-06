from logging import debug


with open("./Input/Names/names.txt") as names:
    guest_names = names.readlines()
    for i in range(len(guest_names)-1):
        guest_names[i] = guest_names[i].strip("\n")

debug(guest_names)
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()
    print(letter_text)
    debug("After getting original letter")
    for name in guest_names:
        debug("Before creating file name")
        if " " in name:
            file_name= name.replace(" ","_").lower()
        else:
            file_name = name.lower()
        debug("After creating file name")
        invite_text = letter_text.replace('[name]',f'{name}')
        debug("Before creating")

        with open(f"./Output/ReadyToSend/letter_for_{file_name}.txt",mode="w") as invite_letter:
            invite_letter.write(invite_text)
