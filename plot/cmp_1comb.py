import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ file CSV
diem_2023 = pd.read_csv("diem2023.csv")
diem_2024 = pd.read_csv("diem2024.csv")

# Khung điểm mới
khoang_diem = [0, 12, 16, 20, 24, 26, 28, 30]

# Định nghĩa các tổ hợp môn
to_hop_A00 = ["toan", "vat_li", "hoa_hoc"]
to_hop_A01 = ["toan", "vat_li", "ngoai_ngu"]
to_hop_B = ["toan", "hoa_hoc", "sinh_hoc"]
to_hop_C = ["ngu_van", "lich_su", "dia_li"]
to_hop_D = ["toan", "ngu_van", "ngoai_ngu"]


# Hàm để tính tổng điểm của từng tổ hợp môn
def tinh_diem_to_hop(df, to_hop):
    return df[to_hop].sum(axis=1)


# Hàm để phân loại điểm theo các khung điểm
def phan_loai_diem(diem, khoang_diem):
    return pd.cut(diem, bins=khoang_diem, include_lowest=True, right=False)


# Tạo bảng phân loại điểm cho từng tổ hợp môn và từng năm
to_hop_dict = {
    "A00": to_hop_A00,
    "A01": to_hop_A01,
    "B": to_hop_B,
    "C": to_hop_C,
    "D": to_hop_D,
}
khung_diem_dict_2023 = {}
khung_diem_dict_2024 = {}

for to_hop, mon in to_hop_dict.items():
    diem_2023_to_hop = tinh_diem_to_hop(diem_2023, mon)
    diem_2024_to_hop = tinh_diem_to_hop(diem_2024, mon)
    khung_diem_dict_2023[to_hop] = (
        phan_loai_diem(diem_2023_to_hop, khoang_diem).value_counts().sort_index()
    )
    khung_diem_dict_2024[to_hop] = (
        phan_loai_diem(diem_2024_to_hop, khoang_diem).value_counts().sort_index()
    )

# Vẽ biểu đồ
fig, axs = plt.subplots(3, 2, figsize=(15, 20))
fig.suptitle(
    "So sánh số lượng học sinh trong các khung điểm của các tổ hợp môn năm 2023 và 2024"
)

for ax, (to_hop, khung_diem_2023) in zip(
    axs.flatten()[:5], khung_diem_dict_2023.items()
):  # Chỉ lấy 5 tổ hợp môn đầu tiên
    khung_diem_2024 = khung_diem_dict_2024[to_hop]
    bars1 = ax.bar(
        khung_diem_2023.index.astype(str),
        khung_diem_2023,
        width=0.4,
        align="center",
        label="2023",
    )
    bars2 = ax.bar(
        khung_diem_2024.index.astype(str),
        khung_diem_2024,
        width=0.4,
        align="edge",
        label="2024",
    )
    ax.set_title(f"Tổ hợp {to_hop}")
    ax.set_xlabel("Khung điểm")
    ax.set_ylabel("Số lượng học sinh")
    ax.legend()

    # Thêm số liệu trên đầu mỗi cột
    for bar in bars1:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            yval,
            int(yval),
            va="bottom",
            ha="center",
            fontsize=7,
        )
    for bar in bars2:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            yval,
            int(yval),
            va="bottom",
            ha="center",
            fontsize=7,
        )

# Ẩn plot thứ 6
fig.delaxes(axs.flatten()[5])

plt.tight_layout(pad=9.0)
plt.show()
