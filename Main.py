import CRUD
import subprocess
import os
file_path1 = "diem2023.csv"
file_path2 = "diem2024.csv"
crud_instance_2023 = CRUD.CRUD(file_path1)
crud_instance_2024 = CRUD.CRUD(file_path2)

def isFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def menu(crud):
    choose = "-1"
    while True:
        print("\nSUB-MENU OPTIONS")
        print("1. Nhập điểm thi cho một thí sinh mới")
        print("2. Đọc dữ liệu điểm thi từ file dữ liệu và xuất ra màn hình")
        print("3. Cập nhật điểm thi thông qua số báo danh của một thí sinh")
        print("4. Xóa dữ liệu của một thí sinh thông qua số báo danh")
        print("5. Xuất ra màn hình thủ khoa các khối thi ở TPHCM")
        print("6. Sắp xếp điểm tăng dần/giảm dần theo môn học")
        print("7. Tìm thông tin điểm thi của thí sinh theo số báo danh")
        print("8. Tìm thông tin thí sinh theo môn thi và điểm thi")
        print("0. Về lại menu chính")

        choose = input("\nNhập lựa chọn của bạn: ")
        
        if choose == "1":
            sbd_input = ""
            while len(sbd_input) != 8 or not sbd_input.isdigit:
                sbd_input = input("Nhập số báo danh: ")
                if len(sbd_input) != 8 or not sbd_input.isdigit:
                    print("Số báo danh không hợp lệ, vui lòng nhập lại theo format của bộ giáo dục!")

            scores_input = {}
            for subject in crud.subjects:
                score_input = ""
                check_num = True
                check_abc = True
                score_float = 0

                while check_num or check_abc:
                    score_input = input(f"Nhập điểm thi môn {crud.convert[subject]} (-1 nếu không thi môn đó): ")
                    check_num = False
                    check_abc = False
                    for i in range(len(score_input)):
                        if score_input[0] == '-':
                            continue
                        if isFloat(score_input) == False:
                            check_abc = True
                            print("Có lỗi xảy ra, vui lòng nhập điểm là chữ số!")
                            break
                    
                    if check_abc == False:
                        score_float = float(score_input)
                        if score_float < -1 or score_float > 10:
                            print("Điểm thi không hợp lệ, vui lòng nhập lại!")
                            check_num = True

                if score_float == -1:
                    scores_input[subject] = ''
                else:
                    scores_input[subject] = score_float
                
            crud.add_score(sbd_input, scores_input)
            print("Thêm dữ liệu cho thí sinh mới thành công!")

        elif choose == "2":
            temp_list = crud.read_score()
            for row in temp_list:
                print(row)
            print("\nDữ liệu trong file đã được đọc thành công!")

        elif choose == "3":
            sbd_input = ""
            subject_input = ""
            score_float = 0
            check = True
            while check:
                sbd_input = input("Nhập số báo danh: ")
                temp_list = crud.read_score()
                for row in temp_list:
                    if sbd_input == row[0]:
                        check = False
                        break
                    
                if check == False:
                    subject_input = ''
                    while subject_input not in crud.subjects:
                        subject_input = input("Nhập tên môn học cần cập nhật: ")
                        if subject_input not in crud.subjects:
                            print("Không tìm thấy môn học này trong các môn thi, vui lòng thử lại theo danh sách các môn\n", crud.subjects)

                    score_input = ""
                    check_num = True
                    check_abc = True
                    while check_num or check_abc:
                        score_input = input(f"Nhập điểm thi môn {crud.convert[subject_input]} cần thay đổi: ")
                        check_num = False
                        check_abc = False
                        for i in range(len(score_input)):
                            if score_input[0] == '-':
                                continue
                            if isFloat(score_input) == False:
                                check_abc = True
                                print("Có lỗi xảy ra, vui lòng nhập điểm là chữ số!")
                                break
                    
                        if check_abc == False:
                            score_float = float(score_input)
                            if score_float < -1 or score_float > 10:
                                print("Điểm thi không hợp lệ, vui lòng nhập lại!")
                                check_num = True
                                
                if check == True:
                    print("Số báo danh không hợp lệ, vui lòng nhập lại!")

            crud.update_score(sbd_input, subject_input, score_float)
            print(f"Cập nhật điểm thi môn {crud.convert[subject_input]} thí sinh {sbd_input} thành công!")

        elif choose == "4":
            check = True
            sbd_input = ""
            while check:
                sbd_input = input("Nhập số báo danh: ")
                temp_list = crud.read_score()
                for row in temp_list:
                    if sbd_input == row[0]:
                        check = False
                        break
                if check:
                    print("Số báo danh không hợp lệ, vui lòng nhập lại!")

            print(f"\nXóa thông tin thí sinh {sbd_input} thành công!")
            crud.delete_score(sbd_input)
            
        elif choose == '5':
            crud.find_top_scorer_per_group()

        elif choose == '6':
            subject_input = input("Nhập tên môn học cần sắp xếp theo điểm thi: ")
            user_input = ""
            isDescending = True
            while True:
                user_input = input("Tăng dần (A) / giảm dần (D): ")
                if user_input == "A" or user_input == "D" or user_input == 'a' or user_input == 'd':
                    break
                else:
                    print("Lựa chọn không hợp lệ, vui lòng lựa thử lại!")
            
            if user_input == "A" or user_input == 'a':
                isDescending = False

            crud.sort_by_subject(subject_input, isDescending)

        elif choose == '7':
            sbd_input = ""
            while len(sbd_input) != 8 or not sbd_input.isdigit:
                sbd_input = input("Nhập số báo danh cần tìm kiếm: ")
                if len(sbd_input) != 8 or not sbd_input.isdigit:
                    print("Số báo danh không hợp lệ, vui lòng nhập lại theo format của bộ giáo dục!")
                                
            crud.find_by_sbd(sbd_input)

        elif choose == '8':
            subject_input = ''
            while subject_input not in crud.subjects:
                subject_input = input("Nhập môn học cần tìm kiếm: ")
                if subject_input not in crud.subjects:
                    print("Không tìm thấy môn học này trong các môn thi, vui lòng thử lại theo danh sách các môn\n", crud.subjects)
            check_num = True
            check_abc = True
            score_float = 0
            while check_num or check_abc:
                check_num = False
                check_abc = False
                score_input = input("Nhập điểm thi môn học cần tìm kiếm: ")
                if score_input[0] == '-':
                    print("\nVui lòng nhập điểm thi không âm!")
                    check_num = True
                else:
                    for i in range(len(score_input)):
                        if isFloat(score_input) == False:
                            check_abc = True
                            print("\nVui lòng nhập điểm thi là chữ số!")
                            break
                    if check_abc == False:
                        score_float = float(score_input)
                        if score_float > 10:
                            print("\nĐiểm thi không hợp lệ, vui lòng nhập lại!")
                            check_num = True

            crud.find(subject_input, score_float)
            
        elif choose == "0":
            # Kiểm tra hệ điều hành nt = Windows -> thực hiện clrsc trên terminal
            subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
            break

        else:
            print("\nLựa chọn không hợp lệ, vui lòng lựa chọn lại!")


choose = "-1"
while True:
    print("\nMAIN MENU OPTIONS")
    print("1. Thực hiện các thao tác trên dữ liệu điểm thi năm 2023")
    print("2. Thực hiện các thao tác trên dữ liệu điểm thi năm 2024")
    print("0. Thoát chương trình")
    choose = input("Nhập lựa chọn của bạn: ")
    if choose == "1":
        menu(crud_instance_2023)
    elif choose == "2":
        menu(crud_instance_2024)
    elif choose == "0":
        break
    else:
        print("\nLựa chọn không hợp lệ, vui lòng nhập lại!")

