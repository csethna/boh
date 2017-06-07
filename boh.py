import csv
with open('master.csv', 'rb') as master_csvfile:
    master_reader = csv.DictReader(master_csvfile, delimiter='\t')
    master_inventory = {row['Item_Number']: int(row['Current_Available']) for row in master_reader if int(row['Current_Available'])}

with open('copy.csv', 'rb') as copy_csvfile:
    copy_reader = csv.DictReader(copy_csvfile, delimiter=',')
    copy_inventory = {row['Campaign Number']: int(row['Available Issue']) for row in copy_reader if int(row['Available Issue'])}

for item_number in master_inventory:
    #print copy_inventory
    try:
        if abs(master_inventory[item_number] - copy_inventory[item_number]) > 500:
            print 'Item {}, master count: {}, copy count:{}'.format(item_number, master_inventory[item_number], copy_inventory[item_number])
    except KeyError, e:
    	print "Missing data for {}".format(e)
