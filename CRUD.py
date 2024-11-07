import csv

class CRUD:
    def __init__(self, file_path):
        self.file_path = file_path
        self.subjects = ["toan", "ngu_van", "ngoai_ngu", "vat_li", "hoa_hoc", "sinh_hoc", "lich_su", "dia_li", "gdcd"]
        self.province_code = {
            "01": "Hà Nội",
            "02": "TP. Hồ Chí Minh",
            "03": "Hải Phòng",
            "04": "Đà Nẵng",
            "05": "Hà Giang",
            "06": "Cao Bằng",
            "07": "Lai Châu",
            "08": "Lào Cai",
            "09": "Tuyên Quang",
            "10": "Lạng Sơn",
            "11": "Bắc Kạn",
            "12": "Thái Nguyên",
            "13": "Yên Bái",
            "14": "Sơn La",
            "15": "Phú Thọ",
            "16": "Vĩnh Phúc",
            "17": "Quảng Ninh",
            "18": "Bắc Giang",
            "19": "Bắc Ninh",
            "21": "Hải Dương",
            "22": "Hưng Yên",
            "23": "Hòa Bình",
            "24": "Hà Nam",
            "25": "Nam Định",
            "26": "Thái Bình",
            "27": "Ninh Bình",
            "28": "Thanh Hóa",
            "29": "Nghệ An",
            "30": "Hà Tĩnh",
            "31": "Quảng Bình",
            "32": "Quảng Trị",
            "33": "Thừa Thiên Huế",
            "34": "Quảng Nam",
            "35": "Quảng Ngãi",
            "36": "Kon Tum",
            "37": "Bình Định",
            "38": "Gia Lai",
            "39": "Phú Yên",
            "40": "Đắk Lắk",
            "41": "Khánh Hòa",
            "42": "Lâm Đồng",
            "43": "Bình Phước",
            "44": "Bình Dương",
            "45": "Ninh Thuận",
            "46": "Tây Ninh",
            "47": "Bình Thuận",
            "48": "Đồng Nai",
            "49": "Long An",
            "50": "Đồng Tháp",
            "51": "An Giang",
            "52": "Bà Rịa - Vũng Tàu",
            "53": "Tiền Giang",
            "54": "Kiên Giang",
            "55": "Cần Thơ",
            "56": "Bến Tre",
            "57": "Vĩnh Long",
            "58": "Trà Vinh",
            "59": "Sóc Trăng",
            "60": "Bạc Liêu",
            "61": "Cà Mau",
            "62": "Điện Biên",
            "63": "Đắk Nông",
            "64": "Hậu Giang"
        }
        self.groups = {
            "A00": ["toan", "vat_li", "hoa_hoc"],
            "A01": ["toan", "vat_li", "ngoai_ngu"],
            "B00": ["toan", "hoa_hoc", "sinh_hoc"],
            "C00": ["ngu_van", "lich_su", "dia_li"],
            "D01": ["ngu_van", "toan", "ngoai_ngu"],
        }
    def add_score(self, sbd ,scores,ma_ngoai_ngu):
        # giả sử ban đầu file csv chỉ có header cho cột và hàng là sbd và tên của từng môn học
        scores_list = [scores.get(subject) for subject in self.subjects] # làm khóa chính để truy cập đến điểm của từng môn
        with open(self.file_path, mode = 'a', newline='') as csv_file:
            # viết thêm vào file csv mode a = mode append
            writer = csv.writer(csv_file)
            row = [sbd] + scores_list + [ma_ngoai_ngu]
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
                ma_ngoai_ngu = row[-1]
                scores.append((sbd, score_dict,ma_ngoai_ngu))
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

    def avg_score(self):
        with open(self.file_path, mode = 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            data = [row for row in reader]
        province_scores = {}
        for row in data:
            province_code_key = row[0][:2]
            province = self.province_code.get(province_code_key)
            score = 0
            count = 0
            for i in range(1,10,1):
                str(row[i])
                if row[i] != '':
                    score += float(row[i])
                    count+=1
            if count > 0:
                score /= count
            if province not in province_scores:
                province_scores[province] = []
            province_scores[province].append(score)
        avg_by_province = {province: sum(scores) / len(scores) for province, scores in province_scores.items()}
        print("\nĐiểm trung bình từng tỉnh thành:")
        for province, avg_score in avg_by_province.items():
            print(f"{province}: {avg_score:.2f}")

    def find_top_scorer_per_group(self):
        with open(self.file_path, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
            header = list(header)
            data = [row for row in reader]
        for group, subjects in self.groups.items():
            top_scorer = None
            max_score = -1
            top_scores = {}
            
            for row in data:
                # Tính tổng điểm của từng khối
                total_score = 0
                count_score = 0
                for var in subjects:
                    for j in range (len(header)):
                        if var == header[j] and row[j] != '':
                            total_score += float(row[j])
                            count_score+=1

                # Nếu tổng điểm cao hơn, cập nhật thông tin thủ khoa
                if total_score > max_score and count_score == len(subjects):
                    max_score = total_score
                    top_scorer = row[0]
                    top_scores = {
                        subject: row[header.index(subject)]
                        for subject in subjects if subject in header and row[header.index(subject)] != ''
                    }

            # In kết quả của thủ khoa
            if top_scorer:
                scores_str = ', '.join([f"{subject}: {top_scores.get(subject, 'N/A')}" for subject in subjects])
                print(f"Thủ khoa khối {group}: SBD: {top_scorer}, Tổng điểm: {max_score:.2f}, Điểm chi tiết: {scores_str}")

test = CRUD("diem_thi_thpt_2024_QG.csv")
# test.avg_score()
test.find_top_scorer_per_group()
