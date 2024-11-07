# data_visualization.py
import pandas as pd
import matplotlib.pyplot as plt

# Dữ liệu tổ hợp môn theo khối cụ thể (đã sửa tên các môn học)
subject_combinations = {
    "A00": ["toan", "vat_li", "hoa_hoc"],
    "A01": ["toan", "vat_li", "ngoai_ngu"],
    "A02": ["toan", "vat_li", "sinh_hoc"],
    "A03": ["toan", "vat_li", "lich_su"],
    "A04": ["toan", "vat_li", "dia_li"],
    "A05": ["toan", "hoa_hoc", "lich_su"],
    "A06": ["toan", "hoa_hoc", "dia_li"],
    "A07": ["toan", "lich_su", "dia_li"],
    "A08": ["toan", "lich_su", "gdcd"],
    "A09": ["toan", "dia_li", "gdcd"],
    "A10": ["toan", "vat_li", "gdcd"],
    "A11": ["toan", "hoa_hoc", "gdcd"],
    "A14": ["toan", "sinh_hoc", "dia_li"],
    "A15": ["toan", "sinh_hoc", "gdcd"],
    "A16": ["toan", "vat_li", "ngu_van"],
    "B00": ["toan", "hoa_hoc", "sinh_hoc"],
    "B01": ["toan", "sinh_hoc", "lich_su"],
    "B02": ["toan", "sinh_hoc", "dia_li"],
    "B03": ["toan", "sinh_hoc", "ngu_van"],
    "B04": ["toan", "sinh_hoc", "gdcd"],
    "B08": ["toan", "sinh_hoc", "ngoai_ngu"],
    "C00": ["ngu_van", "lich_su", "dia_li"],
    "C01": ["ngu_van", "toan", "vat_li"],
    "C02": ["ngu_van", "toan", "hoa_hoc"],
    "C03": ["ngu_van", "toan", "lich_su"],
    "C04": ["ngu_van", "toan", "dia_li"],
    "C05": ["ngu_van", "vat_li", "hoa_hoc"],
    "C06": ["ngu_van", "vat_li", "sinh_hoc"],
    "C07": ["ngu_van", "vat_li", "lich_su"],
    "C08": ["ngu_van", "hoa_hoc", "sinh_hoc"],
    "C09": ["ngu_van", "vat_li", "dia_li"],
    "C10": ["ngu_van", "hoa_hoc", "lich_su"],
    "C12": ["ngu_van", "sinh_hoc", "lich_su"],
    "C13": ["ngu_van", "sinh_hoc", "dia_li"],
    "C14": ["ngu_van", "toan", "gdcd"],
    "C16": ["ngu_van", "vat_li", "gdcd"],
    "C17": ["ngu_van", "hoa_hoc", "gdcd"],
    "C19": ["ngu_van", "lich_su", "gdcd"],
    "C20": ["ngu_van", "dia_li", "gdcd"],
    "D01": ["ngu_van", "toan", "ngoai_ngu"],
    "D07": ["toan", "hoa_hoc", "ngoai_ngu"],
    "D08": ["toan", "sinh_hoc", "ngoai_ngu"],
    "D09": ["toan", "lich_su", "ngoai_ngu"],
    "D10": ["toan", "dia_li", "ngoai_ngu"],
    "D11": ["ngu_van", "vat_li", "ngoai_ngu"],
    "D12": ["ngu_van", "hoa_hoc", "ngoai_ngu"],
    "D13": ["ngu_van", "sinh_hoc", "ngoai_ngu"],
    "D14": ["ngu_van", "lich_su", "ngoai_ngu"],
    "D15": ["ngu_van", "dia_li", "ngoai_ngu"],
    "D66": ["ngu_van", "gdcd", "ngoai_ngu"],
    "D84": ["toan", "gdcd", "ngoai_ngu"],
}

# Đọc dữ liệu từ file CSV
data = pd.read_csv("diem_thi_thpt_2024_QG.csv")

# Điền giá trị 0 cho các ô trống
data.fillna(0, inplace=True)

