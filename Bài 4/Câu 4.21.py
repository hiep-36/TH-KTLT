def check_divisible_by_5(binary_numbers):
    divisible_by_5 = []
    for binary in binary_number.split(','):
        binary = binary.strip()
        if len(binary)== 4 and all(bit in '01' for bit in binary):
            decinal = int(binacy, 2)
            if decinal % 5 == 0:
                divisible_by_5.append(binary)
        else:
            print(f"so nhi phan'(binacy)'khong hop le.")
    return','.join(divisible_by_5)
input_binary = input("Nhap chuoi cac so nhi phan 4 chu so, phan tach boi dau phay:")
result = check_divisible_by_5(input_binary)
if result:
    print("cac so nhi phan chia het cho 5 la:", result)
else:
    print("khong co so nhi phan nao chia het cho 5.")
            
