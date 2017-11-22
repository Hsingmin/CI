
# optimizationtest.py

import optimization

domain = [(0,9)]*(len(optimization.people)*2)

s = optimization.hillclimb(domain, optimization.schedulecost)

print('hillclimb algorithm -- schedulecost : ' )
print(optimization.schedulecost(s))

optimization.printschedule(s)




























