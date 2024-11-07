# UI.py
import tkinter as tk
from tkinter import messagebox

# Dữ liệu lưu trữ thông tin cua sinh viên
student_data = {}

def load_data_from_file():
    try:
        with open("diem_hoc_sinh_test.py", "r") as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 10:  # Đảm bảo có đủ thông tin
                    student_data[data[0]] = {
                        "math": data[1],
                        "literature": data[2],
                        "english": data[3],
                        "physics": data[4],
                        "chemistry": data[5],
                        "biology": data[6],
                        "history": data[7],
                        "geography": data[8],
                        "civic": data[9]
                    }
    except FileNotFoundError:
        pass  # Nếu file không tồn tại, không làm gì cả

def save_to_file():
    with open("diem_hoc_sinh_test.py", "w") as file:
        for student_id, scores in student_data.items():
            file.write(f"{student_id},{scores['math']},{scores['literature']},"
                       f"{scores['english']},{scores['physics']},{scores['chemistry']},"
                       f"{scores['biology']},{scores['history']},{scores['geography']},"
                       f"{scores['civic']}\n")

def is_valid_score(score):
    try:
        value = float(score)
        return -1 <= value <= 10
    except ValueError:
        return False

def submit_info():
    student_id = entry_id.get()
    scores = {
        "math": entry_math.get(),
        "physics": entry_physics.get(),
        "chemistry": entry_chemistry.get(),
        "english": entry_english.get(),
        "literature": entry_literature.get(),
        "biology": entry_biology.get(),
        "history": entry_history.get(),
        "geography": entry_geography.get(),
        "civic": entry_civic.get(),
    }
    
    # Kiểm tra điểm hợp lệ
    for key, value in scores.items():
        if not is_valid_score(value):
            messagebox.showerror("Lỗi", f"Điểm {key} không hợp lệ! Phải từ -1 đến 10.")
            return
    
    student_data[student_id] = scores
    save_to_file()  # Lưu tất cả dữ liệu vào file
    messagebox.showinfo("Thông báo", "Thông tin đã được lưu vào file.")

def search_info():
    student_id = entry_search.get()
    if student_id in student_data:
        scores = student_data[student_id]
        entry_math.delete(0, tk.END)
        entry_math.insert(0, scores["math"])
        entry_physics.delete(0, tk.END)
        entry_physics.insert(0, scores["physics"])
        entry_chemistry.delete(0, tk.END)
        entry_chemistry.insert(0, scores["chemistry"])
        entry_english.delete(0, tk.END)
        entry_english.insert(0, scores["english"])
        entry_literature.delete(0, tk.END)
        entry_literature.insert(0, scores["literature"])
        entry_biology.delete(0, tk.END)
        entry_biology.insert(0, scores["biology"])
        entry_history.delete(0, tk.END)
        entry_history.insert(0, scores["history"])
        entry_geography.delete(0, tk.END)
        entry_geography.insert(0, scores["geography"])
        entry_civic.delete(0, tk.END)
        entry_civic.insert(0, scores["civic"])

        # Xuất thông tin
        messagebox.showinfo("Thông tin sinh viên", 
                            f"Mã số: {student_id}\n"
                            f"Điểm Toán: {scores['math']}\n"
                            f"Điểm Ngữ Văn: {scores['literature']}\n"
                            f"Điểm Ngoại Ngữ: {scores['english']}\n"
                            f"Điểm Lý: {scores['physics']}\n"
                            f"Điểm Hóa: {scores['chemistry']}\n"
                            f"Điểm Sinh: {scores['biology']}\n"
                            f"Điểm Lịch Sử: {scores['history']}\n"
                            f"Điểm Địa Lý: {scores['geography']}\n"
                            f"Điểm GDCD: {scores['civic']}")
    else:
        messagebox.showwarning("Cảnh báo", "Không tìm thấy sinh viên.")

def delete_info():
    student_id = entry_search.get()
    if student_id in student_data:
        del student_data[student_id]
        save_to_file()  # Cập nhật lại file sau khi xóa
        clear_entries()
        messagebox.showinfo("Thông báo", "Thông tin đã được xóa.")
    else:
        messagebox.showwarning("Cảnh báo", "Không tìm thấy sinh viên.")

