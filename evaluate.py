import csv
from sklearn import metrics
from sklearn.metrics import classification_report
with open('out_matrix', 'r') as csvfile:
	mat = csv.reader(csvfile, delimiter=',', quotechar='|')
	listscore = list(mat)
with open('./CensusIncome/CencusIncome.test.txt', 'r') as csvfile:
	mat2 = csv.reader(csvfile, delimiter=' ', quotechar='|')
	listclass = list(mat2)
true = []
ans = []
hit = []
for tup in listclass:
	if (len(tup) > 1):
		if tup[len(tup)-1].find(">"):
			true.append(0)
		elif tup[len(tup)-1].find("<"):
			true.append(1)

for tup in listscore:
	if (len(tup) > 1):
		if (float(tup[0]) >= float(tup[1])):
			ans.append(0)
		else:
			ans.append(1)

target_names = ['class 1', 'class 2']
print(classification_report(true, ans, target_names=target_names))
print("Homogenity: ")
print(metrics.homogeneity_score(true, ans))
print("Completeness: ")
print(metrics.completeness_score(true, ans))
print("V-Measure: ")
print(metrics.v_measure_score(true, ans))
c1m = 0
c2m = 0
c1l = 0
c2l = 0
for tru, an in zip(true,ans):
	if tru == 0 and an == 0:
		c1m+=1
	if tru == 0 and an == 1:
		c2m+=1
	if tru == 1 and an == 0:
		c1l+=1
	if tru == 1 and an == 1:
		c2l+=1

print("Class 1, >50k : " + str(c1m))
print("Class 2, >50k : " + str(c2m))
print("Class 1, <=50k : " + str(c1l))
print("Class 2, <=50k : " + str(c2l))
if (c1l+c2m)/(c1m+c2m+c1l+c2l) > 0.5:
	print("Accuracy : " + str((c1l+c2m)/(c1m+c2m+c1l+c2l)))
else:
	print("Accuracy : " + str((c1m+c2l)/(c1m+c2m+c1l+c2l)))
