print("Le Hoa Hiep")
print("235752021610073")
def Sequential_Search(dlist, item):
  for i in range(len(dlist)):
    if dlist[i] == item:
      return True, i
  return False, -1
n = int(input("Nhập số lượng phần tử: "))
dlist = []
for i in range(n):
  dlist.append(int(input(f"Nhập phần tử thứ {i+1}: ")))
item = int(input("Nhập phần tử cần tìm: "))
result, index = Sequential_Search(dlist, item)
if result:
  print(f"Tìm thấy {item} tại vị trí {index}")
else:
  print(f"Không tìm thấy {item}")
