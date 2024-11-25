import pandas as pd
import matplotlib.pyplot as plt

data2023 = pd.read_csv('diem2023.csv')
data2024 = pd.read_csv('diem2024.csv')

def freqSub(data1, data2, year1, year2):
    """
    Vẽ biểu đồ histogram so sánh phân bố điểm của các môn học giữa hai năm.

    Args:
        data1 (pd.DataFrame): Dữ liệu điểm thi của năm thứ nhất, với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        data2 (pd.DataFrame): Dữ liệu điểm thi của năm thứ hai, với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        year1 (int): Năm học của dữ liệu thứ nhất (ví dụ: 2023).
        year2 (int): Năm học của dữ liệu thứ hai (ví dụ: 2024).

    Returns:
        None: Hiển thị trực tiếp biểu đồ histogram so sánh phân bố điểm của các môn học giữa hai năm.

    Raises:
        None
    """
    # Liệt kê các môn học và tên tiếng Việt tương ứng
    subjects = {
        'toan': 'Toán',
        'ngu_van': 'Ngữ văn',
        'ngoai_ngu': 'Ngoại ngữ',
        'vat_li': 'Vật lý',
        'hoa_hoc': 'Hóa học',
        'sinh_hoc': 'Sinh học',
        'lich_su': 'Lịch sử',
        'dia_li': 'Địa lý',
        'gdcd': 'GDCD'
    }

    # Vẽ biểu đồ histogram cho từng môn
    plt.figure(figsize=(18, 12))  # Tăng kích thước hình
    for i, (subject, vietnamese_name) in enumerate(subjects.items(), 1):
        plt.subplot(3, 3, i)
        data1[subject].dropna().plot(kind='hist', bins=10, alpha=0.5, label=f'{year1}', grid=True)
        data2[subject].dropna().plot(kind='hist', bins=10, alpha=0.5, label=f'{year2}', grid=True)
        plt.xlabel('Điểm')
        plt.ylabel('Tần suất')
        plt.title(vietnamese_name)  # Hiển thị tên tiếng Việt của môn học
        plt.legend()
        plt.tight_layout(pad=5.0)  # Tăng khoảng cách giữa các subplot
    
    plt.suptitle('Phân Bố Điểm Các Môn THPTQG', fontsize=16, y = 1)
    plt.show()

# Gọi hàm với dữ liệu của năm 2023 và 2024
freqSub(data2023, data2024, 2023, 2024)
