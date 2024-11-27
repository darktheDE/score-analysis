import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def heatmapSubject(data, year):
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
    data = data.iloc[:, 1:]

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
    plt.title(f"Ma Trận Tương Quan Giữa Các Môn Học Năm {year} TPHCM", fontsize=16)
    plt.xticks(rotation=45, ha="right")
    plt.yticks(rotation=0)
    plt.show()
    
def heatmapComb(data, year):
    # Định nghĩa các tổ hợp môn
    to_hop_dict = {
            "A00": ["toan", "vat_li", "hoa_hoc"],
            "A02": ["toan", "vat_li", "sinh_hoc"],
            "B00": ["toan", "hoa_hoc", "sinh_hoc"],
            "C00": ["ngu_van", "lich_su", "dia_li"],
            "C19": ["ngu_van", "lich_su", "gdcd"],
            "C20": ["ngu_van", "dia_li", "gdcd"]
    }

    # Tính điểm trung bình cho mỗi tổ hợp môn
    for to_hop, mon in to_hop_dict.items():
        data[to_hop] = data[mon].mean(axis=1)

    # Tạo DataFrame mới chỉ chứa điểm trung bình của các tổ hợp môn
    diem_to_hop = data[list(to_hop_dict.keys())]

    # Tính toán ma trận tương quan
    corr_matrix = diem_to_hop.corr()

    # Vẽ biểu đồ heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True, square=True)
    plt.title(f"Ma Trận Tương Quan Giữa Một Số Tổ Hợp Môn Phổ Biến Năm {year} TPHCM", fontsize=16)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.show()

# Đọc file CSV
data2023 = pd.read_csv(r"data\diem2023.csv")
data2024 = pd.read_csv(r"data\diem2024.csv")

# Vẽ heatmap cho dữ liệu năm 2023 và 2024
# heatmapSubject(data2023, 2023)
# heatmapSubject(data2024, 2024)

# heatmapComb(data2023, 2023)
# heatmapComb(data2024, 2024)