import pandas as pd
import matplotlib.pyplot as plt

# Đọc các file CSV
data2023 = pd.read_csv(r"data\diem2023.csv")
data2024 = pd.read_csv(r"data\diem2024.csv")


def plot_average_scores(data2023, data2024):
    """
    Tính toán điểm trung bình của các môn học và vẽ biểu đồ đường so sánh
    xu hướng điểm trung bình giữa hai năm 2023 và 2024.

    Args:
        data2023 (pd.DataFrame): Dữ liệu điểm thi của năm 2023 với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
        data2024 (pd.DataFrame): Dữ liệu điểm thi của năm 2024 với mỗi cột là một môn học và các hàng là điểm của từng học sinh.

    Returns:
        None: Hiển thị trực tiếp biểu đồ đường so sánh xu hướng điểm trung bình giữa hai năm.

    Raises:
        None
    """
    # Xử lý giá trị thiếu
    data2023 = data2023.fillna(0)
    data2024 = data2024.fillna(0)

    # Tính toán điểm trung bình
    avg2023 = data2023.mean()
    avg2024 = data2024.mean()

    # Tạo DataFrame để chứa điểm trung bình
    df = pd.DataFrame(
        {
            "Year": [2023, 2024],
            "Toan": [avg2023["toan"], avg2024["toan"]],
            "Ngu Van": [avg2023["ngu_van"], avg2024["ngu_van"]],
            "Ngoai Ngu": [avg2023["ngoai_ngu"], avg2024["ngoai_ngu"]],
            "Vat Li": [avg2023["vat_li"], avg2024["vat_li"]],
            "Hoa Hoc": [avg2023["hoa_hoc"], avg2024["hoa_hoc"]],
            "Sinh Hoc": [avg2023["sinh_hoc"], avg2024["sinh_hoc"]],
            "Lich Su": [avg2023["lich_su"], avg2024["lich_su"]],
            "Dia Li": [avg2023["dia_li"], avg2024["dia_li"]],
            "GDCD": [avg2023["gdcd"], avg2024["gdcd"]],
        }
    )

    # Vẽ biểu đồ
    plt.figure(figsize=(12, 6))
    for subject in df.columns[1:]:
        plt.plot(df["Year"], df[subject], marker="o", label=subject)
        for x, y in zip(df["Year"], df[subject]):
            plt.text(x, y, f"{y:.2f}", ha="right", va="bottom")

    plt.title("Xu hướng điểm trung bình từng môn 2 năm 2023, 2024 TPHCM")
    plt.xlabel("Năm")
    plt.ylabel("Điểm trung bình")
    plt.xticks([2023, 2024])  # Chỉ hiển thị năm 2023 và 2024 trên trục X
    plt.legend()
    plt.grid(True)
    plt.show()


# Gọi hàm để vẽ biểu đồ
plot_average_scores(data2023, data2024)
