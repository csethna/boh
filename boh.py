import csv # name of the library is csv.py and thus the file itself cannot be named csv.py
with open('master.csv', 'rb') as master_csvfile: # using open function, open the CSV file and use attribute "as" to define as "master_csvfile" user-defined name.
    master_reader = csv.DictReader(master_csvfile, delimiter='\t') # creates variable "master_reader" defined as running csv(.= library) function on "csv file" with deliminter (the character that separates each word) as "space"
    master_inventory = {row['Item_Number']: int(row['Current_Available']) for row in master_reader if int(row['Current_Available'])} # loops through every row in the csv file

with open('copy.csv', 'rb') as copy_csvfile: # using open function, open the CSV file and use attribute "as" to define as "copy_csvfile" user-defined name.
    copy_reader = csv.DictReader(copy_csvfile, delimiter=',') # creates variable "copy_reader" defined as running csv(.= library) function on "csv file" with deliminter (the character that separates each word) as "space"
    copy_inventory = {row['Campaign_Number']: int(row['Available_Issue']) for row in copy_reader if int(row['Available_Issue'])}

for item_number in master_inventory:
    if abs(master_inventory[item_number] - copy_inventory[item_number]) > 500:
        print 'Item {} - master count: {}, copy count:{}'.format(item_number, master_inventory[item_number], copy_inventory[Campaign_Number])

# master_inventory = {}
# for row in spamreader:
#     if int(row['Current_Available']):
#         master_inventory[row['Item_Number']] = int(row['Current_Available'])



# csvfile = open('FASBOHRpt.csv', 'rb')
# spamreader = csv.DictReader(csvfile, delimiter='\t') # creates variable "spamreader" defined as running csv(.= library) function on "csv file" with deliminter (the character that separates each word) as "space"
# for row in spamreader: # loops through every row in the csv file
# print '~'.join(row)
# csvfile.close()

# filenames = ['this.file', 'that.file', ...]
# for filename in filenames:
#     with open(filename, 'rb') as csvfile:
#         reader....
