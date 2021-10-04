# Import the sqlite3 modules
import sqlite3
from _datetime import datetime

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
rawStart = input("Input start date: ")
rawEnd = input("Input end date: ")

# Convert to datetime for comparing
start = datetime.strptime(rawStart, '%d/%m/%Y')
end = datetime.strptime(rawEnd, '%d/%m/%Y')

# For each record
for r in result:

    # Convert the record date to datetime
    date = datetime.strptime(r[2], '%d/%m/%Y')

    # If the record date is between the start and finished
    if start <= date <= end:
        print(r)
