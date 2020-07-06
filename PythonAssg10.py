age = input("Are you a ciggarette addict older than 75 years old ?(Y/N): ").upper().strip() == "Y"

chronic = input("Do you have severe chronic disease ?(Y/N): ").upper().strip() == "Y"

immune = input("Is your immune system too weak ?(Y/N): ").upper().strip() == "Y"

risk = age or chronic or immune

if risk :
    print("You are in risky group.")
else: 
    print("You are not in risky group.")