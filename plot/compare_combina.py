import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_heatmap(data, year):
    """
    Vẽ biểu đồ heatmap để hiển thị ma trận tương quan giữa các môn học.

    Args:
        data (pd.DataFrame): Dữ liệu điểm thi với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        year (int): Năm học của dữ liệu (ví dụ: 2023, 2024).

    Returns:
        None: Hiển thị trực tiếp biểu đồ heatmap với ma trận tương quan giữa các môn học.

    Raises:
        None
    """
    # Xử lý dữ liệu thiếu
    data = data.fillna(0)

    # Tính ma trận tương quan
    corr_matrix = data.corr()

    # Vẽ biểu đồ heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        cbar=True,
        square=True,
        linewidths=0.5,
    )
    plt.title(f"Ma Trận Tương Quan Giữa Các Môn Học Năm {year}", fontsize=16)
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.show()


# Đọc file CSV
data2023 = pd.read_csv("diem2023.csv")
data2024 = pd.read_csv("diem2024.csv")

# Vẽ heatmap cho dữ liệu năm 2023 và 2024
plot_heatmap(data2023, 2023)
plot_heatmap(data2024, 2024)
