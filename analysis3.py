# Import the sqlite3 modules
import sqlite3
from datetime import datetime

i = 0

# Establish a connection to the database
connection = sqlite3.connect("db.db")
cursor = connection.cursor()

# Write up SQL command
sql_command = """
    SELECT *
    FROM data
    WHERE OFFENCE_DESC LIKE '%camera%' OR OFFENCE_DESC LIKE '%radar%';
"""

# Execute the SQL command
cursor.execute(sql_command)

# Fetch the results of the query and store in variable
result = cursor.fetchall()

# Raw input (will be replaced with the input box)
rawStart = input("Input start period: ")
rawEnd = input("Input end period: ")

# Split in start and end periods
splitStart = rawStart.split('-')
splitEnd = rawEnd.split('-')

# Get period 1 (1st year of start period) & period 2 (2nd year of end period)
period1 = int(splitStart[0])
period2 = int(splitEnd[1])

print(period1, period2)

# For each record
for r in result:

    #
    split_result_period = r[1].split('-')

    result_period1 = int(split_result_period[0])
    result_period2 = int(split_result_period[1])

    if result_period1 >= period1 and result_period2 <= period2:
        print(r)

