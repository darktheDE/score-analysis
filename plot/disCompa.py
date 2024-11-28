import pandas as pd
import matplotlib.pyplot as plt

def plot_student_distribution_comparison():
    """
    Vẽ biểu đồ so sánh số lượng học sinh trong các khung điểm của một số tổ hợp môn phổ biến năm 2023 và 2024.

    Returns:
        None: Hiển thị trực tiếp biểu đồ so sánh số lượng học sinh trong các khung điểm.
    """
    # Đọc dữ liệu từ file CSV
    data_2023 = pd.read_csv(r"data\diem2023.csv")
    data_2024 = pd.read_csv(r"data\diem2024.csv")

    # Khung điểm mới
    score_bins = [0, 12, 16, 20, 24, 26, 28, 30]

    # Định nghĩa các tổ hợp môn
    to_hop_A00 = ["toan", "vat_li", "hoa_hoc"]
    to_hop_A02 = ["toan", "vat_li", "sinh_hoc"]
    to_hop_B00 = ["toan", "hoa_hoc", "sinh_hoc"]
    to_hop_C00 = ["ngu_van", "lich_su", "dia_li"]
    to_hop_C19 = ["ngu_van", "lich_su", "gdcd"]
    to_hop_C20 = ["ngu_van", "dia_li", "gdcd"]

    def calculate_combination_score(df, combination):
        """
        Tính tổng điểm của từng tổ hợp môn.

        Args:
            df (pd.DataFrame): Dữ liệu điểm thi với mỗi cột là một môn học và các hàng là điểm của từng học sinh.
            combination (list): Danh sách các môn học thuộc tổ hợp cần tính điểm.

        Returns:
            pd.Series: Tổng điểm của từng học sinh cho tổ hợp môn.
        """
        # Loại bỏ các thí sinh không thi môn thuộc tổ hợp (NaN)
        df = df.dropna(subset=combination)
        return df[combination].sum(axis=1)

    def categorize_scores(scores, bins):
        """
        Phân loại điểm theo các khung điểm.

        Args:
            scores (pd.Series): Điểm của các học sinh.
            bins (list): Danh sách các khung điểm để phân loại.

        Returns:
            pd.Categorical: Các điểm được phân loại theo khung điểm.
        """
        return pd.cut(scores, bins=bins, include_lowest=True, right=False)

    # Tạo bảng phân loại điểm cho từng tổ hợp môn và từng năm
    combination_dict = {
        "A00": to_hop_A00,
        "A02": to_hop_A02,
        "B00": to_hop_B00,
        "C00": to_hop_C00,
        "C19": to_hop_C19,
        "C20": to_hop_C20
    }
    score_category_dict_2023 = {}
    score_category_dict_2024 = {}

    for combination, subjects in combination_dict.items():
        scores_2023 = calculate_combination_score(data_2023, subjects)
        scores_2024 = calculate_combination_score(data_2024, subjects)
        score_category_dict_2023[combination] = (
            categorize_scores(scores_2023, score_bins).value_counts().sort_index()
        )
        score_category_dict_2024[combination] = (
            categorize_scores(scores_2024, score_bins).value_counts().sort_index()
        )

    # Vẽ biểu đồ
    fig, axs = plt.subplots(3, 2, figsize=(15, 20))
    fig.suptitle(
        "So sánh số lượng học sinh trong các khung điểm của một số tổ hợp môn phổ biến năm 2023 và 2024 TPHCM"
    )

    for ax, (combination, score_category_2023) in zip(
        axs.flatten()[:6], score_category_dict_2023.items()
    ):
        score_category_2024 = score_category_dict_2024[combination]
        bars1 = ax.bar(
            score_category_2023.index.astype(str),
            score_category_2023,
            width=0.4,
            align="center",
            label="2023",
        )
        bars2 = ax.bar(
            score_category_2024.index.astype(str),
            score_category_2024,
            width=0.4,
            align="edge",
            label="2024",
        )
        ax.set_title(f"Tổ hợp {combination}")
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

    plt.tight_layout(pad=9.0)
    plt.show()

# plot_student_distribution_comparison()