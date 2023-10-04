print("Hey there I'm gonna help you to calculate the 3 months average of a budget.")
print("All I need is a few numbers.")

budget_01 = input("What is your budget for January? ")
budget_02 = input("What is your budget for February? ")
budget_03 = input("What is your budget for March? ")

budget_01 = int(budget_01)
budget_02 = int(budget_02)
budget_03 = int(budget_03)

import statistics

list = [budget_01, budget_02, budget_03]
total = sum(list)
average = round(statistics.mean(list), 2)

print(f"The average for that 3 months is {average} UDS.")
print(f"Because the sum of {budget_01} bucks from January plus {budget_02} from February and {budget_03} bucks from March is equal to {total} USD.")
print(f"If we divide the total between 3, we will have {average} as quotient/result.")