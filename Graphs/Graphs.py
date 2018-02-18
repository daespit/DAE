import pandas as pd
import pylab as pl
import numpy as np

Color = ['gold','darkgreen','crimson','navy','plum','black','white','tomato','olive']
file_name = "W_Data.xlsx"
df = pd.read_excel(file_name)


Disease_List = list(set(df['Disease']))
Year_All = list(set(df['Year']))
Ward_All = list(set(df['Ward_Name']))
Months_All = list(set(df['Month']))

Ward_All.remove('Total')
Year_All.remove(0)

Rand = list()
count = 0

Disease_Name = ['Fever','Blood Pressure','Common Cold','Helminthiasis']

print(Disease_Name)

def DiseaseOccGraph():
    Disease_Occ = dict()


    global count
    for i in Disease_Name:
        Disease_Occ.update({i:0})
        Rand.append(count)
        count = count + 1

    print(Disease_Occ)
    for i in Disease_Name:
        for j in range(0,13240):
            if df['Disease'][j] == i:
                Disease_Occ[i] = Disease_Occ[i] + df['Occurances'][j]

    pl.bar(Rand, Disease_Occ.values(), align='center')
    pl.xticks(Rand, Disease_Occ.keys(), rotation=90)
    pl.ylabel("Occurances")
    pl.xlabel("Disease Name")
    pl.title("Occurances of Disease")
    pl.savefig('DO.png')
    #pl.show()



def DiseaseYearwise():
    Year_Wise = dict()
    Year_List = Year_All
    for i in Year_List:
        Year_Wise.update({i: [0]*len(Disease_Name)})

    for k in Year_List:
        for j in range(0, 13240):
            if df['Year'][j] == k:
                for i in range(0,len(Disease_Name)):
                    if df['Disease'][j] == Disease_Name[i]:
                        #print(k,i,j)
                        Year_Wise[k][i] = Year_Wise[k][i] + df['Occurances'][j]



    Temp = np.array([0]*len(Disease_Name))
    for k in range(0,len(Year_List)):
        pl.bar(Rand, Year_Wise[Year_List[k]],align = 'center', width=0.8, label=str(Year_List[k]), color=Color[k], bottom=Temp)
        Temp = Temp + np.array(Year_Wise[Year_List[k]])

    pl.xticks(Rand, Disease_Name, rotation = 90)
    pl.ylabel("Occurances")
    pl.xlabel("Disease Name")
    pl.legend(loc="upper left",prop={'size': 3})
    pl.title("Year-Wise Occurances of Disease")
    pl.savefig('DY.png')
    #pl.show()

def DiseaseWardwise():
    Ward_Wise = dict()
    Ward_List = Ward_All
    for i in Ward_List:
        Ward_Wise.update({i: [0]*len(Disease_Name)})

    for k in Ward_List:
        for j in range(0, 13240):
            if df['Ward_Name'][j] == k:
                for i in range(0,len(Disease_Name)):
                    if df['Disease'][j] == Disease_Name[i]:
                        #print(k,i,j)
                        Ward_Wise[k][i] = Ward_Wise[k][i] + df['Occurances'][j]


    print(Ward_Wise,Ward_List)
    Temp = np.array([0]*len(Disease_Name))
    for k in range(0,len(Ward_List)):
        print(k)
        pl.bar(Rand, Ward_Wise[Ward_List[k]],align = 'center', width=0.8, label=str(Ward_List[k]), color=Color[k%9], bottom=Temp)
        Temp = Temp + np.array(Ward_Wise[Ward_List[k]])

    pl.xticks(Rand, Disease_Name, rotation = 90)
    pl.ylabel("Occurances")
    pl.xlabel("Disease Name")
    pl.legend(loc="upper left",prop={'size': 3})
    pl.title("Ward-Wise Occurances of Disease")
    pl.savefig('DW.png')
    #pl.show()



def DiseaseMonthwise():
    Month_Wise = dict()
    Month_List = Months_All
    for i in Month_List:
        Month_Wise.update({i: [0]*len(Disease_Name)})

    for k in Month_List:
        for j in range(0, 13240):
            if df['Month'][j] == k:
                for i in range(0,len(Disease_Name)):
                    if df['Disease'][j] == Disease_Name[i]:
                        #print(k,i,j)
                        Month_Wise[k][i] = Month_Wise[k][i] + df['Occurances'][j]



    Temp = np.array([0]*len(Disease_Name))
    for k in range(0,len(Month_List)):
        pl.bar(Rand, Month_Wise[Month_List[k]],align = 'center', width=0.8, label=str(Month_List[k]), color=Color[k%9], bottom=Temp)
        Temp = Temp + np.array(Month_Wise[Month_List[k]])

    pl.xticks(Rand, Disease_Name, rotation = 90)
    pl.ylabel("Occurances")
    pl.xlabel("Disease Name")
    pl.legend(loc="upper left",prop={'size': 3})
    pl.title("Month-Wise Occurances of Disease")
    pl.savefig('DM.png')
    #pl.show()


DiseaseOccGraph()
DiseaseYearwise()
DiseaseWardwise()
DiseaseMonthwise()
