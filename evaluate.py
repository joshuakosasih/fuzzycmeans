import csv
with open('out_matrix', 'r') as csvfile:
	mat = csv.reader(csvfile, delimiter=' ', quotechar='|')
	listscore = list(mat)
with open('./CensusIncome/CencusIncome.data.txt', 'r') as csvfile:
	mat = csv.reader(csvfile, delimiter=' ', quotechar='|')
	listclass = list(mat)
classes = []
ans = []
hit = []
for tup in listclass:
	if (len(tup) > 1):
		classes.append([tup[len(tup)-1]])
i = 0;
for tup in listscore:
	if (len(tup) > 1):
		if (tup[0] >= tup[1]):
			classes[i].append("class1")
		else:
			classes[i].append("class2")
		i+=1
print(classes)

c1m = 0
c2m = 0
c1l = 0
c2l = 0
for x in classes:
	if x[0] == ">50K" and x[1] == "class1":
		c1m+=1
	if x[0] == ">50K" and x[1] == "class2":
		c2m+=1
	if x[0] == "<=50K" and x[1] == "class1":
		c1l+=1
	if x[0] == "<=50K" and x[1] == "class2":
		c2l+=1

print("Class 1, >50k : " + str(c1m))
print("Class 2, >50k : " + str(c2m))
print("Class 1, <=50k : " + str(c1l))
print("Class 2, <=50k : " + str(c2l))
print("Accuracy : " + str((c1l+c2m)/(c1m+c2m+c1l+c2l)))