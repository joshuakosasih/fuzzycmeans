import csv
with open('./CensusIncome/CencusIncome.data.txt', 'r') as csvfile:
	mat = csv.reader(csvfile, delimiter=' ', quotechar='|')
	listclass = list(mat)
more=0
less=0
for tup in listclass:
	if (len(tup) > 1):
		if tup[len(tup)-1].find(">"):
			more+=1
		elif tup[len(tup)-1].find("<"):
			less+=1
print(">50 : " + str(more))
print("<=50 : " + str(less))