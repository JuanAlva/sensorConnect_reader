#import pandas as pd
#import matplotlib as plt

filename = 'SensorConnectData.csv'
#csv_file = "SensorConnectData.csv"

def get_header():
    header_flag = 0
    header_table = []
    header = []
    with open(filename, 'r') as file:
        for line in file:
            #print(line.strip())
            line = line.strip()
            if line == "Channel,Type,SampleRate,Equation,Coefficients,Unit,UnitSymbol,WhereApplied,WhenApplied":
                header_flag = 1
                continue

            if line == "":
                header_flag = 0

            if header_flag == 1:
                print(line)
                header_table.append(line)
    # automatically close when end up block line

    #print(header_table)
    
    for i in header_table:
        #print(i)
        raw = i.split(":")
        if "," in raw[1]:
            raw_clean = raw[1].split(",")
            print(raw_clean[0])
            header.append(raw_clean[0])
        else:
            valid = raw[2].split(",")
            print(raw[1],":",valid[1])
            header.append(valid[1])
    print(header)
    
get_header()
#df = pd.read_csv(csv_file, sep=',', header=1)