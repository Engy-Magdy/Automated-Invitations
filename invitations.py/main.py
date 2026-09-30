with open("./Names/invited_names.txt","r") as filename:
    names=filename.readlines()
with open("./input/Letters/starting_letter.txt","r") as fileletters:
   letter=fileletters.read()
for name in names:
   update_letter=letter.replace("{name}",name.strip()) 
   final_letter=update_letter.replace("{signature}","Cairo University")
   with open (f"./output/Ready_to_send/send_to_{name.strip("\n")}.txt","w") as filesend:
     filesend.write(final_letter)
    
