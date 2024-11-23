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


    def add_score(self, sbd ,scores, ma_ngoai_ngu):
        scores_list = [scores.get(subject) for subject in self.subjects]
        with open(self.file_path, mode = 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            row = [sbd] + scores_list + [ma_ngoai_ngu]
            writer.writerow(row)


    def read_score(self): 
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
                ma_ngoai_ngu = row[-1]
                scores.append((sbd, score_dict,ma_ngoai_ngu))
        return scores
    

    def update_score(self, sbd, subject, new_score):
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


    def avg_score(self):
        with open(self.file_path, mode = 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            # Bỏ qua dòng tiêu đề
            next(reader)
            # Tạo list data là các dòng dữ liệu
            data = [row for row in reader]

        # Tạo dict để lưu kết quả cho mỗi items với key tỉnh và value là đtb của tỉnh
        province_scores = {}

        for row in data:
            # Lấy mã tỉnh của từng thí sinh 
            province_code_key = row[0][:2]
            # Xác định tỉnh thông qua mã tỉnh
            province = self.province_code.get(province_code_key)
            score = 0
            count = 0

            for i in range(1,10):
                str(row[i])
                # Nếu điểm thi môn i khác rỗng -> tính tổng điểm / số lượng môn
                if row[i] != '':
                    score += float(row[i])
                    count+=1

            if count > 0:
                score /= count
            # Nếu tỉnh không nằm trong ds điểm từng tỉnh -> tạo value mới cho tỉnh đó là một list điểm rỗng
            if province not in province_scores:
                province_scores[province] = [] 
            # Nếu đã được tạo danh sách đtb của từng thí sinh tỉnh đó -> tiến hành thêm đtb của thí sinh kế tiếp
            province_scores[province].append(score)

        # Tạo dict chứa các item với key là tên tình và value là đtb của từng tỉnh
        avg_by_province = {province: sum(scores) / len(scores) for province, scores in province_scores.items()}
        print("\nĐiểm trung bình từng tỉnh thành:")
        for province, avg_score in avg_by_province.items():
            print(f"{province}: {avg_score:.2f}")


    def find_top_scorer_per_group(self):
        with open(self.file_path, mode='r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            # Lấy hàng tiêu đề và trỏ qua dòng tiếp theo
            header = next(reader)
            header = list(header)
            # Tạo list data chứa các dòng dữ liệu
            data = [row for row in reader]


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
