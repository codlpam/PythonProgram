def read_data(filename):
	records = []
	#with-as statement to create file read object
	with open(filename) as readfile:
		lines = readfile.readlines()
		for line in lines: #while there are more lines 
			line = line.strip()
			if len(line) == 0: #if line is empty 
				continue 	
			# cleaning list 
			str_rec = line.split(",") # removes ","
			store_id = str_rec[0].strip()
			employees = int(str_rec[1].strip()) 
			suburb_name = str_rec[2].strip()
			sale_volume = float(str_rec[3].strip()) 
			rec = [store_id, employees, suburb_name, sale_volume]
			records.append(rec)
	return records

def print_all_records(records):	 # function to print list with formatting 
	h0, h1, h2, h3, h4 = " ", "Store ID", "Employees", "Suburb", "Sales"  
	print(f"{h0*6}{h1:<20}{h2:<20}{h3:<20}{h4}") 
	print("-"*75)  
	for rec in records: # while there are more records
		num = records.index(rec) + 1 
		print(f"{num:<6}{rec[0]:<20}{rec[1]:<20}{rec[2]:<20}{rec[3]}")
	
def write_data(filename, records):
	#with-as statement to create file handle for writing data
	with open(filename, "w") as writefile: # "w" to write
		for rec in records: # for there are more records 
			str_rec = [rec[0],str(rec[1]), rec[2], str(rec[3])]
			line = ",".join(str_rec) # joins individual items with ","
			writefile.write(line + "\n")

def query_suburb_stats(records): #function to search records 
	suburb_name = input("Enter suburb name: ") 
	rec_found = False # cover negative search
	total, count = 0, 0
	for rec in records: 
		# for there are records with suburb equal to input
		if suburb_name.lower() == rec[2].lower(): 
			total += rec[3]
			count += 1 
			rec_found = True # updates if result found
	if rec_found == False: 
		# no result found , print
		print(f"No record was found for {suburb_name}")
	else: 
		# else (result was found) , print with rounding
		print(f"Total sale by {suburb_name}: ${total:.2f}")
		print(f"Average sale by {suburb_name}: ${total / count:.2f}")

def get_max_sales(records):
	max_sale = records[0][3] # max_sale = first record sales
	store = records[0] 
	for rec in records: # while there are more records 
		if rec[3] > max_sale: #if max_sales > previous max
			max_sale = rec[3]
			store = rec[0] 
	return max_sale, store # return max_sale and store
	
def count_employees(records):
	total_employees = 0 
	for rec in records: # for there are more items 
		if rec[3] > 50000: # sales > 50,000
			total_employees += rec[1] 
	return total_employees

def main():
	data = read_data("data.txt")
	print_all_records(data) 
	write_data("backup.txt",data) 
	query_suburb_stats(data) 
	sales = get_max_sales(data) 
	print(f"\nThe maximum sale volume is: ${sales[0]}")
	print(f"Store ID: {sales[1]}")
	total_employees = count_employees(data)
	print(f"\nTotal employees from stores with sales more than $50,000: {total_employees}")

main()