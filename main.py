
import pandas as pd
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)
criminal = pd.read_csv("criminal data3.csv", encoding='cp949')
import matplotlib.pyplot as plt


#저학력자 범죄 종류

df1=criminal[['범죄대분류','범죄중분류','전문직(예술인)']]
low_w1=df1.sort_values(ascending = False,by = '전문직(예술인)').head()

df2=criminal[['범죄대분류','범죄중분류','자영업(농.임.수산업)']]
low_w2=df2.sort_values(ascending = False,by = '자영업(농.임.수산업)').head()

df3=criminal[['범죄대분류','범죄중분류','피고용자(운전사)']]
low_w3=df3.sort_values(ascending = False,by = '피고용자(운전사)').head()

df4=criminal[['범죄대분류','범죄중분류','자영업(요식업)']]
low_w4=df4.sort_values(ascending = False,by = '자영업(요식업)').head()

df5=criminal[['범죄대분류','범죄중분류','자영업(도.소매업)']]
low_w5=df5.sort_values(ascending = False,by = '자영업(도.소매업)').head()

#고학력자 범죄 종류

dk1=criminal[['범죄대분류','범죄중분류','공무원']]
heigh_w1=dk1.sort_values(ascending = False,by = '공무원').head()

dk2=criminal[['범죄대분류','범죄중분류','전문직(교수)']]
heigh_w2=dk2.sort_values(ascending = False,by = '전문직(교수)').head()

dk3=criminal[['범죄대분류','범죄중분류','전문직(변호사)']]
heigh_w3=dk3.sort_values(ascending = False,by = '전문직(변호사)').head()

dk4=criminal[['범죄대분류','범죄중분류','전문직(의사)']]
heigh_w4=dk4.sort_values(ascending = False,by = '전문직(의사)').head()

dk5=criminal[['범죄대분류','범죄중분류','피고용자(기술자)']]
heigh_w5=dk5.sort_values(ascending = False,by = '피고용자(기술자)').head()
print("======================================================")
print(low_w1)
print("======================================================")
print(low_w2)
print("======================================================")
print(low_w3)
print("======================================================")
print(low_w4)
print("======================================================")
print(low_w5)

print("======================================================")
print(heigh_w1)
print("======================================================")
print(heigh_w2)
print("======================================================")
print(heigh_w3)
print("======================================================")
print(heigh_w4)
print("======================================================")
print(heigh_w5)
print("======================================================")

# 분야별 지능범죄 비율

lw1=low_w1['전문직(예술인)'].sum()
lw1a=low_w1[low_w1['범죄대분류']=='지능범죄']
lw1b=lw1a['전문직(예술인)'].sum()
result1=lw1b/lw1

lw2=low_w2['자영업(농.임.수산업)'].sum()
lw2a=low_w2[low_w2['범죄대분류']=='지능범죄']
lw2b=lw2a['자영업(농.임.수산업)'].sum()
result2=lw2b/lw2

lw3=low_w3['피고용자(운전사)'].sum()
lw3a=low_w3[low_w3['범죄대분류']=='지능범죄']
lw3b=lw3a['피고용자(운전사)'].sum()
result3=lw3b/lw3

lw4=low_w4['자영업(요식업)'].sum()
lw4a=low_w4[low_w4['범죄대분류']=='지능범죄']
lw4b=lw4a['자영업(요식업)'].sum()
result4=lw4b/lw4

lw5=low_w5['자영업(도.소매업)'].sum()
lw5a=low_w5[low_w5['범죄대분류']=='지능범죄']
lw5b=lw5a['자영업(도.소매업)'].sum()
result5=lw5b/lw5

hw1=heigh_w1['공무원'].sum()
hw1a=heigh_w1[heigh_w1['범죄대분류']=='지능범죄']
hw1b=hw1a['공무원'].sum()
result6=hw1b/hw1

hw2=heigh_w2['전문직(교수)'].sum()
hw2a=heigh_w2[heigh_w2['범죄대분류']=='지능범죄']
hw2b=hw2a['전문직(교수)'].sum()
result7=hw2b/hw2

hw3=heigh_w3['전문직(변호사)'].sum()
hw3a=heigh_w3[heigh_w3['범죄대분류']=='지능범죄']
hw3b=hw3a['전문직(변호사)'].sum()
result8=hw3b/hw3

hw4=heigh_w4['전문직(의사)'].sum()
hw4a=heigh_w4[heigh_w4['범죄대분류']=='지능범죄']
hw4b=hw4a['전문직(의사)'].sum()
result9=hw4b/hw4

hw5=heigh_w5['피고용자(기술자)'].sum()
hw5a=heigh_w5[heigh_w5['범죄대분류']=='지능범죄']
hw5b=hw5a['피고용자(기술자)'].sum()
result10=hw5b/hw5



criminal_value = dict()
criminal_value = {
    '전문직(예술인)': result1,
    '자영업(농.임.수산업)' : result2,
    '피고용자(운전사)' : result3,
    '자영업(요식업)': result4,
    '자영업(도.소매업)': result5,
    '공무원': result6,
    '전문직(교수)': result7,
    '전문직(변호사)': result8,
    '피고용자(기술자)': result10,
}
print(criminal_value)
cd = pd.DataFrame(criminal_value,index=["지능범죄비율"])
cd = cd.transpose()
cd.plot(kind='bar', y='지능범죄비율',color='red')

print(cd)
plt.show()


# heigh_w4.plot(kind='bar',x='범죄대분류',y='전문직(의사)', color='blue')
# #plt.show()
# #
# heigh_w5.plot(kind='bar',x='범죄대분류',y='피고용자(기술자)', color='blue')
# # plt.show()
# #
# heigh_w3.plot(kind='bar',x='범죄대분류',y='전문직(변호사)', color='blue')
# # plt.show()
# #
# heigh_w2.plot(kind='bar',x='범죄대분류',y='전문직(교수)', color='blue')
# # plt.show()
# #
# heigh_w1.plot(kind='bar',x='범죄대분류',y='공무원', color='blue')
# plt.show()

