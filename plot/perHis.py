import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def plot_percentage_histogram(subject):
    """
    Vẽ biểu đồ histogram để so sánh phân bố điểm của một môn học giữa hai năm,
    đồng thời hiển thị tỷ lệ phần trăm của mỗi khoảng điểm và các percentiles.

    Args:
        subject (str): Tên môn học cần vẽ biểu đồ (ví dụ: 'toan').
    
    Returns:
        None: Hiển thị trực tiếp biểu đồ histogram so sánh phân bố điểm của một môn học giữa hai năm.

    Raises:
        ValueError: Nếu môn học không có trong dữ liệu của một trong hai năm.
    """
    data1 = pd.read_csv(r"data\diem2023.csv")
    data2 = pd.read_csv(r"data\diem2024.csv")
    year1 = 2023
    year2 = 2024
    
    # Kiểm tra xem môn học có trong dữ liệu không
    if subject not in data1.columns or subject not in data2.columns:
        print(f"Môn học {subject} không có trong dữ liệu.")
        return

    # Tạo biểu đồ
    fig, axs = plt.subplots(1, 2, figsize=(18, 6), sharey=True)

    # Vẽ histogram và tính tỷ lệ phần trăm cho năm 2023
    counts1, bins1, patches1 = axs[0].hist(
        data1[subject].dropna(),
        bins=10,
        edgecolor="black",
        color="skyblue",
        density=True,
    )
    counts1 = counts1 * (bins1[1] - bins1[0]) * 100  # Chuyển đổi tỷ lệ phần trăm
    for count, patch in zip(counts1, patches1):
        height = patch.get_height()
        axs[0].text(
            patch.get_x() + patch.get_width() / 2.0,
            height,
            f"{count:.1f}%",
            ha="center",
            va="bottom",
        )
    axs[0].set_title(f"Năm {year1}")
    axs[0].set_xlabel("Điểm")
    axs[0].set_ylabel("Tần suất (%)")

    # Vẽ histogram và tính tỷ lệ phần trăm cho năm 2024
    counts2, bins2, patches2 = axs[1].hist(
        data2[subject].dropna(),
        bins=10,
        edgecolor="black",
        color="lightcoral",
        density=True,
    )
    counts2 = counts2 * (bins2[1] - bins2[0]) * 100  # Chuyển đổi tỷ lệ phần trăm
    for count, patch in zip(counts2, patches2):
        height = patch.get_height()
        axs[1].text(
            patch.get_x() + patch.get_width() / 2.0,
            height,
            f"{count:.1f}%",
            ha="center",
            va="bottom",
        )
    axs[1].set_title(f"Năm {year2}")
    axs[1].set_xlabel("Điểm")

    # Thêm tiêu đề tổng thể cho hình
    plt.suptitle(
        f"So Sánh Phân Bố Điểm Môn {subject.capitalize()} Giữa Các Năm 2023, 2024 của TPHCM",
        fontsize=16,
        y=1,
    )
    plt.tight_layout(pad=3.0)
    plt.show()


# Gọi hàm để vẽ biểu đồ Percentage Histogram cho một môn, ví dụ: Toán
# plot_percentage_histogram("toan")
