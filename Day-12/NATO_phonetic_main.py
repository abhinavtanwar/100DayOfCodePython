import pandas

filePath = "100DayOfCodePython\Day-12\data.csv"
data = pandas.read_csv(filePath)
flag = 0
while flag == 0:
    name = input("Enter your string: ").upper()
    # print(data)
    letter_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    # print(letter_dict)
    try:
        out_list = [letter_dict[letter] for letter in name]
    except KeyError:
        print("Enter alphabets only, other characters re not allowed")
        continue
    else:    
        print(out_list)
        flag = 1
    
