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
    "A02": ["toan", "vat_li", "sinh_hoc"],
    "B00": ["toan", "hoa_hoc", "sinh_hoc"],
    "C00": ["ngu_van", "lich_su", "dia_li"],
    "C19": ["ngu_van", "lich_su", "gdcd"],
    "C20": ["ngu_van", "dia_li", "gdcd"]
}

# Đọc dữ liệu từ file CSV
data2023 = pd.read_csv(r"data\diem2023.csv")
data2024 = pd.read_csv(r"data\diem2024.csv")

# Điền giá trị 0 cho các ô trống
data2023.fillna(0, inplace=True)
data2024.fillna(0, inplace=True)


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
    if subject not in data.columns:  # Kiểm tra xem môn học có hợp lệ không
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
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.hist(
        data[subject],
        bins=[x * 0.5 for x in range(21)],
        edgecolor="black",
        color="lightcoral",
    )
    ax.set_xlabel("Điểm")
    ax.set_ylabel("Số lượng thí sinh")
    ax.set_title(f"Phổ điểm môn {subject.capitalize()}")
    ax.set_xticks([x * 0.5 for x in range(21)])

    # Thêm lưới
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    # Hiển thị thông tin thống kê bên phải biểu đồ
    ax.text(
        1.02,
        0.8,
        f"Điểm cao nhất: {max_score} (Số học sinh: {max_count})",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.75,
        f"Điểm thấp nhất: {min_score} (Số học sinh: {min_count})",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.7,
        f"Điểm trung bình: {avg_score:.2f}",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02, 0.65, f"Điểm trung vị: {median_score}", transform=ax.transAxes, ha="left"
    )
    ax.text(
        1.02,
        0.6,
        f"Điểm phổ biến nhất: {mode_score}",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.55,
        f"Tổng số học sinh: {total_students}",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.5,
        f"Số học sinh có điểm < 1: {below_1}",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.45,
        f"Số học sinh có điểm < 5: {below_5}",
        transform=ax.transAxes,
        ha="left",
    )

    # Cân chỉnh layout để không bị chồng chéo
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()


def plot_score_distribution_by_combination(
    data, combination_code, subject_combinations
):
    """
    Vẽ biểu đồ phổ điểm cho một tổ hợp môn cụ thể.

    Args:
        data (pd.DataFrame): Dữ liệu điểm thi với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        combination_code (str): Mã tổ hợp môn (ví dụ: "A01", "C00") để tính tổng điểm tổ hợp.
        subject_combinations (dict): Dictionary chứa mã tổ hợp môn và danh sách các môn học tương ứng.

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
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.hist(
        data["combination_score"], bins=range(0, 31), edgecolor="black", color="skyblue"
    )
    ax.set_xlabel("Điểm")
    ax.set_ylabel("Số lượng thí sinh")
    ax.set_title(f"Phổ điểm tổ hợp {combination_code} ({', '.join(subjects)})")
    ax.set_xticks(range(0, 31))

    # Hiển thị thông tin thống kê bên phải biểu đồ
    ax.text(
        1.02,
        0.8,
        f"Điểm cao nhất: {max_score} (Số học sinh: {max_count})",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.75,
        f"Điểm thấp nhất: {min_score} (Số học sinh: {min_count})",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.7,
        f"Điểm trung bình: {avg_score:.2f}",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02, 0.65, f"Điểm trung vị: {median_score}", transform=ax.transAxes, ha="left"
    )
    ax.text(
        1.02,
        0.6,
        f"Điểm phổ biến nhất: {mode_score}",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.55,
        f"Tổng số học sinh: {total_students}",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.5,
        f"Số học sinh có điểm < 1: {below_1}",
        transform=ax.transAxes,
        ha="left",
    )
    ax.text(
        1.02,
        0.45,
        f"Số học sinh có điểm < 5: {below_5}",
        transform=ax.transAxes,
        ha="left",
    )

    # Cân chỉnh layout để không bị chồng chéo
    plt.tight_layout(rect=[0, 0, 0.85, 1])
    plt.show()


def plot_score_distribution_pie(data, combination_code, subject_combinations):
    """
    Vẽ biểu đồ tròn thể hiện tỷ lệ học sinh thuộc các nhóm điểm của một tổ hợp môn.

    Args:
        data (pd.DataFrame): Dữ liệu điểm thi với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        combination_code (str): Mã tổ hợp môn (ví dụ: "A01", "C00") để tính tổng điểm tổ hợp.
        subject_combinations (dict): Dictionary chứa mã tổ hợp môn và danh sách các môn học tương ứng.

    Returns:
        None: Hiển thị biểu đồ tròn trực tiếp.

    Raises:
        ValueError: Nếu mã tổ hợp không hợp lệ.
    """
    if combination_code not in subject_combinations:
        raise ValueError(f"Mã tổ hợp {combination_code} không hợp lệ.")

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

    # Thêm chú thích
    plt.legend(title="Nhóm điểm", loc="upper left")

    plt.show()


def plot_score_distribution_by_combinations(data, subject_combinations):
    """
    Vẽ biểu đồ cột hiển thị điểm cao nhất giữa các tổ hợp môn.

    Args:
        data (pd.DataFrame): Dữ liệu điểm thi với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        subject_combinations (dict): Dictionary chứa mã tổ hợp môn và danh sách các môn học tương ứng.

    Returns:
        None: Hiển thị biểu đồ cột trực tiếp.
    """
    # Tạo dictionary lưu điểm cao nhất
    combination_scores = {"Combination": [], "Max Score": []}

    # Tính điểm cao nhất cho từng tổ hợp
    for combination, subjects in subject_combinations.items():
        # Tính tổng điểm tổ hợp
        temp_data = data[subjects].replace(0, pd.NA)
        data["combination_score"] = temp_data.sum(axis=1, skipna=True)

        # Lấy điểm cao nhất
        max_score = data["combination_score"].max()

        # Lưu kết quả vào dictionary
        combination_scores["Combination"].append(combination)
        combination_scores["Max Score"].append(max_score)

    # Chuyển dictionary thành DataFrame
    scores_df = pd.DataFrame(combination_scores)

    # Sắp xếp DataFrame theo điểm cao nhất
    scores_df.sort_values("Max Score", inplace=True)

    # Vẽ biểu đồ cột nhóm
    plt.figure(figsize=(16, 8))
    bar_width = 0.35
    x = range(len(scores_df))

    # Vẽ cột Max Score
    bars = plt.bar(
        x,
        scores_df["Max Score"],
        width=bar_width,
        label="Điểm cao nhất",
        color="skyblue",
    )

    # Thêm số liệu trên đầu mỗi cột
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            yval,
            round(yval, 2),
            va="bottom",
            ha="center",
            fontsize=10,
        )

    # Thêm lưới
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Thiết lập trục và nhãn
    plt.xlabel("Tổ hợp môn", fontsize=12)
    plt.ylabel("Điểm", fontsize=12)
    plt.title("Phân phối điểm cao nhất giữa các tổ hợp môn", fontsize=16)
    plt.xticks([i for i in x], scores_df["Combination"], rotation=45)
    plt.legend()

    # Hiển thị biểu đồ
    plt.tight_layout()
    plt.show()


# Ví dụ gọi hàm
plot_score_distribution_by_combination(data2024, "A02", subject_combinations)

plot_score_distribution_by_subject(data2024, "ngu_van")

plot_score_distribution_pie(data2023, "A02", subject_combinations)

plot_score_distribution_by_combinations(data2023, subject_combinations)
