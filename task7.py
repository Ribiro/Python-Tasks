# Write that prompts the user to input student marks. 
# The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40

score = float(input("Enter Student Score: "))

if (score >= 0) and (score <= 100):
    if score > 79:
        print("Grade A")
    elif (score >= 60) and (score <= 79):
        print("Grade B")
    elif (score >= 50) and (score <= 59):
        print("Grade C")
    elif (score >= 40) and (score <= 49):
        print("Grade D")
    else:
        print("Grade E")
else:
    print("Score/Marks out of range!")