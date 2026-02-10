import pandas as pd
#import matplotlib as plt
import csv

file_path = 'SensorConnectData3.csv'
#csv_file = "SensorConnectData.csv"

def get_header():
    header_flag = 0
    header_table = []
    header = ["timestamp"]
    raw_header_number = 0
    with open(file_path, 'r') as file:
        it = -4
        for line in file:
            it += 1

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

            if  line == "DATA_START":
                raw_header_number = it
            
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
            valid_concat = raw[1],":",valid[1]
            separator = ""
            valid_concat = separator.join(valid_concat)
            # valid_concat = valid_concat.replace(" ","")
            header.append(valid_concat)
    # print(header)
    return header, raw_header_number

#print(get_header())

def csv_cleaner():
    header_list, raw_header_number = get_header()
    df = pd.read_csv(file_path, sep=',', header=raw_header_number, names=header_list)
    print(df)

    output_file = "output.csv"

    # 3. Open the file in write mode ('w') and use the csv.writer
    try:
        # 'newline=""' is important when writing with the csv module
        with open(output_file, mode='w', newline='') as file:
            writer = csv.writer(file)

            # 4. Write the data to the file
            # To write all data at once:
            writer.writerows(df)
            
            # Alternatively, you can write row by row:
            # writer.writerow(data_to_write[0])
            # writer.writerow(data_to_write[1])
            # ...

        print(f"Successfully created and saved data to {file_path}")
    
    except:
        print("create csv file failed")

# with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
#     # Create a reader object
#         print(csvfile)
#     # csv_reader = pd.read_csv(csvfile, delimiter=',')
#     # print(csv_reader)

csv_cleaner()