import pandas as pd
import matplotlib.pyplot as plt

def scaPlot_compareSub(mon_hoc1, mon_hoc2):
    """ Hàm vẽ biểu đồ phân tán so sánh điểm của hai môn học giữa hai năm.
     
    Tham số: 
    mon_hoc1 (str): Mã môn học thứ nhất. mon_hoc2 (str): Mã môn học thứ hai. 
    
    Trả về: 
    None: Hàm sẽ hiển thị biểu đồ phân tán và không trả về giá trị nào. 
    
    Ví dụ: scaPlot_compareSub('toan', 'ngoai_ngu') 
    """
    # Đọc dữ liệu từ các file CSV
    data1 = pd.read_csv(r"data\diem2023.csv")
    data2 = pd.read_csv(r"data\diem2024.csv")

    # Loại bỏ các thí sinh có điểm NaN
    data1 = data1.dropna(subset=[mon_hoc1, mon_hoc2])
    data2 = data2.dropna(subset=[mon_hoc1, mon_hoc2])

    # Vẽ biểu đồ phân tán
    plt.figure(figsize=(10, 5))
    plt.scatter(data1[mon_hoc1], data1[mon_hoc2], color='blue', alpha=0.5, label='Năm 2023')
    plt.scatter(data2[mon_hoc1], data2[mon_hoc2], color='red', alpha=0.5, label='Năm 2024')
    plt.xlabel(f'Điểm {mon_hoc1.capitalize()}')
    plt.ylabel(f'Điểm {mon_hoc2.capitalize()}')
    plt.title(f'So sánh điểm {mon_hoc1.capitalize()} và {mon_hoc2.capitalize()} giữa hai năm')
    plt.legend()
    plt.show()

# Gọi hàm với các tham số cụ thể
# scaPlot_compareSub('ngu_van', 'toan')
