import csv
import os
csvpath=os.path.join("budget_data.csv")
csvpathwrite=os.path.join("budget_datarite.txt")
prolosscsv=[]
totalbudget=0
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    listcsv=list(csvreader)


for x in range(len(listcsv)):
    prolosscsv.append(['',0,0])
#assign values to fist element to prolosscsv

prolosscsv[0][0] = listcsv[0][0]
prolosscsv[0][1] = listcsv[0][1]
prolosscsv[0][2] = 0
budchange=0
rownumber=0
for row in range(1,len(listcsv)-1):

    buddiff=int(listcsv[row][1])-int(listcsv[row-1][1])


    prolosscsv[row][0] = listcsv[row][0]
    prolosscsv[row][1] = listcsv[row][1]
    prolosscsv[row][2] = int(buddiff)
    budchange=budchange+buddiff
    rownumber=row
#assing values to last list in prolosscsv
buddiff=int(listcsv[rownumber+1][1])-int(listcsv[rownumber][1])

prolosscsv[rownumber+1][0] = listcsv[rownumber+1][0]
prolosscsv[rownumber+1][1] = listcsv[rownumber+1][1]
prolosscsv[rownumber+1][2] = buddiff
budchange=budchange+buddiff

budtotal=0
for row in range(len(listcsv)):
    bud=int(listcsv[row][1])

    budtotal=budtotal+bud



totalmonths=len(listcsv)-1
#sorting on third element
def takeThird(elem):
    return elem[2]

sortedlist=sorted(prolosscsv,key=takeThird,reverse=True)
print(sortedlist)
print(budchange)
avgchange=budchange/totalmonths

file=open(csvpathwrite,"w")
print("Financial Analysis")
file.write("Financial Analysis\n")
print("-------------------------")
file.write("-------------------------\n")
print("Total Months: "+str(totalmonths))
file.write("Total Months: "+str(totalmonths)+"\n")
print("Total:" +str(budtotal))
file.write("Total:" +str(budtotal)+"\n")
print("Average Change "+str(avgchange))
file.write("Average Change "+str(avgchange)+"\n")

print("Greastest Increase in Profits:" +sortedlist[0][0]+"  "+"(%"+str(sortedlist[0][2])+")")
file.write("Greastest Increase in Profits:" +sortedlist[0][0]+"  "+"(%"+str(sortedlist[0][2])+")"+"\n")
print("Greatest Decrease in Profits:" +sortedlist[::-1][0][0]+"  "+"(%"+str(sortedlist[::-1][0][2])+")" )

file.write("Greatest Decrease in Profits:" +sortedlist[::-1][0][0]+"  "+"(%"+str(sortedlist[::-1][0][2])+")")