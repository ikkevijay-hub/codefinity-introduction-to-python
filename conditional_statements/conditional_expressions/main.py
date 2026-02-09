# Input variables
product_type = "Vegetables"
day_of_week = "Monday"

if (product_type == "Fruits") and (day_of_week == "Monday"):
    print("Fruits discount!") 
elif (product_type == "Vegetables") and (day_of_week == "Tuesday"):
    print("Vegetables discount!")
else:
    print ("No discount.")
#90+ → Grade A
#75–89 → Grade B
#60–74 → Grade C
#40–59 → Grade D
#Below 40 → Fail

Marks_scored = "39%"

if (Marks_scored >= "90%"):
    print("Grade A!")
elif (Marks_scored <= "89%") and (Marks_scored >= "75%"):
    print("Grade B!")
elif (Marks_scored <= "74%") and (Marks_scored >= "60%"):
    print("Grade C!")
elif (Marks_scored <= "59%") and (Marks_scored >= "40%"):
    print("Grade D!")
else:
    print ("Fail")