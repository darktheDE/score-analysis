import csv

class crud:
    def __init__(self,file_path):
        self.file_path = file_path
        self.subjects = ["toan", "ngu_van", "ngoai_ngu", "li", "hoa", "sinh", "lich_su", "dia_ly", "gdcd"]

    def add_score(self,sbd,scores):
        scores_list = [scores.get(subject) for subject in self.subjects]
        with open(self.file_path, mode = 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            row = [sbd] + scores_list
            writer.writerow(row)
    def read_score(self): 
        scores  = []
        with open(self.file_path, mode = 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            next(reader) # bo qua dong dau tien, vi dong nay chi chua tieu de
            for row in reader:
                sbd = row[0]
                score_dict = {}
                j = 1
                for subject in self.subjects:
                    score_dict[subject] = row[j]
                    j+=1

                scores.append(sbd,score_dict)
        return scores
    def update_score(self, sbd, subject, new_score): # cap nhat diem cua mot mon hoc cu the
        data = []
        with open(self.file_path, mode = 'r', newline = '') as csv_file:
            reader = csv.reader(csv_file) #csv.reader chi tra ve iterator 
            data = list(reader)
        with open(self.file_path, mode = 'w', newline = '') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data[0]) # ghi vao dong chua tieu de
            for row in data[1:]:
                if row[0] == sbd: # neu row[0] bang sbd can cap nhat diem thi cap nhat lai diem
                    if subject in self.subjects:
                        index_update = self.subjects.index(subject) + 1
                        row[index_update] = new_score
                        writer.writerow(row)
                else:
                    writer.writerow(row)
    def delete_score(self, sbd): # xoa hoc sinh theo sbd
        data = []
        with open(self.file_path, mode = 'r', newline = '') as csv_file: # doc du lieu du file vao
            reader = csv.reader(csv_file)
            data = list(reader)
        with open(self.file_path, mode = 'w', newline = '') as csv_file: # ghi de du lieu vao trong file
            writer = csv.writer(csv_file)
            writer.writerow(data[0]) # ghi vao tieu de
            for row in data[1:]:
                if row[0] != sbd:
                    writer.writerow(row)
