import sqlite3
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
from dateutil import parser
from collections import Counter
import openpyxl

def analysis():
    conn = sqlite3.connect("db.db")
    c = conn.cursor()
    #years
    c.execute("SELECT DISTINCT(OFFENCE_FINYEAR) FROM data ")
    years = c.fetchall()
    c.execute("SELECT count(OFFENCE_FINYEAR) as FIN_YEAR FROM data WHERE MOBILE_PHONE_IND == 'Y' GROUP BY OFFENCE_FINYEAR")
    yearlytrend = c.fetchall()
    c.execute("SELECT OFFENCE_FINYEAR, OFFENCE_CODE, count(*) FROM data WHERE MOBILE_PHONE_IND == 'Y' GROUP BY OFFENCE_FINYEAR, OFFENCE_CODE")
    query = "SELECT OFFENCE_FINYEAR, OFFENCE_CODE, count(*) as COUNT FROM data WHERE MOBILE_PHONE_IND == 'Y' GROUP BY OFFENCE_FINYEAR, OFFENCE_CODE"
    df = pd.read_sql(query, conn)
    # plot=df.plot.bar(x='OFFENCE_FINYEAR', y='COUNT')
    codetrend = c.fetchall()
    return df


analysis()
