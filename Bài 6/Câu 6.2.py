print("Le Hoa Hiep")
print("235752021610073")
class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        if chieu_dai <= 0 or chieu_rong <= 0:
            raise ValueError("Chiều dài và chiều rộng phải lớn hơn 0")
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong
hcn = Hinhchunhat(5, 3)
print("Diện tích hình chữ nhật:", hcn.dien_tich())
