print("Le Hoa Hiep")
print("235752021610073")
def tim_tu_dai_nhat(cau):
  cac_tu = cau.split()

  do_dai_lon_nhat = 0
  for tu in cac_tu:
    if len(tu) > do_dai_lon_nhat:
      do_dai_lon_nhat = len(tu)

  print("Các từ dài nhất:")
  for tu in cac_tu:
    if len(tu) == do_dai_lon_nhat:
      print(tu)

cau = input("Nhập một câu: ")
tim_tu_dai_nhat(cau)
