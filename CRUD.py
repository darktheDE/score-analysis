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
    
