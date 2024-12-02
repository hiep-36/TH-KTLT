print("Le Hoa Hiep")
print("235752021610073")
ho_ten=input("nhap ho ten day du cua ban:")
slist=ho_ten.split()
n=len(slist)
ho=slist[0]
ten=slist[n-1]
dem=" ".join(slist[1:n-1])
print("ten cua ban la: ",ten)
print("ho cua ban la: ",ho)
if n>2:
    print("ten dem cua ban la: ",dem)
