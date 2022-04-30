# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Hypothesis String
hypothesis = "I believe the number of vehicle crashes in NJ from 2001 to 2019 has increased by atleast 10%"

# Step 1: Get the data inside program
df = pd.read_csv("Total_NJ_Crash_Records_By_County.csv", index_col=0)

# Step 2: Create loop to make number of years dictionary with
#         appending a key but with no values
startYear = 2001
years = {}
while startYear <= 2019:
	years[startYear] = None
	startYear = startYear + 1

# Step 3: Get total sum of crashes from 2001 to 2019 for data report at the end
# 		  Also take totals from each year and put them into the dictionary
startYear = 2001
sumTotalCrashes = 0
totalCrashes = df[df.columns[21]]
for row in totalCrashes:
	years[startYear] = int(row)
	sumTotalCrashes += int(row)
	startYear = startYear + 1

# Step 4: Calculate average number of crashes from 2001 to 2019
avgCrashes = sumTotalCrashes / len(years.keys())
formatAvgCrashes = "{:.2f}".format(avgCrashes)

# Step 5: Calculate percentage change from 2001 to 2019
total2001 = years.get(int(2001))
total2019 = years.get(int(2019))
percChange = ((total2019 - total2001) / total2001) * 100
formatPercChange = "{:.2f}".format(percChange)

# Step 6: Create a txt file that shows my results and findings
outFile = open("Report.txt", "w")
print(hypothesis, file=outFile)
print("The number of crashes in 2001:", total2001, file=outFile)
print("The number of crashes in 2019:", total2019, file=outFile)
print("Percentage of crashes change from 2001 to 2019:", formatPercChange+"%", file=outFile)
print("The average number of crashes from 2001 to 2019:", formatAvgCrashes, file=outFile)
outFile.close()
