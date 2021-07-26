import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_csv("ToHopTuNhien.csv")
data2 = pd.read_csv("ToHopXaHoi.csv")


#Toán
truc_diem_toan = [i/10 for i in range(0,101,2)]
count_toan = [0 for i in range(len(truc_diem_toan))]

for i in range(len(truc_diem_toan)):
    for diem in data1.values[:,1]:
        if diem == truc_diem_toan[i]:
            count_toan[i] += 1


#Anh
truc_diem_anh = [i/10 for i in range(0,101,2)]
count_anh = [0 for i in range(len(truc_diem_anh))]

for i in range(len(truc_diem_anh)):
    for diem in data1.values[:,6]:
        if diem == truc_diem_anh[i]:
            count_anh[i] += 1

# #Văn
truc_diem_van = [i/100 for i in range(0,1001,25)]
count_van = [0 for i in range(len(truc_diem_van))]

for i in range(len(truc_diem_van)):
    for diem in data1.values[:,2]:
        if diem == truc_diem_van[i]:
            count_van[i] += 1

#Lý
truc_diem_ly = [i/100 for i in range(0,1001,25)]
count_ly = [0 for i in range(len(truc_diem_ly))]

for i in range(len(truc_diem_ly)):
    for diem in data1.values[:,3]:
        if diem == truc_diem_ly[i]:
            count_ly[i] += 1

#Hóa
truc_diem_hoa = [i/100 for i in range(0,1001,25)]
count_hoa = [0 for i in range(len(truc_diem_hoa))]

for i in range(len(truc_diem_hoa)):
    for diem in data1.values[:,4]:
        if diem == truc_diem_hoa[i]:
            count_hoa[i] += 1

#Sinh
truc_diem_sinh = [i/100 for i in range(0,1001,25)]
count_sinh = [0 for i in range(len(truc_diem_sinh))]

for i in range(len(truc_diem_sinh)):
    for diem in data1.values[:,5]:
        if diem == truc_diem_sinh[i]:
            count_sinh[i] += 1

sum_ly = 0
thisinh = sum(count_ly)

for i in range(len(truc_diem_ly)):
     tong = truc_diem_ly[i] * count_ly[i]
     sum_ly += tong

print(sum_ly/thisinh)



ax1 = plt.subplot2grid((2,3),(0,0))
ax1.bar(truc_diem_toan, count_toan, align='center', width=0.1, alpha =0.5)

ax1.set_title('Điểm Toán')

ax2 = plt.subplot2grid((2,3),(0,1))
ax2.bar(truc_diem_van, count_van, align='center', width=0.1, alpha =0.5)
ax2.set_title('Điểm Văn')

ax3 = plt.subplot2grid((2,3),(0,2))
ax3.bar(truc_diem_anh, count_anh, align='center', width=0.1, alpha =0.5)
ax3.set_title('Điểm Anh')

ax4 = plt.subplot2grid((2,3),(1,0))
ax4.bar(truc_diem_ly, count_ly, align='center', width=0.1, alpha =0.5)
ax4.set_title('Điểm Lý')

ax5 = plt.subplot2grid((2,3),(1,1))
ax5.bar(truc_diem_hoa, count_hoa, align='center', width=0.1, alpha =0.5)
ax5.set_title('Điểm Hóa')

ax6 = plt.subplot2grid((2,3),(1,2))
ax6.bar(truc_diem_sinh, count_sinh, align='center', width=0.1, alpha =0.5)
ax6.set_title('Điểm Sinh')


plt.suptitle("Biểu đồ điểm thi THPT 2021 tỉnh Bắc Ninh")
plt.show()




