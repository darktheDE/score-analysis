import CRUD

# code test CRUD
choose = -1
file_path = "diem_hoc_sinh_test.csv"
crud_instance = CRUD.CRUD(file_path)

while(choose != 0):
    print("\nMENU OPTIONS")
    print("1. Nhập điểm thi cho một thí sinh mới")
    print("2. Đọc dữ liệu điểm thi từ file dữ liệu và xuất ra màn hình")
    print("3. Cập nhật điểm thi thông qua số báo danh của một thí sinh")
    print("4. Xóa dữ liệu của một thí sinh thông qua số báo danh")
    print("0. Thoát chương trình")
    choose = int(input("\nNhập lựa chọn của bạn: "))

    if choose == 1:
        sbd_input = int(input("Nhập số báo danh: "))
        scores_input = {}
        for subject in crud_instance.subjects:
            score = -1.0
            while(score < 0):
                score = float(input(f"Nhập điểm thi môn {subject}: "))
                if score < 0 or score > 10:
                    print("Điểm thi không hợp lệ, vui lòng nhập lại!")
                else:
                    scores_input[subject] = score
        crud_instance.add_score(sbd_input, scores_input)
        print("Thêm dữ liệu cho thí sinh mới thành công!")

    elif choose == 2:
        print("Dữ liệu trong file đã được đọc thành công!")
        temp_list = crud_instance.read_score()
        for row in temp_list:
            print(row)

    elif choose == 3:
        sbd_input = ""
        check = True
        while check:
            sbd_input = input("Nhập số báo danh: ")
            temp_list = crud_instance.read_score()
            for row in temp_list:
                if sbd_input == row[0]:
                    check = False
                    break
            if check:
                print("Số báo danh không hợp lệ, vui lòng nhập lại!")
        subject_input = input("Nhập tên môn học cần cập nhật: ")
        new_score_input = -1.0
        while new_score_input < 0:
            new_score_input = float(input("Nhập điểm thi mới cần thay đổi: "))
            if new_score_input < 0 or new_score_input > 10:
                print("Điểm thi không hợp lệ, vui lòng nhập lại!")
        crud_instance.update_score(sbd_input, subject_input, new_score_input)
        print(f"Cập nhật điểm thi môn {subject_input} thí sinh {sbd_input} thành công!")

    elif choose == 4:
        check = True
        sbd_input = ""
        while check:
            sbd_input = input("Nhập số báo danh: ")
            temp_list = crud_instance.read_score()
            for row in temp_list:
                if sbd_input == row[0]:
                    check = False
                    break
            if check:
                print("Số báo danh không hợp lệ, vui lòng nhập lại!")
        print(f"Xóa thông tin thí sinh {sbd_input} thành công!")
        crud_instance.delete_score(sbd_input)

    if(choose == 0):
        pass

    else:
        print("\nLựa chọn không hợp lệ, vui lòng đọc menu và lựa chọn lại!")