import typing

PATH = ''
# 11 6 4 3 2 9 8 9 4 7 6 1

# Criterion 1
def nhap(file_name=PATH+'INPUT.TXT', data=None) -> typing.List:
    with open(file_name, mode='w') as f:
        if data is None:
            stdin = input('Nhap day so: ')
        else:
            # Để ghi vào file cần chuyển sang dạng string
            stdin = ' '.join(map(str, data))
        f.write(stdin)
    a = list(map(float, stdin.split()))
    return a

# Criterion 2    
def xuat(file_name=PATH+'INPUT.TXT') -> typing.List:
    with  open(file_name, mode='r') as f:
        try:
            lst = next(f).split()
            a = list(map(float, lst))
            print('Du lieu tu file:', *a)
        except (UnboundLocalError, StopIteration):
            pass
    
    #return a

# Criterion 3
def Bubble_Sort(a: typing.List) -> None:
    lst = a.copy()
    n = len(lst)
    print('Bubble_Sort')
    print('Unsorted:', *a)
    for i in range(1, n):
        for j in range(0, n-i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print(f'Buoc {i}: {lst}')
    
    nhap(file_name=PATH+'OUTPUT1.TXT', data=lst)

# Criterion 4
def Selection_Sort(a: typing.List) -> None:
    lst = a.copy()
    n = len(lst)
    print('Selection_Sort:')
    print('Unsorted:', *a)
    for i in range(n-1):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
        print(f'Buoc {i+1}: {lst}')
    
    nhap(file_name=PATH+'OUTPUT2.TXT', data=lst)

# Criterion 5
def Insertion_Sort(a: typing.List) -> None:
    lst = a.copy()
    n = len(lst)
    print('Insertion_Sort:')
    print('Unsorted:', *a)
    for i in range(1, n):
        for j in range(0, i):
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
        print(f'Buoc {i}: {lst}')
    
    nhap(file_name=PATH+'OUTPUT3.TXT', data=lst)

# Criterion 6
def Linear_Search(a: typing.List) -> None:
    lst = a.copy()
    n = len(lst)
    print('Linear_Search:')
    print('Unsorted:', *a)
    value = float(input('Nhap gia tri: '))
    indexs = []
    for i in range(n):
        if lst[i] > value:
            indexs.append(i)
    line = 'Cac chi so trong mang ma gia tri tai do lon hon ' + str(value) + ': '
    print(line, *indexs)

    nhap(file_name=PATH+'OUTPUT4.TXT', data=indexs)

# Criterion 7
def Binary_Search(a: typing.List) -> None:
    lst = a.copy()
    n = len(lst)
    # Sắp xếp lại mảng tăng dần bằng Selection
    for i in range(n-1):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
    print('Binary_Search:')
    print('Sorted:', *lst)
    value = float(input('Nhap gia tri can tim: '))
    l = 0
    r = n-1
    while l <= r:
        mid = (l + r) // 2
        if lst[mid] > value:
            # tìm tiếp trong mảng con bên trái
            r = mid-1
        elif lst[mid] < value:
            # tìm tiếp trong mảng con bên phải
            l = mid+1
        else:
            break
    if l > r:
        mid = -1
        print('Khong tim thay')
    else:
        print('Vi tri tim duoc:', mid)

class Choice:
    def __init__(self, choice=None):
        self.choice = choice
        self.input_stt = 'Lựa chọn của bạn (Vui lòng nhập STT tương ứng): '
        self.a = list()
    
    def menu(self):
        print('*****')
        print('MENU')
        print('*****')
        print('0. Thoát chương trình')
        print('1. Nhập dữ liệu vào file INPUT.TXT')
        print('2. Xuất dữ liệu trong file INPUT.TXT')
        print('3. Sử dụng "Sắp xếp nổi bọt"')
        print('4. Sử dụng "Sắp xếp lựa chọn"')
        print('5. Sử dụng "Sắp xếp chèn"')
        print('6. Sử dụng "Tìm kiếm tuần tự"')
        print('7. Sử dụng "Tìm kiếm nhị phân"')
        print('*****')

    def get_choice(self):
        self.choice = input(self.input_stt)
        self.validation()

    def validation(self):
        # Kiểm tra input cho den khi hop le
        while 1:
            try:
                self.choice = int(self.choice)
                if 0 <= self.choice <= 7:
                    break
                else:
                    print('Vui lòng nhập STT từ 0-7.')
            except ValueError:
                print('Vui lòng nhập 1 số nguyên.')
            
            self.get_choice()

    def operation(self):
        if self.choice == 1:
            self.a = nhap()
        elif self.choice == 2:
            xuat()
        elif self.choice == 3:
            Bubble_Sort(self.a)
        elif self.choice == 4:
            Selection_Sort(self.a)
        elif self.choice == 5:
            Insertion_Sort(self.a)
        elif self.choice == 6:
            Linear_Search(self.a)
        elif self.choice == 7:
            Binary_Search(self.a)

def final():
    c = Choice()
    while c.choice != 0:
        c.menu()
        c.get_choice()
        c.operation()


if __name__ == "__main__":
    final()
