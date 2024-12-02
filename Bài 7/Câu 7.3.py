print("Le Hoa Hiep")
print("235752021610073")
def read_file(file_path):
    try:
        print(open(file_path, 'r').read())
    except FileNotFoundError:
        print("không tim thay file.")
    except Exception as e:
        print(f"Loi: {e}")
read_file('your_file.txt')
