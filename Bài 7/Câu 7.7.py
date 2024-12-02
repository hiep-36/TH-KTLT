print("Le Hoa Hiep")
print("235752021610073")
def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)  
    return line_count

filename = 'test.txt'
line_count = count_lines_in_file(filename)
print(f"Số dòng trong tệp {filename}: {line_count}")
