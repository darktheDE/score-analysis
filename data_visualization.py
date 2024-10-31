import pandas as pd
import matplotlib.pyplot as plt

# Dữ liệu tổ hợp môn theo khối
subject_combinations = {
    "A00": ["toan", "li", "hoa"],
    "A01": ["toan", "li", "ngoai_ngu"],
    "A02": ["toan", "li", "sinh"],
    "A03": ["toan", "li", "lich_su"],
    "A04": ["toan", "li", "dia_ly"],
    "A05": ["toan", "hoa", "lich_su"],
    "A06": ["toan", "hoa", "dia_ly"],
    "A07": ["toan", "lich_su", "dia_ly"],
    "A08": ["toan", "lich_su", "gdcd"],
    "A09": ["toan", "dia_ly", "gdcd"],
    "A10": ["toan", "li", "gdcd"],
    "A11": ["toan", "hoa", "gdcd"],
    "A14": ["toan", "sinh", "dia_ly"],
    "A15": ["toan", "sinh", "gdcd"],
    "A16": ["toan", "li", "van"],
    "B00": ["toan", "hoa", "sinh"],
    "B01": ["toan", "sinh", "lich_su"],
    "B02": ["toan", "sinh", "dia_ly"],
    "B03": ["toan", "sinh", "van"],
    "B04": ["toan", "sinh", "gdcd"],
    "B08": ["toan", "sinh", "ngoai_ngu"],
    "C00": ["ngu_van", "lich_su", "dia_ly"],
    "C01": ["ngu_van", "toan", "li"],
    "C02": ["ngu_van", "toan", "hoa"],
    "C03": ["ngu_van", "toan", "lich_su"],
    "C04": ["ngu_van", "toan", "dia_ly"],
    "C05": ["ngu_van", "li", "hoa"],
    "C06": ["ngu_van", "li", "sinh"],
    "C07": ["ngu_van", "li", "lich_su"],
    "C08": ["ngu_van", "hoa", "sinh"],
    "C09": ["ngu_van", "li", "dia_ly"],
    "C10": ["ngu_van", "hoa", "lich_su"],
    "C12": ["ngu_van", "sinh", "lich_su"],
    "C13": ["ngu_van", "sinh", "dia_ly"],
    "C14": ["ngu_van", "toan", "gdcd"],
    "C16": ["ngu_van", "li", "gdcd"],
    "C17": ["ngu_van", "hoa", "gdcd"],
    "C19": ["ngu_van", "lich_su", "gdcd"],
    "C20": ["ngu_van", "dia_ly", "gdcd"],
    "D01": ["ngu_van", "toan", "ngoai_ngu"],
    "D07": ["toan", "hoa", "ngoai_ngu"],
    "D08": ["toan", "sinh", "ngoai_ngu"],
    "D09": ["toan", "lich_su", "ngoai_ngu"],
    "D10": ["toan", "dia_ly", "ngoai_ngu"],
    "D11": ["ngu_van", "li", "ngoai_ngu"],
    "D12": ["ngu_van", "hoa", "ngoai_ngu"],
    "D13": ["ngu_van", "sinh", "ngoai_ngu"],
    "D14": ["ngu_van", "lich_su", "ngoai_ngu"],
    "D15": ["ngu_van", "dia_ly", "ngoai_ngu"],
    "D66": ["ngu_van", "gdcd", "ngoai_ngu"],
    "D84": ["toan", "gdcd", "ngoai_ngu"],
}

# Bước 1: Đọc dữ liệu từ file CSV
data = pd.read_csv("diem_hoc_sinh_test.csv")


