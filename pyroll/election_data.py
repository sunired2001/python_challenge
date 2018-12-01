import csv
import os
sumlist=[[],[]]
sortedlist=[[],[]]
voterlist=[]
totelvotes=0

csvpath=os.path.join("election_data.csv")
csvpathwrite=os.path.join("election_datawrite.txt")
with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    header=next(csvreader)
    listdata=list(csvreader)

sumlist=[[],[]]
sortedlist=[[],[]]
    
#to assign initial values to nexted list if not throw error when try to access this index
for x in range(4):


        voterlist.append(['',0,0])
#function to sort on certain index
def takeThird(elem):
    return elem[2]

sortedlist=sorted(listdata,key=takeThird)
#total number of votes for all voters
totalvotes=0
for i in range(len(sortedlist)):
    totalvotes=int(totalvotes+1)

j=0
total=0
tmpname=sortedlist[0][2]
#as list is already sorted assign the total and name when name changes

for i in range(len(sortedlist)):
    if(tmpname==sortedlist[i][2]):
        total=total+1
        
        voterlist[j][0]=tmpname
        voterlist[j][1]=total
        voterlist[j][2] = total/totalvotes



    else:
        j=j+1
        total=1
        tmpname = sortedlist[i][2]

        voterlist[j][0]=tmpname
        voterlist[j][1]=total

        voterlist[j][2] = total / totalvotes


sortedonvoter=[[],[],[]]
def takeSecond(elem):
    return elem[1]
#sort list by total votes of each person to take first element as highest votes
voterlist=sorted(voterlist,key=takeSecond,reverse=True)


file=open(csvpathwrite,"w")

print("Election Results")
file.write("Election Results"+'\n')
print("----------------------------------"+'\n')
file.write("----------------------------------"+'\n')
print(f'Total Votes: {totalvotes}')
file.write('Total Votes:'+str(totalvotes)+'\n')
print("----------------------------------")
file.write("----------------------------------")
for i in range(len(voterlist)):

    print(voterlist[i][0]+": "+"{:2.4%}".format((voterlist[i][1]/totalvotes))+" ("+str(voterlist[i][1]) +")")
    file.write(str(voterlist[i][0]) + ": " + "{:2.3%}".format((voterlist[i][1] / totalvotes)) + " (" + str(
        voterlist[i][1]) + ")" + '\n')

print(f'Winner : {voterlist[0][0]}')
file.write("Winner :"+str(voterlist[0][0])+'\n')
print("----------------------------------")
file.write("----------------------------------")



