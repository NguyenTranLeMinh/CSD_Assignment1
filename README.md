***

Bubble_Sort: giống như bong bóng nổi lên mặt nước, mỗi lần lặp ta đẩy 1 phần tử Max/Min nhất về bên phải.

Selection_Sort: CHỌN 1 phần tử Max/Min nhất từ mảng con bên phải, swap với vị trí cuối mảng con bên trái.

Insertion_Sort: Ý nghĩa là mảng con (bên trái) đã được sắp xếp. Sau mỗi lần lặp, ta chỉ CHÈN phần tử mới
                vào đúng vị trí trong mảng con đó.

# 11 6 4 3 2 9 8 9 4 7 6 1

***

Xây dựng chương trình để thực hiện các công việc sắp xếp và tìm kiếm trên một dãy số thực. Chương trình gồm các chức năng sau:

Nhập một dãy các số thực gồm có n số (n<=20)  lưu vào tệp INPUT.TXT

Đọc dữ liệu từ tệp INPUT.TXT lưu vào mảng 1 chiều a và hiển thị ra màn hình

Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, theo từng bước của thuật toán Bubble Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT1.TXT

Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, theo từng bước của thuật toán Selection Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT2.TXT

Hiển thị ra màn hình kết quả sắp xếp các phần tử trong mảng a ở câu 2 theo thứ tự tăng dần, theo từng bước của thuật toán Insert Sort (mỗi bước hiển thị lên 1 dòng) và lưu vào tệp OUTPUT3.TXT

Sử dụng phương pháp tìm kiếm tuần tự, hãy liệt kê ra màn hình chỉ số các phần tử (biết rằng phần tử đầu tiên có chỉ số là 0) trong mảng a  chưa được sắp xếp ở câu 2 có giá trị lớn hơn value (value là một số thực được nhập vào từ bàn phím), kết quả tìm được lưu vào dòng tiếp theo trong tệp OUTPUT4.TXT

Sử dụng phương pháp tìm kiếm nhị phân, hãy tìm chỉ số phần tử đầu tiên có giá trị bằng value (value là một số thực được nhập vào từ bàn phím) trên mảng đã a đã được sắp xếp.

***

Hướng dẫn

1. Thiết kế menu

Có ít nhất 7 chức năng để lựa chọn
Mỗi chức năng tương ứng với một câu hỏi
Không hạn chế số lần lựa chọn
2. Chức năng và yêu cầu 

Nhập dữ liệu từ bàn phím: 
Nhập giá trị của n;

Nhập giá trị của n số thực, lưu vào tệp INPUT.TXT.

Đọc dữ liệu từ tệp lưu vào mảng a và hiển thị dữ liệu ra màn hình 
Đọc dữ liệu sẽ lưu vào mảng a

Hiển thị dữ liệu của mảng a ra màn hình, mỗi phần tử cách nhau 1 vài khoảng trống

Sắp xếp theo thuật toán Bubble Sort
Lưu dữ liệu của mảng a sang một mảng b

Thực hiện thuật toán Bubble Sort trên mảng b  

Kết quả sắp xếp tại mỗi bước của thuật toán  sẽ in ra màn hình, lưu vào tệp (Mỗi bước liệt kê ra trên một dòng)

Sắp xếp theo thuật toán Selection Sort
Lưu dữ liệu của mảng a sang một mảng b

Thực hiện thuật toán Selection Sort trên mảng b 

Kết quả sắp xếp tại mỗi bước của thuật toán  sẽ in ra màn hình, lưu vào tệp (Mỗi bước liệt kê ra trên một dòng)

Sắp xếp theo thuật toán Insertion Sort
Lưu dữ liệu của mảng a sang một mảng b

Thực hiện thuật toán Insertion Sort trên mảng b  

Kết quả sắp xếp tại mỗi bước của thuật toán  sẽ in ra màn hình, lưu vào tệp (Mỗi bước liệt kê ra trên một dòng)

Tìm kiếm theo thuật toán tuần tự
Lưu dữ liệu của mảng a sang một mảng b

Nhập một số thực lưu vào biến value