# Hàm vẽ phổ điểm cho một môn học cụ thể
def plot_score_distribution_by_subject(data, subject):
    if subject not in data.columns[1:]:  # Kiểm tra xem môn học có hợp lệ không
        print(f"Môn học {subject} không hợp lệ.")
        return

    # Thống kê
    max_score = data[subject].max()
    max_sbd = data[data[subject] == max_score]["sbd"].tolist()
    min_score = data[subject].min()
    min_sbd = data[data[subject] == min_score]["sbd"].tolist()
    avg_score = data[subject].mean()
    median_score = data[subject].median()
    mode_score = data[subject].mode().values[0]
    total_students = len(data)
    below_1 = len(data[data[subject] < 1])
    below_5 = len(data[data[subject] < 5])

    # Tạo biểu đồ
    plt.figure(figsize=(12, 6))
    plt.hist(data[subject], bins=range(0, 11), edgecolor="black", color="lightcoral")
    plt.xlabel("Điểm")
    plt.ylabel("Số lượng thí sinh")
    plt.title(f"Phổ điểm môn {subject.capitalize()}")
    plt.xticks(range(0, 11))

    # Hiển thị thông tin thống kê bên phải biểu đồ
    plt.figtext(
        0.75,
        0.8,
        f"Điểm cao nhất: {max_score} (SBD: {', '.join(map(str, max_sbd))})",
        ha="left",
    )
    plt.figtext(
        0.75,
        0.75,
        f"Điểm thấp nhất: {min_score} (SBD: {', '.join(map(str, min_sbd))})",
        ha="left",
    )
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
    # Kiểm tra mã tổ hợp có hợp lệ không
    if combination_code not in subject_combinations:
        print(f"Mã tổ hợp {combination_code} không hợp lệ.")
        return

    subjects = subject_combinations[combination_code]

    # Tính điểm tổ hợp
    data["combination_score"] = data[subjects].sum(axis=1)

    # Thống kê
    max_score = data["combination_score"].max()
    max_sbd = data[data["combination_score"] == max_score]["sbd"].tolist()
    min_score = data["combination_score"].min()
    min_sbd = data[data["combination_score"] == min_score]["sbd"].tolist()
    avg_score = data["combination_score"].mean()
    median_score = data["combination_score"].median()
    mode_score = data["combination_score"].mode().values[0]
    total_students = len(data)
    below_1 = len(data[data["combination_score"] < 1])
    below_5 = len(data[data["combination_score"] < 5])

    # Tạo biểu đồ
    plt.figure(figsize=(12, 6))
    plt.hist(
        data["combination_score"], bins=range(0, 31), edgecolor="black", color="skyblue"
    )
    plt.xlabel("Điểm")
    plt.ylabel("Số lượng thí sinh")
    plt.title(f"Phổ điểm tổ hợp {combination_code} ({' - '.join(subjects)})")
    plt.xticks(range(0, 31))

    # Hiển thị thông tin thống kê bên phải biểu đồ
    plt.figtext(
        0.75,
        0.8,
        f"Điểm cao nhất: {max_score} (SBD: {', '.join(map(str, max_sbd))})",
        ha="left",
    )
    plt.figtext(
        0.75,
        0.75,
        f"Điểm thấp nhất: {min_score} (SBD: {', '.join(map(str, min_sbd))})",
        ha="left",
    )
    plt.figtext(0.75, 0.7, f"Điểm trung bình: {avg_score:.2f}", ha="left")
    plt.figtext(0.75, 0.65, f"Điểm trung vị: {median_score}", ha="left")
    plt.figtext(0.75, 0.6, f"Điểm phổ biến nhất: {mode_score}", ha="left")
    plt.figtext(0.75, 0.55, f"Tổng số học sinh: {total_students}", ha="left")
    plt.figtext(0.75, 0.5, f"Số học sinh có điểm < 1: {below_1}", ha="left")
    plt.figtext(0.75, 0.45, f"Số học sinh có điểm < 5: {below_5}", ha="left")

    # Cân chỉnh layout để không bị chồng chéo
    plt.tight_layout(rect=[0, 0, 0.7, 1])
    plt.show()


# Gọi hàm để vẽ biểu đồ cho mã tổ hợp A00
plot_score_distribution_by_combination(data, "A01")


# Ví dụ gọi hàm:
# Vẽ phổ điểm cho một môn học (ví dụ: "toan")
plot_score_distribution_by_subject(data, "ngu_van")