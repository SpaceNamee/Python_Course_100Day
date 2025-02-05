from prettytable import PrettyTable, from_csv
fp = open("my_csv.csv", "r")
pt = from_csv(fp)

print(pt)

table = PrettyTable()
print(table)

table.add_column("Name", ["Marianna", "Olga", "Ostap", "Oleksandr"])
print(table)

fp.close()

x = table.get_string( )
print(x)