# Hàm vẽ phổ điểm cho một môn học cụ thể
def plot_score_distribution_by_subject(data, subject):
    if subject not in data.columns[1:]:  # Kiểm tra xem môn học có hợp lệ không
        print(f"Môn học {subject} không hợp lệ.")
        return

    # Thống kê
    max_score = data[subject].max()
    min_score = data[subject].min()
    avg_score = data[subject].mean()
    median_score = data[subject].median()
    mode_score = data[subject].mode().values[0]
    total_students = len(data)
    below_1 = len(data[data[subject] < 1])
    below_5 = len(data[data[subject] < 5])
    max_count = len(data[data[subject] == max_score])
    min_count = len(data[data[subject] == min_score])

    # Tạo biểu đồ
    plt.figure(figsize=(12, 6))
    plt.hist(data[subject],  bins=[x * 0.5 for x in range(21)], edgecolor="black", color="lightcoral")
    plt.xlabel("Điểm")
    plt.ylabel("Số lượng thí sinh")
    plt.title(f"Phổ điểm môn {subject.capitalize()}")
    plt.xticks([x * 0.5 for x in range(21)])

    # Hiển thị thông tin thống kê bên phải biểu đồ
    plt.figtext(0.75, 0.8, f"Điểm cao nhất: {max_score} (Số học sinh: {max_count})", ha="left")
    plt.figtext(0.75, 0.75, f"Điểm thấp nhất: {min_score} (Số học sinh: {min_count})", ha="left")
    plt.figtext(0.75, 0.7, f"Điểm trung bình: {avg_score:.2f}", ha="left")
    plt.figtext(0.75, 0.65, f"Điểm trung vị: {median_score}", ha="left")
    plt.figtext(0.75, 0.6, f"Điểm phổ biến nhất: {mode_score}", ha="left")
    plt.figtext(0.75, 0.55, f"Tổng số học sinh: {total_students}", ha="left")
    plt.figtext(0.75, 0.5, f"Số học sinh có điểm < 1: {below_1}", ha="left")
    plt.figtext(0.75, 0.45, f"Số học sinh có điểm < 5: {below_5}", ha="left")

    # Cân chỉnh layout để không bị chồng chéo
    plt.tight_layout(rect=[0, 0, 0.7, 1])
    plt.show()

# Hàm vẽ biểu đồ phổ điểm theo tổ hợp
def plot_score_distribution_by_combination(data, combination_code):
    if combination_code not in subject_combinations:
        print(f"Mã tổ hợp {combination_code} không hợp lệ.")
        return

    subjects = subject_combinations[combination_code]

    # Tính điểm tổ hợp, bỏ qua các môn có điểm 0
    data["combination_score"] = data[subjects].replace(0, pd.NA).sum(axis=1, skipna=True)

    # Thống kê
    max_score = data["combination_score"].max()
    min_score = data["combination_score"].min()
    avg_score = data["combination_score"].mean()
    median_score = data["combination_score"].median()
    mode_score = data["combination_score"].mode().values[0]
    total_students = len(data)
    below_1 = len(data[data["combination_score"] < 1])
    below_5 = len(data[data["combination_score"] < 5])
    max_count = len(data[data["combination_score"] == max_score])
    min_count = len(data[data["combination_score"] == min_score])

    # Tạo biểu đồ
    plt.figure(figsize=(12, 6))
    plt.hist(data["combination_score"], bins=range(0, 31), edgecolor="black", color="skyblue")
    plt.xlabel("Điểm")
    plt.ylabel("Số lượng thí sinh")
    plt.title(f"Phổ điểm tổ hợp {combination_code} ({', '.join(subjects)})")
    plt.xticks(range(0, 31))

    # Hiển thị thông tin thống kê bên phải biểu đồ
    plt.figtext(0.75, 0.8, f"Điểm cao nhất: {max_score} (Số học sinh: {max_count})", ha="left")
    plt.figtext(0.75, 0.75, f"Điểm thấp nhất: {min_score} (Số học sinh: {min_count})", ha="left")
    plt.figtext(0.75, 0.7, f"Điểm trung bình: {avg_score:.2f}", ha="left")
    plt.figtext(0.75, 0.65, f"Điểm trung vị: {median_score}", ha="left")
    plt.figtext(0.75, 0.6, f"Điểm phổ biến nhất: {mode_score}", ha="left")
    plt.figtext(0.75, 0.55, f"Tổng số học sinh: {total_students}", ha="left")
    plt.figtext(0.75, 0.5, f"Số học sinh có điểm < 1: {below_1}", ha="left")
    plt.figtext(0.75, 0.45, f"Số học sinh có điểm < 5: {below_5}", ha="left")

    # Cân chỉnh layout để không bị chồng chéo
    plt.tight_layout(rect=[0, 0, 0.7, 1])
    plt.show()

# Ví dụ gọi hàm
plot_score_distribution_by_subject(data, "ngu_van")
plot_score_distribution_by_combination(data, "A01")
