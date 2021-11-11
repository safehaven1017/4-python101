from tip_calculator import percentagePlus

def groupTipCalculator():
    total = input("Enter your bill amount: ")
    tip_percent = input("Enter what percentage you want to tip: ")
    people = int(input("How many people are in the group? "))
    final_total = percentagePlus(total, tip_percent)
    print(f"Your final total, including your tip, is ${final_total}.")
    print(f"Each person should pay ${final_total/people}")

groupTipCalculator()