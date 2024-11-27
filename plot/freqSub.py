import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data2023 = pd.read_csv(r"data\diem2023.csv")
data2024 = pd.read_csv(r"data\diem2024.csv")


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
        "toan": "Toán",
        "ngu_van": "Ngữ văn",
        "ngoai_ngu": "Ngoại ngữ",
        "vat_li": "Vật lý",
        "hoa_hoc": "Hóa học",
        "sinh_hoc": "Sinh học",
        "lich_su": "Lịch sử",
        "dia_li": "Địa lý",
        "gdcd": "GDCD",
    }

    # Tạo DataFrame mới chứa điểm và năm
    data1["Year"] = year1
    data2["Year"] = year2
    combined_data = pd.concat([data1, data2], ignore_index=True)

    # Vẽ biểu đồ histogram cho từng môn
    fig, axes = plt.subplots(3, 3, figsize=(18, 12))
    fig.suptitle("Phân Bố Điểm Các Môn THPTQG 2 năm 2023, 2024 của TPHCM", fontsize=16, y=1)

    for ax, (subject, vietnamese_name) in zip(axes.flatten(), subjects.items()):
        sns.histplot(
            data=combined_data,
            x=subject,
            hue="Year",
            bins=20,
            kde=False,
            ax=ax,
            palette="pastel",
            alpha=0.6,
        )
        ax.set_title(vietnamese_name)
        ax.set_xlabel("Điểm")
        ax.set_ylabel("Tần suất")
        ax.grid(True)

    plt.tight_layout(pad=3.0)
    plt.show()


# Gọi hàm với dữ liệu của năm 2023 và 2024
# freqSub(data2023, data2024, 2023, 2024)
