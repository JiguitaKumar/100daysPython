#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

# convert file with name into a list with the names
with open("./Input/Names/invited_names.txt") as n:
    names_list = n.read().split()
print(names_list)

# get text from starting letter
with open("./Input/Letters/starting_letter.txt") as l:
    content = l.read()
#print(content)

# create and save letters ready to send
for name in names_list:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new:
        final_content = content.replace("[name]", name)
        new.write(final_content)
