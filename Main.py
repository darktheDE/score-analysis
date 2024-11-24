import CRUD

file_path1 = "diem2023.csv"
file_path2 = "diem2024.csv"
crud_instance_2023 = CRUD.CRUD(file_path1)
crud_instance_2024 = CRUD.CRUD(file_path2)


def add_new_score():
    choose = "-1"
    while choose != "0":
        print("\nMENU OPTIONS")
        print("1. Thêm điểm thi cho thí sinh mới vào dữ liệu năm 2023")
        print("2. Thêm điểm thi cho thí sinh mới vào dữ liệu năm 2024")
        print("0. Trở lại menu chính")

        choose = input("\nNhập lựa chọn của bạn: ")

        if choose == "1":
            sbd_input = input("Nhập số báo danh: ")
            scores_input = {}
            for subject in crud_instance_2023.subjects:
                score = ""
                check_number = True
                check_string = True
                score_float = 0
                while check_number or check_string:
                    score = input(
                        f"Nhập điểm thi môn {subject} (-1 nếu không thi môn đó): "
                    )
                    check_number = False
                    check_string = False
                    for i in range(len(score)):
                        if score[0] == "-":
                            continue
                        if score[i].isdigit() == False:
                            check_string = True
                            print("Có lỗi xảy ra, vui lòng nhập điểm là chữ số!")
                            break

                    if check_string == False:
                        score_float = float(score)
                        if score_float < -1 or score_float > 10:
                            print("Điểm thi không hợp lệ, vui lòng nhập lại!")
                            check_number = True

                if score_float == -1:
                    scores_input[subject] = ""
                else:
                    scores_input[subject] = score_float

            crud_instance_2023.add_score(sbd_input, scores_input)
            print("Thêm dữ liệu cho thí sinh mới năm 2023 thành công!")

        elif choose == "2":
            sbd_input = input("Nhập số báo danh: ")
            scores_input = {}
            for subject in crud_instance_2024.subjects:
                score = ""
                check_number = True
                check_string = True
                score_float = 0
                while check_number or check_string:
                    score = input(
                        f"Nhập điểm thi môn {subject} (-1 nếu không thi môn đó): "
                    )
                    check_number = False
                    check_string = False
                    for i in range(len(score)):
                        if score[0] == "-":
                            continue
                        if score[i].isdigit() == False:
                            check_string = True
                            print("Có lỗi xảy ra, vui lòng nhập điểm là chữ số!")
                            break

                    if check_string == False:
                        score_float = float(score)
                        if score_float < -1 or score_float > 10:
                            print("Điểm thi không hợp lệ, vui lòng nhập lại!")
                            check_number = True

                if score_float == -1:
                    scores_input[subject] = ""
                else:
                    scores_input[subject] = score_float

            crud_instance_2024.add_score(sbd_input, scores_input)
            print("Thêm dữ liệu cho thí sinh mới năm 2024 thành công!")

        elif choose == "0":
            break

        else:
            print("\nLựa chọn không hợp lệ, vui lòng đọc menu và lựa chọn lại!")


choose = "-1"
while choose != "0":
    print("\nMENU OPTIONS")
    print("1. Nhập điểm thi cho một thí sinh mới")
    print("2. Đọc dữ liệu điểm thi từ file dữ liệu và xuất ra màn hình")
    print("3. Cập nhật điểm thi thông qua số báo danh của một thí sinh")
    print("4. Xóa dữ liệu của một thí sinh thông qua số báo danh")
    print("5. Xuất ra màn hình điểm trung bình từng tỉnh thành")
    print("6. Xuất ra màn hình thủ khoa cho từng khối")
    print("0. Thoát chương trình")
    choose = input("\nNhập lựa chọn của bạn: ")

    if choose == "1":
        add_new_score()

    # elif choose == 2:
    #     print("Dữ liệu trong file đã được đọc thành công!")
    #     temp_list = crud_instance.read_score()
    #     for row in temp_list:
    #         print(row)

    # elif choose == 3:
    #     sbd_input = ""
    #     subject_input = ""
    #     score_float = 0
    #     check = True
    #     while check:
    #         sbd_input = input("Nhập số báo danh: ")
    #         temp_list = crud_instance.read_score()
    #         for row in temp_list:
    #             if sbd_input == row[0]:
    #                 check = False
    #                 break

    #         if check == False:
    #             subject_input = input("Nhập tên môn học cần cập nhật: ")
    #             score = ""
    #             check_number = True
    #             check_string = True
    #             while(check_number or check_string):
    #                 score = input(f"Nhập điểm thi môn {subject_input} cần thay đổi: ")
    #                 check_number = False
    #                 check_string = False
    #                 for i in range(len(score)):
    #                     if score[0] == '-':
    #                         continue
    #                     if score[i].isdigit() == False:
    #                         check_string = True
    #                         print("Có lỗi xảy ra, vui lòng nhập điểm là chữ số!")
    #                         break

    #                 if check_string == False:
    #                     score_float = float(score)
    #                     if score_float < -1 or score_float > 10:
    #                         print("Điểm thi không hợp lệ, vui lòng nhập lại!")
    #                         check_number = True

    #         if check == True:
    #             print("Số báo danh không hợp lệ, vui lòng nhập lại")
    #     crud_instance.update_score(sbd_input, subject_input, score_float)
    #     print(f"Cập nhật điểm thi môn {subject_input} thí sinh {sbd_input} thành công!")

    # elif choose == 4:
    #     check = True
    #     sbd_input = ""
    #     while check:
    #         sbd_input = input("Nhập số báo danh: ")
    #         temp_list = crud_instance.read_score()
    #         for row in temp_list:
    #             if sbd_input == row[0]:
    #                 check = False
    #                 break
    #         if check:
    #             print("Số báo danh không hợp lệ, vui lòng nhập lại!")
    #     print(f"Xóa thông tin thí sinh {sbd_input} thành công!")
    #     crud_instance.delete_score(sbd_input)

    # elif choose == 5:
    #     crud_instance.avg_score()
    # elif choose == 6:
    #     crud_instance.find_top_scorer_per_group()
    elif choose == "0":
        break

    else:
        print("\nLựa chọn không hợp lệ, vui lòng đọc menu và lựa chọn lại!")
