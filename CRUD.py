import csv

class CRUD:
    def __init__(self, file_path):
        self.file_path = file_path
        self.subjects = ["toan", "ngu_van", "ngoai_ngu", "li", "hoa", "sinh", "lich_su", "dia_ly", "gdcd"]

    def add_score(self, sbd ,scores):
        # giả sử ban đầu file csv chỉ có header cho cột và hàng là sbd và tên của từng môn học
        scores_list = [scores.get(subject) for subject in self.subjects] # làm khóa chính để truy cập đến điểm của từng môn
        with open(self.file_path, mode = 'a', newline='') as csv_file:
            # viết thêm vào file csv mode a = mode append
            writer = csv.writer(csv_file)
            row = [sbd] + scores_list
            writer.writerow(row) # viết thêm dòng mới vào

    def read_score(self): 
        scores  = []
        with open(self.file_path, mode = 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader) # bo qua dong dau tien, vi dong nay chi chua tieu de
            for row in reader:
                sbd = row[0] # row[i] tức là duyệt qua các phần tử thứ i trong file csv trên từng dòng
                score_dict = {}
                j = 1
                for subject in self.subjects:
                    score_dict[subject] = row[j] # gán điểm cho từng môn theo từng khóa chính
                    j+=1
                scores.append((sbd, score_dict))
        return scores
    
    def update_score(self, sbd, subject, new_score): # cap nhat diem cua mot mon hoc cu the
        data = []
        with open(self.file_path, mode = 'r', newline = '') as csv_file:
            reader = csv.reader(csv_file) #csv.reader chi tra ve iterator 
            data = list(reader) # chuyển file csv thành 1 list các phần tử mà mỗi phần tử chính là 1 dòng
        with open(self.file_path, mode = 'w', newline = '') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data[0]) # ghi lại dòng chứa tiêu đề vào file mới
            for row in data[1:]:
                if row[0] == sbd: # neu row[0] bang sbd can cap nhat diem thi cap nhat lai diem
                    if subject in self.subjects:
                        index_update = self.subjects.index(subject) + 1 # lấy chỉ số của môn cần cập nhật (cần cộng thêm 1 vì khóa chính không chứa cột sbd)
                        row[index_update] = new_score
                        writer.writerow(row)
                else:
                    # nếu row[0] không khớp với sbd, ghi dòng đó lại vào file mà không thay đổi.
                    writer.writerow(row)

    def delete_score(self, sbd): # xoa hoc sinh theo sbd
        data = []
        with open(self.file_path, mode = 'r', newline = '') as csv_file: # doc du lieu du file vao
            reader = csv.reader(csv_file)
            data = list(reader)
        with open(self.file_path, mode = 'w', newline = '') as csv_file: # ghi de du lieu vao trong file
            writer = csv.writer(csv_file)
            writer.writerow(data[0]) # ghi lại dòng chứa tiêu đề vào file mới
            for row in data[1:]:
                if row[0] != sbd:
                    writer.writerow(row)

# # code test mẫu
# choose = -1
# file_path = "Project\diem_hoc_sinh_test.csv"
# crud_instance = crud(file_path)

# while(choose != 0):
#     print("\nMENU OPTIONS")
#     print("1. Nhập điểm thi cho một thí sinh mới")
#     print("2. Đọc dữ liệu điểm thi từ file dữ liệu và xuất ra màn hình")
#     print("3. Cập nhật điểm thi thông qua số báo danh của một thí sinh")
#     print("4. Xóa dữ liệu của một thí sinh thông qua số báo danh")
#     print("0. Thoát chương trình")
#     choose = int(input("Nhập lựa chọn của bạn: "))

#     if choose == 1:
#         sbd_input = int(input("Nhập số báo danh: "))
#         scores_input = {}
#         for subject in crud_instance.subjects:
#             score = -1.0
#             while(score < 0):
#                 score = float(input(f"Nhập điểm thi môn {subject}: "))
#                 if score < 0 or score > 10:
#                     print("Điểm thi không hợp lệ, vui lòng nhập lại!")
#                 else:
#                     scores_input[subject] = score
#         crud_instance.add_score(sbd_input, scores_input)
#         print("Thêm dữ liệu cho thí sinh mới thành công!")

#     elif choose == 2:
#         print("Dữ liệu trong file đã được đọc thành công!")
#         temp_list = crud_instance.read_score()
#         for row in temp_list:
#             print(row)

#     elif choose == 3:
#         sbd_input = ""
#         check = True
#         while check:
#             sbd_input = input("Nhập số báo danh: ")
#             temp_list = crud_instance.read_score()
#             for row in temp_list:
#                 if sbd_input == row[0]:
#                     check = False
#                     break
#             if check:
#                 print("Số báo danh không hợp lệ, vui lòng nhập lại!")
#         subject_input = input("Nhập tên môn học cần cập nhật: ")
#         new_score_input = -1.0
#         while new_score_input < 0:
#             new_score_input = float(input("Nhập điểm thi mới cần thay đổi: "))
#             if new_score_input < 0 or new_score_input > 10:
#                 print("Điểm thi không hợp lệ, vui lòng nhập lại!")
#         crud_instance.update_score(sbd_input, subject_input, new_score_input)
#         print(f"Cập nhật điểm thi môn {subject_input} thí sinh {sbd_input} thành công!")

#     elif choose == 4:
#         check = True
#         sbd_input = ""
#         while check:
#             sbd_input = input("Nhập số báo danh: ")
#             temp_list = crud_instance.read_score()
#             for row in temp_list:
#                 if sbd_input == row[0]:
#                     check = False
#                     break
#             if check:
#                 print("Số báo danh không hợp lệ, vui lòng nhập lại!")
#         print(f"Xóa thông tin thí sinh {sbd_input} thành công!")
#         crud_instance.delete_score(sbd_input)

#     if(choose == 0):
#         pass

#     else:
#         print("Lựa chọn không hợp lệ, vui lòng đọc menu và lựa chọn lại!")
                