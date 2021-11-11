def percentagePlus(total, tip_percent):
    float_total = float(total)
    float_tip_percent = float(tip_percent)
    tip = float_total * float_tip_percent/100
    return round(float_total + tip, 2)

def tipCalculator():
    total = input("Enter your bill amount: ")
    tip_percent = input("Enter what percentage you want to tip: ")
    final_total = percentagePlus(total, tip_percent)
    print(f"Your final total, including your tip, is ${final_total}.")

# tipCalculator()