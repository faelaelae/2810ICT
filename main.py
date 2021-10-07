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

def analysis1(dbPath):
   pass
def analysis2(code):
    c = connectToDB(dbPath)
    print(c)
    sqlString = "SELECT OFFENCE_FINYEAR, count(*) as counter from fines WHERE OFFENCE_CODE = {code:.0f} GROUP by OFFENCE_FINYEAR"
    formattedSqlString = sqlString.format(code = code)
    print(formattedSqlString)
    c.execute(formattedSqlString)
    x = c.fetchall()
    datalength = len(x)
    print(len(x))
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

        
def analysis3(dbPath, code):
    pass


def analysis4(option):
    c = connectToDB(dbPath)
    if option == "trend":    
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
    if option == "codes":
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
    if option == "schoolzonedata":
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
    if option == "legislation":
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

analysis2(6644)





#leftover 
#analysis 4 backup
# c.execute("SELECT DISTINCT(OFFENCE_FINYEAR) FROM fines ")
#     years = c.fetchall()
#     c.execute("SELECT count(OFFENCE_FINYEAR) as FIN_YEAR FROM fines WHERE MOBILE_PHONE_IND == 'Y' GROUP BY OFFENCE_FINYEAR")
#     yearlytrend = c.fetchall()
#     c.execute("SELECT OFFENCE_FINYEAR, OFFENCE_CODE, count(*) FROM fines WHERE MOBILE_PHONE_IND == 'Y' GROUP BY OFFENCE_FINYEAR, OFFENCE_CODE")
#     query = "SELECT OFFENCE_FINYEAR, OFFENCE_CODE, count(*) as COUNT FROM fines WHERE MOBILE_PHONE_IND == 'Y' GROUP BY OFFENCE_FINYEAR, OFFENCE_CODE"
#df = pd.read_sql(trenddata, conn)
    #plt.plot(years2, trenddata2)
    #df = pd.read_sql(query, conn)
    #plot=df.plot.bar(x='OFFENCE_FINYEAR', y='COUNT')
    #codetrend = c.fetchall()



# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# #Analysing the cases caused by mobile phone usage - ie: trend over time, offence code, and so on.
# import openpyxl
# import datetime
# import matplotlib.pyplot as plt
# import numpy as np
# from dateutil import parser
# from collections import Counter

# path = "testdata.xlsx"

# def open_Workbook(path):
#     wb = openpyxl.load_workbook(path)
#     return wb

# wb = open_Workbook(path)

# sheet = wb['data']

# startDate = datetime.datetime(2012,1,1)
# endDate = datetime.datetime(2013,12,12)


# path = "testdata.xlsx"

#     def open_Workbook(path):
#         wb = openpyxl.load_workbook(path)
#         return wb

#     wb = open_Workbook(path)

#     sheet = wb['data']

#     startDate = datetime.datetime(2012,1,1)
#     endDate = datetime.datetime(2013,12,12)

#     def buildData(startDate, endDate, sheet):
#         counter = 2
#         data = []
#         maxrows = sheet.max_row
#         maxcolumn = sheet.max_column
#         print(startDate, endDate)
#         for row in sheet.iter_rows(min_row=1, max_col=maxcolumn,max_row=maxrows):
#             counter += 1
#             date = sheet.cell(row=counter,column=2).value
#             if date is not None:
#                 #date = parser.parse(d)
#                 code = sheet.cell(row=counter,column=3).value
#                 print(code)
#                 if date >= startDate and date <= endDate:
#                         data.append(code)
#         print(data)
#         return data
            
#     listData = buildData(startDate, endDate, sheet)
#     #def translateData(listData):
#     #    countedList = Counter(listData)
#     #    return countedList

#     data = Counter(listData)

#     def drawGraph(data):
#         print(data.keys())
#         print(data.values())
#         index = np.arange(len(data.keys()))
#         width = 0.2
#         plt.bar(index, data.values(), width)
#         plt.xticks(index + width * 0.5, data.keys())
#         plt.show()

#     drawGraph(data)