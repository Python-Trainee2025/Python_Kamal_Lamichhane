# 5. Read a .csv file and print each row. Handle file not found and other parsing errors if needed
from ftplib import print_line
from logging import exception


def printRow(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.readlines()
            for row in content:
                print(row)

    except FileNotFoundError as e:
        print("File not found")
        print(e)
    except Exception as e:
        print(e)

printRow("SimpleCSV.csv")