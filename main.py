import sqlite3
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
from dateutil import parser
from collections import Counter
import openpyxl
# import ui
dbPath = "newdb.db"


def createDB(csvPath):
    df = pd.read_csv(csvPath)
    con = sqlite3.connect("newdb.db")
    df.to_sql("fines", con)
    con.close()
    global dbPath 
    dbPath = "newdb.db"
    connectToDB(dbPath)

def analysis1():
    # Establish a connection to the database
    c = connectToDB(dbPath)
    
    # Write up SQL command
    sql_command = """
        SELECT *
        FROM fines
        WHERE OFFENCE_DESC LIKE '%camera%' OR OFFENCE_DESC LIKE '%radar%';
    """
    
    # Execute the SQL command
    c.execute(sql_command)
    
    # Fetch the results of the query and store in variable
    result = c.fetchall()
def analysis2(code):
    c = connectToDB(dbPath)
    sqlString = "SELECT OFFENCE_FINYEAR, count(*) as counter from fines WHERE OFFENCE_CODE = {code:.0f} GROUP by OFFENCE_FINYEAR"
    formattedSqlString = sqlString.format(code = code)
    c.execute(formattedSqlString)
    x = c.fetchall()
    datalength = len(x)
    # checking length on the result of the SQL query
    # returning an error msg if the length of x was 0
    if datalength == 0:
        print("Not valid code")
        errorMsg = "Did not find any codes with that value"
        return errorMsg
    data = dict(x)
    keys = list(data.keys())
    values = list(data.values())
    
    fixedkeys = list(map(str, keys))
    
    
    fig = plt.figure(figsize = (10, 5))
    plt.bar(fixedkeys, values, color='maroon', width=0.4)
            
    plt.xlabel("Financial Years")
    plt.ylabel("Occurences")
    plt.title("Amount of times each code occurs")
            
    plt.show()

        
def analysis3(startDate, endDate):
    i = 0

    # Establish a connection to the database
    c = connectToDB(dbPath)
    
    # Write up SQL command
    sql_command = """
        SELECT *
        FROM fines
        WHERE OFFENCE_DESC LIKE '%camera%' OR OFFENCE_DESC LIKE '%radar%';
    """
    
    # Execute the SQL command
    c.execute(sql_command)
    
    # Fetch the results of the query and store in variable
    result = c.fetchall()
    
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
    

def analysis4(option):
    if option == "trend":    
        a4Trend()
    if option == "codes":
        a4Codes()
    if option == "schoolzonedata":
        a4School()
    if option == "legislation":
        a4Legislation()
        
            
   
def analysis5():
    c = connectToDB(dbPath)
    #fetching distinct financial YEARS from db
    c.execute("SELECT DISTINCT(OFFENCE_FINYEAR) FROM fines")
    years = c.fetchall()
    print(years)
    #fetching count of rows with same OFFENCE_FINYEAR
    c.execute("SELECT count(*) as COUNT FROM fines GROUP BY OFFENCE_FINYEAR")
    count = c.fetchall()
    print(count)
    plt.plot(count, years)


def connectToDB(dbPath):
    print(dbPath)
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    return c

def a4Trend():
    c = connectToDB(dbPath)
    # SQL executions and converting to numpy arrays
    c.execute("SELECT DISTINCT(OFFENCE_FINYEAR) FROM fines")
    years2 = c.fetchall()
    y2 = np.array(years2)
    c.execute("SELECT count(*) as Counter from fines WHERE MOBILE_PHONE_IND ='Y' GROUP by OFFENCE_FINYEAR ORDER by OFFENCE_FINYEAR")
    trenddata2 = c.fetchall()
    td2 = np.array(trenddata2)
    # converting years data into a readable list
    y4 = list(set(y2.flat))
    # sorting y4 so it matches the data from the database
    y5 = y4.sort()
    # plotting and showing graph
    plt.plot(y4, td2)
    plt.show()
            
def a4Codes():
    c = connectToDB(dbPath)
    c.execute("SELECT OFFENCE_CODE, count(*) as Counter from fines WHERE MOBILE_PHONE_IND ='Y' GROUP by OFFENCE_CODE ORDER by OFFENCE_CODE")
    x = c.fetchall()        
    data = dict(x)
    keys = list(data.keys())
    values = list(data.values())
    
    fixedkeys = list(map(str, keys))
    
    fig = plt.figure(figsize = (10, 5))
    plt.bar(fixedkeys, values, color='maroon', width=0.4)
    
    plt.xlabel("Codes")
    plt.ylabel("Occurences")
    plt.title("Amount of times each mobile phone offence code occurs")
    
    plt.show()
    
def a4School():
    c = connectToDB(dbPath)
    c.execute("SELECT OFFENCE_CODE, count(*) as Counter from fines WHERE MOBILE_PHONE_IND ='Y' AND SCHOOL_ZONE_IND ='Y' GROUP by OFFENCE_CODE ORDER by OFFENCE_CODE")
    x = c.fetchall()
    data = dict(x)
    keys = list(data.keys())
    values = list(data.values())
    
    fixedkeys = list(map(str, keys))
    
    fig = plt.figure(figsize = (10, 5))
    
    plt.bar(fixedkeys, values, color='maroon', width=0.4)
    
    plt.xlabel("Codes")
    plt.ylabel("Occurences")
    plt.title("Amount of times each code also occured in school zone")
    
    plt.show()
            
def a4Legislation():
    c = connectToDB(dbPath)
    c.execute("SELECT LEGISLATION, count(*) as legislationCount from fines WHERE MOBILE_PHONE_IND = 'Y' GROUP by LEGISLATION")
    x = c.fetchall()
    data = dict(x)
    keys = list(data.keys())
    values = list(data.values())
    
    fixedkeys = list(map(str, keys))
    
    fig = plt.figure(figsize = (8, 8))
    
    plt.bar(fixedkeys, values, color='maroon', width=0.2)
    
    plt.xlabel("Legislation Act")
    plt.ylabel("Occurences")
    plt.title("Which legislation was used to fine")
    
    plt.show()




