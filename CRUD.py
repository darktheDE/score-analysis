import csv

class CRUD:
    """
    Class với các phương thức có thể thao tác với dữ liệu trên file
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.subjects = ["toan", "ngu_van", "ngoai_ngu", "vat_li", "hoa_hoc", "sinh_hoc", "lich_su", "dia_li", "gdcd"]
        self.province_code = {"02": "TP. Hồ Chí Minh"}
        self.groups = {
            "A00": ["toan", "vat_li", "hoa_hoc"],
            "A02": ["toan", "vat_li", "sinh_hoc"],
            "B00": ["toan", "hoa_hoc", "sinh_hoc"],
            "C00": ["ngu_van", "lich_su", "dia_li"],
            "C19": ["ngu_van", "lich_su", "gdcd"],
            "C20": ["ngu_van", "dia_li", "gdcd"]
        }
        self.convert = {"toan":"toán", "ngu_van" : "ngữ văn", "ngoai_ngu": "ngoại ngữ", "vat_li":"vật lí", "hoa_hoc": "hóa học",
                        "sinh_hoc":"sinh học", "lich_su":"lịch sử","dia_li": "địa lí", "gdcd": "giáo dục công dân"
        }

    def add_score(self, sbd, scores):
        """
        Hàm thêm điểm cho một thí sinh mới

        Args:
            sbd(string): Số báo danh cho thí sinh cần thêm
            scores(dictionary): Chứa các item với key là tên môn thi và value là điểm thi
        """
        scores_list = [scores.get(subject) for subject in self.subjects]
        with open(self.file_path, mode = 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            row = [sbd] + scores_list
            writer.writerow(row)


    def read_score(self): 
        """
        Hàm đọc dữ liệu điểm thi từ file csv

        Args:
            (none)
        
        Returns:
            list: chứa danh sách các dòng dữ liệu được đọc từ file
        """
        scores  = []
        with open(self.file_path, mode = 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                sbd = row[0]
                score_dict = {}
                j = 1
                for subject in self.subjects:
                    score_dict[subject] = row[j]
                    j+=1
                scores.append((sbd, score_dict))
        return scores
    

    def update_score(self, sbd, subject, new_score):
        """
        Hàm cập nhật điểm thi cho một thí sinh dựa vào số báo danh của thí sinh đó

        Args:
            sbd(string): Số báo danh của thí sinh cần cập nhật điểm thi
            subject(string): Tên môn học cần sửa đổi điểm
            new_score(float): Điểm thi mới cần cập nhật cho môn học đó
        """
        data = []
        with open(self.file_path, mode = 'r', newline = '') as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)
        with open(self.file_path, mode = 'w', newline = '') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data[0])
            for row in data[1:]:
                if row[0] == sbd:
                    if subject in self.subjects:
                        index_update = self.subjects.index(subject) + 1
                        row[index_update] = new_score
                        writer.writerow(row)
                else:
                    writer.writerow(row)


    def delete_score(self, sbd):
        """
        Hàm xoá toàn bộ điểm thi dựa vào số báo danh của thí sinh đó

        Args:
            sbd(string): Số báo danh của thí sinh cần xoá điểm thi
        """
        data = []
        with open(self.file_path, mode = 'r', newline = '') as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)
        with open(self.file_path, mode = 'w', newline = '') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data[0])
            for row in data[1:]:
                if row[0] != sbd:
                    writer.writerow(row)


    def find_top_scorer_per_group(self):
        """
        Hàm tìm thủ khoa TPHCM cho từng khối thi

        Args:
            (none)
        """
        with open(self.file_path, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            # Lấy hàng tiêu đề và trỏ qua dòng tiếp theo
            header = next(reader)
            header = list(header)
            # Tạo list data chứa các dòng dữ liệu
            data = list(reader)


        # Duyệt qua từng khối thi
        for group, group_subjects in self.groups.items():
            # SBD của thủ khoa
            top_scorer = None
            # Điểm của thủ khoa
            max_score = -1
            # Dict chứa các item với key là môn thi và value là điểm thi của môn đó
            top_scores = {}
            
            for row in data:
                total_score = 0
                count_score = 0
                # Duyệt qua các môn thi trong khối thi đó
                for subject in group_subjects:
                    for j in range (len(header)):
                        # Nếu môn thi đó có trong header và điểm thi môn đó của thi sinh khác rỗng
                        if subject == header[j] and row[j] != '':
                            total_score += float(row[j])
                            count_score += 1

                # Kiểm tra nếu điểm thi của thí sinh khối đó cao hơn thủ khoa khối đó hiện tại -> cập nhật thủ khoa mới
                if total_score > max_score and count_score == len(group_subjects):
                    max_score = total_score
                    top_scorer = row[0]
                    for subject in group_subjects:
                        if subject in header and row[header.index(subject) != '']:
                            # Thêm môn đó vào dict chứa các item với key là điểm thi 1 môn trong khối và value là điểm thi môn đố
                            top_scores[subject] = row[header.index(subject)]

            # Nếu tồn tại thủ khoa khối đó -> In ra màn hình
            if top_scorer:
                scores_str = ', '.join([f"{subject}: {top_scores.get(subject, 'N/A')}" for subject in group_subjects])
                print(f"Thủ khoa khối {group}: SBD: {top_scorer}, Tổng điểm: {max_score:.2f}, Điểm chi tiết: {scores_str}")
                
    def sort_by_subject(self, subject, reversed):
        """
        Hàm sắp xếp danh sách thí sinh theo điểm tăng dần của một môn học và in ra toàn bộ thông tin

        Args:
            subject (string): Tên môn học để sắp xếp
            reversed(boolean): Biến để xác định sắp xếp tăng dần hay giảm dần
        """
        if subject not in self.subjects:
            print(f"Môn học '{subject}' không hợp lệ. Vui lòng chọn trong danh sách: {self.subjects}")
            return

        with open(self.file_path, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            data = list(reader)

        # Lấy index của môn học cần sắp xếp
        subject_index = self.subjects.index(subject) + 1

        sorted_data = sorted(data, key=lambda row: float(row[subject_index]) if row[subject_index] != '' else 0, reverse=reversed)

        # In kết quả sắp xếp ra màn hình
        print(f"\nDanh sách sắp xếp theo điểm môn '{self.convert[subject]}:")
        for row in sorted_data:
            print(row)
    
    def find_by_sbd(self, sbd_target):
        """
        Hàm tìm kiếm thông tin thí sinh theo số báo danh

        Args:
            sbd_target(string): Truyền vào số báo danh của thí sinh cần tìm kiếm
        """
        with open(self.file_path, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            data = list(reader)
        
        for row in data:
            if row[0] == sbd_target:
                print("\nThông tin của thí sinh cần tìm kiếm: ")
                print(row)
                return
        
        print("Không tìm thấy thông tin thí sinh với số báo danh:", sbd_target)

    
    def find(self, subject, score):
        """
        Hàm tìm kiếm thông tin các thí sinh thi môn có điểm thi bằng với điểm thi cần tìm

        Args:
            subject(string): Môn thi cần tìm:
            score(float): Điểm thi cần tìm
        """
        if subject not in self.subjects:
            print(f"Môn học '{subject}' không hợp lệ. Vui lòng chọn trong danh sách: {self.subjects}")
            return
        with open(self.file_path, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            data = list(reader)

        subject_index = self.subjects.index(subject) + 1

        print("Thông tin các thí sinh thi môn", self.convert[subject], "có điểm", score, "là:")
        check = True
        for row in data:
            if row[subject_index] != '':
                if float(row[subject_index]) == score:
                    check = False
                    print(row)
        
        if check == True:
            print("Không tìm thấy thông tin thí sinh thi môn", self.convert[subject], "có điểm", score)