Tìm kiếm tuần tự từng phần tử trên mảng b có giá trị lớn hơn value

Kết quả tìm được hiển thị ra màn hình, lưu vào tệp

Tìm kiếm theo thuật toán nhị phân
Lưu dữ liệu của mảng a sang một mảng b, sắp xếp mảng b;

Nhập một số thực lưu vào biến value

Tìm kiếm nhị phân để tìm chỉ số phần tử đầu tiên có giá trị bằng value trên mảng b

Kết quả tìm được hiển thị ra màn hình, lưu vào tệp

3. Tổ chức code

Kết quả khi chạy chương trình (Test case)

run:

+-------------------Menu------------------+

|      1.Manual Input                 |

|      2.File input                        |

|      3.Bubble sort                    |

|      4.Selection sort                 |

|      5.Insertion sort                  |

|      6.Search > value                |

|      7.Search = value                |

|      0.Exit                              |

+-----------------------------------------.+

 

- Nếu bấm 1, màn hình sẽ hiện ra:

Choice 1: Manual Input

Hướng dẫn nhập vào độ dài của chuỗi số:

Please enter input number of elements: ...

VD về output: 7

Hướng dẫn nhập vào từng số

Please enter input elements: ...

VD về output: 9 3 5 6 1 2 4

 

- Nếu bấm 2, màn hình sẽ hiện ra:

Choice 2: File input

Hướng dẫn nhập vào đường dẫn file file:

Please enter the file path: ...

VD về output: file có đường dẫn "data.txt"

In ra input đọc được ở trong file:

Input array: '9 3 5 6 1 2 4'

 

- Nếu bấm 3, màn hình sẽ hiện ra:

Choice 3: Bubble sort

3.0 5.0 6.0 1.0 2.0 4.0 9.0 

3.0 5.0 1.0 2.0 4.0 6.0 9.0 

3.0 1.0 2.0 4.0 5.0 6.0 9.0 

1.0 2.0 3.0 4.0 5.0 6.0 9.0 

1.0 2.0 3.0 4.0 5.0 6.0 9.0 

1.0 2.0 3.0 4.0 5.0 6.0 9.0 

 

- Nếu bấm 4, màn hình sẽ hiện ra:

Choice 4: Selection sort

1.0 3.0 5.0 6.0 9.0 2.0 4.0 

1.0 2.0 5.0 6.0 9.0 3.0 4.0 

1.0 2.0 3.0 6.0 9.0 5.0 4.0 

1.0 2.0 3.0 4.0 9.0 5.0 6.0 

1.0 2.0 3.0 4.0 5.0 9.0 6.0 

1.0 2.0 3.0 4.0 5.0 6.0 9.0 

 

- Nếu bấm 5, màn hình sẽ hiện ra:

Choice 5: Insertion sort

3.0 9.0 5.0 6.0 1.0 2.0 4.0 

3.0 5.0 9.0 6.0 1.0 2.0 4.0 

3.0 5.0 6.0 9.0 1.0 2.0 4.0 

1.0 3.0 5.0 6.0 9.0 2.0 4.0 

1.0 2.0 3.0 5.0 6.0 9.0 4.0 

1.0 2.0 3.0 4.0 5.0 6.0 9.0 

 

- Nếu bấm 6, màn hình sẽ hiện ra:

Choice 6: Linear Search

Hướng dẫn nhập vào giá trị tìm kiếm:

Please enter searched input value: ...

VD: Nếu input là 5 thì output sẽ là:

Larger position: 0 3  

 

- Nếu bấm 7, màn hình sẽ hiện ra:

Choice 7: Binary Search

Hướng dẫn nhập vào giá trị tìm kiếm:

Please enter searched input value: ...

VD: Nếu input là 5 thì output sẽ là:

The right position: 4

 

- Nếu bấm 0, màn hình sẽ hiện ra:

Thanks!!!

Và kết thúc chương trình.

Chú ý: Sau mỗi khi thực thi mỗi bước thì cần hiển thị lại menu để người dùng dễ dàng đưa ra lựa chọn.