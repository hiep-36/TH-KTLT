print("Le Hoa Hiep")
print("235752021610073")
def copy_file (output_file, destination_file):
    try:
        with open (output_file, 'r') as src, open (destination_file, 'w') as dest:
             content = src.read()
             dest.write (content)
        print (f"Nội dung đã được sao chép từ (output_file) sang (destination_file).")
    except FileNotFoundError:
        print("Tệp nguồn không tồn tại.")
    except Exception as e:
        print (f"Lỗi: (e)")
copy_file('output.txt', 'destination.txt')
