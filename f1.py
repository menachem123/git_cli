

def load_csv_function (csv):
    External_list = []
    with open (csv,"r",encoding="utf-8") as file :
        for line in file:
            External_list.append(list(line.strip().split(",")))


    return External_list

