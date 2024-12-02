print("Le Hoa Hiep")
print("235752021610073")
def tong_cua_uoc_so(n):
    for i in range(1,n):
        tong_uoc=0
    for j in range(1,i+1):
        if i % j ==0:
            tong_uoc +=j
    if tong_uoc>i:
        print(i)
n=int(input("nhap so nguyen duong n: "))
tong_cua_uoc_so(n)
