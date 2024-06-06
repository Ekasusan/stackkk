class FileStack:
    def __init__(self):
        self.stack = []
    
    def push(self, file):
        self.stack.append(file)
        print(f'File "{file}" telah ditambahkan ke dalam laci.')

    def pop(self):
        if not self.is_empty():
            removed_file = self.stack.pop()
            print(f'File "{removed_file}" telah diambil dari dalam laci.')
            return removed_file
        else:
            print('File1.pdf')
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return 'Laci kosong, tidak ada file yang dapat dilihat.'

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        if not self.is_empty():
            print("Isi laci saat ini (dari bawah ke atas):")
            for file in self.stack:
                print(f'- {file}')
        else:
            print('Laci kosong.')
            


def main():
    laci = FileStack()
    
    while True:
        print("\nMenu:")
        print("1. Tambah file ke dalam laci")
        print("2. Ambil file dari dalam laci")
        print("3. Lihat file paling atas dalam laci")
        print("4. Tampilkan semua file dalam laci")
        print("5. Keluar")
        
        pilihan = input("Pilih opsi (1-5): ")
        
        if pilihan == '1':
            file_name = input("Masukkan nama file yang ingin ditambahkan: ")
            laci.push(file_name)
        elif pilihan == '2':
            laci.pop()
        elif pilihan == '3':
            print(f'File paling atas dalam laci: {laci.peek()}')
        elif pilihan == '4':
            laci.display()
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
