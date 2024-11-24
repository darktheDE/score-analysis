"""
data_visualization.py
Module chứa các hàm để trực quan hóa dữ liệu điểm thi, bao gồm việc hiển thị phổ điểm của từng môn học, tổ hợp môn, và so sánh giữa các tổ hợp.
"""

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
data2023 = pd.read_csv("diem2023.csv")
data2024 = pd.read_csv("diem2024.csv")

# Điền giá trị 0 cho các ô trống
data2023.fillna(0, inplace=True)
data2024.fillna(0, inplace=True)


# Hàm vẽ phổ điểm cho một môn học cụ thể
def plot_score_distribution_by_subject(data, subject):
    """
    Vẽ biểu đồ phổ điểm cho một môn học cụ thể.

    Args:
        data (pd.DataFrame): Dữ liệu điểm thi với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        subject (str): Tên môn học cần vẽ biểu đồ.

    Returns:
        None: Hiển thị biểu đồ histogram trực tiếp.

    Raises:
        ValueError: Nếu môn học không có trong cột của DataFrame.
    """
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
    plt.hist(
        data[subject],
        bins=[x * 0.5 for x in range(21)],
        edgecolor="black",
        color="lightcoral",
    )
    plt.xlabel("Điểm")
    plt.ylabel("Số lượng thí sinh")
    plt.title(f"Phổ điểm môn {subject.capitalize()}")
    plt.xticks([x * 0.5 for x in range(21)])

    # Hiển thị thông tin thống kê bên phải biểu đồ
    plt.figtext(
        0.75, 0.8, f"Điểm cao nhất: {max_score} (Số học sinh: {max_count})", ha="left"
    )
    plt.figtext(
        0.75, 0.75, f"Điểm thấp nhất: {min_score} (Số học sinh: {min_count})", ha="left"
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
    """
    Vẽ biểu đồ phổ điểm cho một tổ hợp môn cụ thể.

    Args:
        data (pd.DataFrame): Dữ liệu điểm thi với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        combination_code (str): Mã tổ hợp môn (ví dụ: "A01", "C00") để tính tổng điểm tổ hợp.

    Returns:
        None: Hiển thị biểu đồ histogram trực tiếp.

    Raises:
        ValueError: Nếu mã tổ hợp không hợp lệ.
    """
    if combination_code not in subject_combinations:
        print(f"Mã tổ hợp {combination_code} không hợp lệ.")
        return

    subjects = subject_combinations[combination_code]

    # Tính điểm tổ hợp, bỏ qua các môn có điểm 0
    data["combination_score"] = (
        data[subjects].replace(0, pd.NA).sum(axis=1, skipna=True)
    )

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
    plt.hist(
        data["combination_score"], bins=range(0, 31), edgecolor="black", color="skyblue"
    )
    plt.xlabel("Điểm")
    plt.ylabel("Số lượng thí sinh")
    plt.title(f"Phổ điểm tổ hợp {combination_code} ({', '.join(subjects)})")
    plt.xticks(range(0, 31))

    # Hiển thị thông tin thống kê bên phải biểu đồ
    plt.figtext(
        0.75, 0.8, f"Điểm cao nhất: {max_score} (Số học sinh: {max_count})", ha="left"
    )
    plt.figtext(
        0.75, 0.75, f"Điểm thấp nhất: {min_score} (Số học sinh: {min_count})", ha="left"
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


def plot_score_distribution_pie(data, combination_code):
    """
    Vẽ biểu đồ tròn thể hiện tỷ lệ học sinh thuộc các nhóm điểm của một tổ hợp môn.

    Args:
        data (pd.DataFrame): Dữ liệu điểm thi với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        combination_code (str): Mã tổ hợp môn (ví dụ: "A01", "C00") để tính tổng điểm tổ hợp.

    Returns:
        None: Hiển thị biểu đồ tròn trực tiếp.

    Raises:
        ValueError: Nếu mã tổ hợp không hợp lệ.
    """
    subjects = subject_combinations[combination_code]
    data["combination_score"] = (
        data[subjects].replace(0, pd.NA).sum(axis=1, skipna=True)
    )
    bins = [0, 15, 24, 30]
    labels = ["< 15", "15 - 24", ">= 24"]
    data["score_group"] = pd.cut(
        data["combination_score"], bins=bins, labels=labels, include_lowest=True
    )
    group_counts = data["score_group"].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(
        group_counts,
        labels=group_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["red", "yellow", "green"],
    )
    plt.title(f"Tỷ lệ học sinh theo mức điểm tổ hợp {combination_code}")
    plt.show()


def plot_score_distribution_by_combinations(data, subject_combinations):
    """
    Vẽ biểu đồ cột nhóm so sánh điểm cao nhất và thấp nhất giữa các tổ hợp môn.

    Args:
        data (pd.DataFrame): Dữ liệu điểm thi với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        subject_combinations (dict): Dictionary chứa mã tổ hợp môn và danh sách các môn học tương ứng.

    Returns:
        None: Hiển thị biểu đồ cột trực tiếp.
    """
    # Tạo dictionary lưu điểm cao nhất và thấp nhất
    combination_scores = {"Combination": [], "Max Score": [], "Min Score": []}

    # Tính điểm cao nhất và thấp nhất cho từng tổ hợp
    for combination, subjects in subject_combinations.items():
        # Tính tổng điểm tổ hợp
        data["combination_score"] = (
            data[subjects].replace(0, pd.NA).sum(axis=1, skipna=True)
        )

        # Lấy điểm cao nhất và thấp nhất
        max_score = data["combination_score"].max()
        min_score = data["combination_score"].min()

        # Lưu kết quả vào dictionary
        combination_scores["Combination"].append(combination)
        combination_scores["Max Score"].append(max_score)
        combination_scores["Min Score"].append(min_score)

    # Chuyển dictionary thành DataFrame
    scores_df = pd.DataFrame(combination_scores)

    # Vẽ biểu đồ cột nhóm
    plt.figure(figsize=(16, 8))
    bar_width = 0.35
    x = range(len(scores_df))

    # Vẽ cột Max Score
    plt.bar(
        x,
        scores_df["Max Score"],
        width=bar_width,
        label="Điểm cao nhất",
        color="skyblue",
    )

    # Vẽ cột Min Score
    plt.bar(
        [i + bar_width for i in x],
        scores_df["Min Score"],
        width=bar_width,
        label="Điểm thấp nhất",
        color="salmon",
    )

    # Thiết lập trục và nhãn
    plt.xlabel("Tổ hợp môn", fontsize=12)
    plt.ylabel("Điểm", fontsize=12)
    plt.title("Phân phối điểm cao/thấp giữa các tổ hợp", fontsize=16)
    plt.xticks([i + bar_width / 2 for i in x], scores_df["Combination"], rotation=45)
    plt.legend()

    # Hiển thị biểu đồ
    plt.tight_layout()
    plt.show()


# Ví dụ gọi hàm
# plot_score_distribution_by_combination(data2024, "A01")

# plot_score_distribution_by_subject(data2024, "ngu_van")

# plot_score_distribution_pie(data2023, "A01")

# plot_score_distribution_by_combinations(data2023, subject_combinations)
