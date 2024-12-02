print("Le Hoa Hiep")
print("235752021610073")
def benefit(t, n, k):
    return n * (1 + t / 100) ** k

t = float(input("Nhap lai suat(%/thang): "))
n = float(input("Nhap so von ban dau: "))
k = int(input("Nhap so thang gui: "))

so_tien = benefit(t, n, k)
print(f"So tien nha duoc sau (k) thang gui la: (so_tien:.2f)")
