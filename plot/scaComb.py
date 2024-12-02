import pandas as pd
import matplotlib.pyplot as plt

subject_combinations = {
    "A00": ["toan", "vat_li", "hoa_hoc"],
    "A02": ["toan", "vat_li", "sinh_hoc"],
    "B00": ["toan", "hoa_hoc", "sinh_hoc"],
    "C00": ["ngu_van", "lich_su", "dia_li"],
    "C19": ["ngu_van", "lich_su", "gdcd"],
    "C20": ["ngu_van", "dia_li", "gdcd"],
}
def scaPlot_combination(ma_to_hop_1, ma_to_hop_2):
    """
    Hàm vẽ biểu đồ phân tán so sánh điểm của hai tổ hợp môn học giữa hai năm.

    Tham số:
    ma_to_hop_1 (str): Mã tổ hợp ứng với danh sách các môn học trong tổ hợp thứ nhất.
    ma_to_hop_2 (list): Mã tổ hợp ứng với danh sách các môn học trong tổ hợp thứ hai.

    Trả về:
    None: Hàm sẽ hiển thị biểu đồ phân tán và không trả về giá trị nào.

    Ví dụ:
    scaPlot_combination('A00', 'A02')
    """
    
    # Đọc dữ liệu từ các file CSV
    data1 = pd.read_csv(r"data\diem2023.csv")
    data2 = pd.read_csv(r"data\diem2024.csv")
    to_hop_1 = subject_combinations[ma_to_hop_1]
    to_hop_2 = subject_combinations[ma_to_hop_2]

    # Tính điểm trung bình của các tổ hợp môn học
    data1['trung_binh_to_hop_1'] = data1[to_hop_1].mean(axis=1)*3
    data1['trung_binh_to_hop_2'] = data1[to_hop_2].mean(axis=1)*3
    data2['trung_binh_to_hop_1'] = data2[to_hop_1].mean(axis=1)*3
    data2['trung_binh_to_hop_2'] = data2[to_hop_2].mean(axis=1)*3

    # Loại bỏ các thí sinh có điểm NaN
    data1 = data1.dropna(subset=['trung_binh_to_hop_1', 'trung_binh_to_hop_2'])
    data2 = data2.dropna(subset=['trung_binh_to_hop_1', 'trung_binh_to_hop_2'])

    # Vẽ biểu đồ phân tán
    plt.figure(figsize=(10, 5))
    plt.scatter(data1['trung_binh_to_hop_1'], data1['trung_binh_to_hop_2'], color='blue', alpha=0.5, label='2023')
    plt.scatter(data2['trung_binh_to_hop_1'], data2['trung_binh_to_hop_2'], color='red', alpha=0.5, label='2024')
    plt.xlabel(f'Điểm Trung Bình Tổ Hợp {ma_to_hop_1}')
    plt.ylabel(f'Điểm Trung Bình Tổ Hợp {ma_to_hop_2}')
    plt.title('So sánh điểm trung bình của hai tổ hợp môn học giữa hai năm 2023 và 2024')
    plt.legend()
    plt.show()

# Gọi hàm với các tham số cụ thể
# scaPlot_combination("A00", "A02")
