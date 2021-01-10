def sort_by_length(lines):
    for line in lines:
        splited_line = line.split(',')
        add_to_mask(splited_line[0])
        
def add_to_mask(line):
    lenght = len(line.strip())/2
    if lenght == 8:
        with open("corp_8_freq.hcmask", "a") as myfile:
            myfile.write(line+'\n')
    elif lenght == 9:
        with open("corp_9_freq.hcmask", "a") as myfile:
            myfile.write(line+'\n')
    elif lenght == 10:
        with open("corp_10_freq.hcmask", "a") as myfile:
            myfile.write(line+'\n')
    elif lenght == 11:
        with open("corp_11_freq.hcmask", "a") as myfile:
            myfile.write(line+'\n')
    elif lenght == 12:
        with open("corp_12_freq.hcmask", "a") as myfile:
            myfile.write(line+'\n')
    elif lenght == 13:
        with open("corp_13_freq.hcmask", "a") as myfile:
            myfile.write(line+'\n')
    elif lenght == 14:
        with open("corp_14_freq.hcmask", "a") as myfile:
            myfile.write(line+'\n')
    else:
        with open("error_file.txt", "a") as myfile:
            myfile.write(line+'\n')

# using "with statement" with open() function
with open('corp_8-14.statsgen', "r") as file_object:
    # read file content
    lines = file_object.readlines()
    sort_by_length(lines)

print("Done")
