import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc file CSV
data2023 = pd.read_csv('diem2023.csv')
data2024 = pd.read_csv('diem2024.csv')

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
    # Tính ma trận tương quan
    corr_matrix = data.corr()

    # Vẽ biểu đồ heatmap
    plt.figure(figsize=(8, 4))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True, square=True)
    plt.title(f'Ma Trận Tương Quan Giữa Các Môn Học Năm {year}')
    plt.show()

# Gọi hàm để vẽ biểu đồ heatmap cho dữ liệu năm 2023 và 2024
# plot_heatmap(data2023, 2023)
plot_heatmap(data2024, 2024)
