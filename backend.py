import requests 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time
import sqlite3
import pandas as pd


def get_db_connection():
    return sqlite3.connect("twse_data.db")

def initialize_database():
    """Creates the stock_data table if it does not exist."""
    
    if os.path.exists("twse_data.db"):
        print("Database already exists!")
        return
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE "stock_data" (
	"證券代號"	TEXT,
	"證券名稱"	TEXT,
	"成交股數"	INTEGER,
	"成交筆數"	INTEGER,
	"成交金額"	INTEGER,
	"開盤價"	NUMERIC,
	"最高價"	NUMERIC,
	"最低價"	NUMERIC,
	"收盤價"	NUMERIC,
	"漲跌(+/-)"	TEXT,
	"漲跌價差"	NUMERIC,
	"最後揭示買價"	NUMERIC,
	"最後揭示買量"	REAL,
	"最後揭示賣價"	NUMERIC,
	"最後揭示賣量"	NUMERIC,
	"本益比"	NUMERIC,
	"交易日期"	TEXT)
    """)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

initialize_database()