def update_info():
    student_id = entry_id.get()
    if student_id in student_data:
        scores = {
            "math": entry_math.get(),
            "physics": entry_physics.get(),
            "chemistry": entry_chemistry.get(),
            "english": entry_english.get(),
            "literature": entry_literature.get(),
            "biology": entry_biology.get(),
            "history": entry_history.get(),
            "geography": entry_geography.get(),
            "civic": entry_civic.get(),
        }
        
        # Kiểm tra điểm hợp lệ
        for key, value in scores.items():
            if not is_valid_score(value):
                messagebox.showerror("Lỗi", f"Điểm {key} không hợp lệ! Phải từ -1 đến 10.")
                return
        
        student_data[student_id] = scores
        save_to_file()  # Ghi thông tin đã cập nhật vào file
        messagebox.showinfo("Thông báo", "Thông tin đã được cập nhật.")
    else:
        messagebox.showwarning("Cảnh báo", "Không tìm thấy sinh viên.")

def clear_entries():
    for entry in entries:
        entry.delete(0, tk.END)

def export_info():
    try:
        with open("diem_hoc_sinh_test.py", "r") as file:
            content = file.readlines()
        
        export_data = ""
        for line in content:
            data = line.strip().split(',')
            export_data += f"Mã số: {data[0]}, Điểm Toán: {data[1]}, Điểm Ngữ Văn: {data[2]}, " \
                           f"Điểm Ngoại Ngữ: {data[3]}, Điểm Lý: {data[4]}, Điểm Hóa: {data[5]}, " \
                           f"Điểm Sinh: {data[6]}, Điểm Lịch Sử: {data[7]}, Điểm Địa Lý: {data[8]}, " \
                           f"Điểm GDCD: {data[9]}\n"
        
        messagebox.showinfo("Thông tin xuất", export_data)
    except FileNotFoundError:
        messagebox.showwarning("Cảnh báo", "File không tồn tại.")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý thông tin điểm tốt nghiệp sinh viên")

# Tải dữ liệu từ file khi khởi động
load_data_from_file()

# Tạo các nhãn và ô nhập liệu
labels = ["Mã số", "Điểm Toán", "Điểm Lý", "Điểm Hóa", "Điểm Anh Văn", 
          "Điểm Ngữ Văn", "Điểm Sinh", "Điểm Sử", "Điểm Địa", "Điểm GDCD"]

entries = []
for label in labels:
    row = tk.Frame(root)
    label_widget = tk.Label(row, text=label, width=15)
    entry_widget = tk.Entry(row)
    row.pack(side=tk.TOP, padx=5, pady=5)
    label_widget.pack(side=tk.LEFT)
    entry_widget.pack(side=tk.RIGHT)
    entries.append(entry_widget)

# Lưu trữ các ô nhập liệu vào biến
entry_id, entry_math, entry_physics, entry_chemistry, entry_english, \
entry_literature, entry_biology, entry_history, entry_geography, entry_civic = entries

# Tìm kiếm
search_label = tk.Label(root, text="Tìm kiếm mã số")
search_label.pack(side=tk.TOP, padx=5, pady=5)
entry_search = tk.Entry(root)
entry_search.pack(side=tk.TOP, padx=5, pady=5)

# Khung chứa các nút chức năng
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, padx=5, pady=5)

# Nút gửi thông tin
submit_button = tk.Button(button_frame, text="Gửi thông tin", command=submit_info)
submit_button.pack(side=tk.LEFT, padx=5)

# Nút tìm kiếm
search_button = tk.Button(button_frame, text="Tìm kiếm", command=search_info)
search_button.pack(side=tk.LEFT, padx=5)

# Nút xóa thông tin
delete_button = tk.Button(button_frame, text="Xóa thông tin", command=delete_info)
delete_button.pack(side=tk.LEFT, padx=5)

# Nút sửa thông tin
update_button = tk.Button(button_frame, text="Cập nhật thông tin", command=update_info)
update_button.pack(side=tk.LEFT, padx=5)

# Nút xuất thông tin
export_button = tk.Button(button_frame, text="Xuất thông tin", command=export_info)
export_button.pack(side=tk.LEFT, padx=5)

# Bắt đầu vòng lặp chính của ứng dụng
root.mainloop()
