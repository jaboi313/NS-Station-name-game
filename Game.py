import csv
import pandas as pd


def read_file(file_path:str = None) -> list:
    with open(file_path, 'r') as infile:
        info = csv.reader(infile, delimiter= ',')
    return info



def search(country:str = None)-> str:
    read_file('Stations_info.csv')
    row = 0
    if country == None:
