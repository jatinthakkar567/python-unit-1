# Visitor IDs for two days
day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}

# 1. Visitors who visited both days
both_days = day1.intersection(day2)

# 2. Visitors who visited only one of the days
only_one_day = day1.symmetric_difference(day2)

# 3. Total unique visitors across both days
total_unique = day1.union(day2)

# Display results
print("Visitors who visited both days:", both_days)
print("Visitors who visited only one day:", only_one_day)
print("Total unique visitors:", total_unique)
