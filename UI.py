from tkinter import *
from utils.CRUD import CRUD
# Tạo cửa sổ chính
root = Tk()

# Đặt kích thước cửa sổ cố định
window_width = 847
window_height = 612

# Khai báo các frame toàn cục
frame_feature = None
frame_menu = None
frame_content = None

# Hàm để hiển thị màn hình ở giữa
def makecenter(root):
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (window_width // 2)
    y = (root.winfo_screenheight() // 2) - (window_height // 2) - 30
    root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Tạo các chức năng của Frame bên trái (Features)
def create_features(root, change_content_callback):
    global frame_feature
    frame_feature = Frame(root, bg="#000080")
    frame_feature.grid(column=0, row=0, rowspan=2,sticky="nswe")  # Kéo dài toàn bộ chiều dọc

    # Đặt chiều rộng tối thiểu cho frame chứa các nút
    frame_feature.grid_columnconfigure(0, minsize=100)
    # Tạo danh sách nút bên dưới logo
    buttons = [
        ("\n \n ", lambda: change_content_callback(""), "icon_UI/hcmute.png"),
        ("Home", lambda: change_content_callback("Home"), "icon_UI/home.png"),
        ("Search", lambda: change_content_callback("Search"), "icon_UI/loupe.png"),
        ("Members", lambda: change_content_callback("Members"), "icon_UI/group.png"),
        ("Student List", lambda: change_content_callback("Student List"), "icon_UI/cells.png"),
        ("Chart", lambda: change_content_callback("Chart"), "icon_UI/char.png"),
        ("Document", lambda: change_content_callback("Document"), "icon_UI/documents.png"),
    ]

    for i, (text_content, command, icon_path) in enumerate(buttons, start=1):
        try:
            # Tải icon cho từng nút
            icon = PhotoImage(file=icon_path)
            icon = icon.subsample(20, 20)  # Điều chỉnh kích thước icon nếu cần
        except Exception as e:
            print(f"Không thể tải icon {icon_path}: {e}")
            icon = None

        # Tạo nút với icon và text
        button = Button(
            frame_feature,
            font=('Helvetica', 9),
            text = text_content,
            justify= LEFT,
            anchor = 'w',
            fg="white",
            bg="#000080",
            bd=0,
            image=icon,  # Gắn icon vào nút
            compound= LEFT,
            command=command,
        )
        button.grid(column=0, row=i+1, pady=5, padx= 5, sticky="w")
        if icon:
            button.image = icon  # Lưu tham chiếu icon để tránh mất ảnh

# Tạo Menu (Menu bên phải)
def create_menu(root):
    global frame_menu
    frame_menu = Frame(root, bg="#104E8B")
    frame_menu.grid(column=1, row=0, sticky="ew")

    # Thêm nút hoặc nội dung vào menu (có thể bổ sung nếu cần)
    Label(frame_menu, text = ' \n ' ,bg="#104E8B").grid(column=0, row=0, padx=10, pady=5)

# Tạo nội dung (Nội dung chính)
def create_content(root):
    global frame_content
    frame_content = Frame(root, bg="white")
    frame_content.grid(column=1, row=1, sticky="nsew")
    return frame_content

# Hàm để thay đổi nội dung khi nhấn nút
def change_content(content):
    # Hàm để tạo một Label với ảnh và thông tin
    def create_label_with_image(frame, row, col, image_file, text):
        # Tạo Label chính
        label = Label(frame, bg="lightblue", relief="solid")
        label.grid(column=col, row=row, padx=18, pady=5, sticky="nsew")  # Dùng sticky để giãn rộng Label
        
        # Thêm Label hiển thị thông tin vào Label
        text_label = Label(label, bg="lightblue", justify='left', anchor='w', text=text, font=('Arial', 9))
        text_label.grid(column=1, row=0, sticky="nswe")  # sticky="nswe" giúp giãn Label theo cả chiều ngang và dọc

        # Thêm ảnh vào Label bên trong Label
        try:
            img = PhotoImage(file=image_file)
            img = img.subsample(3, 3)  # Thay đổi kích thước ảnh theo tỷ lệ
            img_info = Label(label, image=img, bg="lightblue")
            img_info.grid(column=0, row=0, sticky="nswe")  # Đặt ảnh vào vị trí cột 0, hàng 0 của label
            label.image = img  # Giữ tham chiếu đến ảnh để tránh mất ảnh
        except Exception as e:
            print(f"Không thể tải ảnh: {e}")

        return label

    for widget in frame_content.winfo_children():
        widget.destroy()

    if content == 'Members':
        # Tạo các label với ảnh và thông tin
        text_info='Tên: Phan Trọng Phú \n MSSV: 23133056 \n Nhiệm vụ: .............'
        create_label_with_image(frame_content, row=0, col=0, image_file= 'icon_UI/hung.png', text=text_info)
        create_label_with_image(frame_content, row=1, col=0, image_file= 'icon_UI/hung.png', text=text_info)
        create_label_with_image(frame_content, row=2, col=0, image_file= 'icon_UI/hung.png', text=text_info)
        create_label_with_image(frame_content, row=0, col=1, image_file= 'icon_UI/hung.png', text=text_info)
        create_label_with_image(frame_content, row=1, col=1, image_file='icon_UI/hung.png', text=text_info)
    elif content == 'Search':
        # Nút xác nhận
        def on_confirm_click():
            # Lấy dữ liệu từ các entry
            student_id = entry_id.get()
            term = entry_term.get()
            
            # Giả sử điểm các môn sẽ được tính hoặc lấy từ cơ sở dữ liệu:
            scores = {
                "Toán": 8.5,
                "Lý": 7.0,
                "Hóa": 8.0,
                "Văn": 6.5,
                "Tiếng Anh": 9.0,
                "Sinh": 7.5,
                "Sử": 6.0,
                "Địa": 7.8,
                "GDCD": 8.2
            }
            
            # Cập nhật điểm vào các entry môn học
            entry_math.delete(0, END)
            entry_physics.delete(0, END)
            entry_chemistry.delete(0, END)
            entry_literature.delete(0, END)
            entry_english.delete(0, END)
            entry_biology.delete(0, END)
            entry_history.delete(0, END)
            entry_geography.delete(0, END)
            entry_gdcd.delete(0, END)

            entry_math.insert(0, scores["Toán"])
            entry_physics.insert(0, scores["Lý"])
            entry_chemistry.insert(0, scores["Hóa"])
            entry_literature.insert(0, scores["Văn"])
            entry_english.insert(0, scores["Tiếng Anh"])
            entry_biology.insert(0, scores["Sinh"])
            entry_history.insert(0, scores["Sử"])
            entry_geography.insert(0, scores["Địa"])
            entry_gdcd.insert(0, scores["GDCD"])


        frame_search = Frame(frame_content, bg="lightblue", bd =5)
        frame_search.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        
        label_search  = Label(frame_search, text="Search Panel", font=("Arial", 14), bg="lightblue", width=10, height=2)
        label_search.grid(columnspan=2, row=0, pady=50)
        labele_title = Label(frame_search, text="Thí sinh nhập số báo \n danh và năm học ở dưới", font=("Arial", 14), bg="lightblue")
        labele_title.grid(columnspan=2, row = 1)

        labele_id = Label(frame_search, text="Số báo danh", font=("Arial", 14), bg="lightblue")
        labele_id.grid(column=0, row = 2)
        entry_id = Entry(frame_search, font=('Arial', 9))
        entry_id.grid(column=1, row = 2, pady= 20)

        labele_term = Label(frame_search, text="Năm học", font=("Arial", 14), bg="lightblue")
        labele_term.grid(column=0, row = 3)
        entry_term = Entry(frame_search, font=('Arial', 9))
        entry_term.grid(column=1, row = 3, pady= 10)

        button_search = Button(frame_search, text = 'Xác nhận',command=on_confirm_click )
        button_search.grid(column=1, row = 4)

        # # Frame chứa thông tin sinh viên và điểm các môn
        frame_display = Frame(frame_content, bg="lightgray")
        frame_display.pack(side=RIGHT, fill=BOTH,expand=TRUE, padx=5, pady=5)
        label_title = Label(frame_display , text="Thông tin cá nhân", font=("Arial", 14),justify='center')
        label_title.grid(columnspan=5, row=0 , pady=20)

        # Hiển thị thô cho từng môn học (dùng pack thay vì grid)
        label_math = Label(frame_display, text="Toán", font=("Arial", 12), bg="lightgray")
        label_math.grid(column=0, row=1)
        entry_math = Entry(frame_display, font=('Arial', 12))
        entry_math.grid(column=1, row=1)

        label_physics = Label(frame_display, text="Lý", font=("Arial", 12), bg="lightgray")
        label_physics.grid(column=0, row=2)
        entry_physics = Entry(frame_display, font=('Arial', 12))
        entry_physics.grid(column=1, row=2)

        label_chemistry = Label(frame_display, text="Hóa", font=("Arial", 12), bg="lightgray")
        label_chemistry.grid(column=0, row=3)
        entry_chemistry = Entry(frame_display, font=('Arial', 12))
        entry_chemistry.grid(column=1, row=3)

        label_literature = Label(frame_display, text="Văn", font=("Arial", 12), bg="lightgray")
        label_literature.grid(column=0, row=4)
        entry_literature = Entry(frame_display, font=('Arial', 12))
        entry_literature.grid(column=1, row=4)

        label_english = Label(frame_display, text="Tiếng Anh", font=("Arial", 12), bg="lightgray")
        label_english.grid(column=0, row=5)
        entry_english = Entry(frame_display, font=('Arial', 12))
        entry_english.grid(column=1, row=5)

        label_biology = Label(frame_display, text="Sinh", font=("Arial", 12), bg="lightgray")
        label_biology.grid(column=0, row=6)
        entry_biology = Entry(frame_display, font=('Arial', 12))
        entry_biology.grid(column=1, row=6)

        label_history = Label(frame_display, text="Sử", font=("Arial", 12), bg="lightgray")
        label_history.grid(column=0, row=7)
        entry_history = Entry(frame_display, font=('Arial', 12))
        entry_history.grid(column=1, row=7)

        label_geography = Label(frame_display, text="Địa", font=("Arial", 12), bg="lightgray")
        label_geography.grid(column=0, row=8)
        entry_geography = Entry(frame_display, font=('Arial', 12))
        entry_geography.grid(column=1, row=8)

        label_gdcd = Label(frame_display, text="GDCD", font=("Arial", 12), bg="lightgray")
        label_gdcd.grid(column=0, row=9)
        entry_gdcd = Entry(frame_display, font=('Arial', 12))
        entry_gdcd.grid(column=1, row=9)
    elif content == 'Student List':
        # Xóa các widget cũ trong frame_content
        for widget in frame_content.winfo_children():
            widget.destroy()

        students = [
            {"name": "Nguyen A", "score": 8.5},
            {"name": "Le B", "score": 9.0},
            {"name": "Tran C", "score": 7.5},
            {"name": "Pham D", "score": 6.8},
            {"name": "Hoang E", "score": 8.0},
        ]
        
        # Hàm hiển thị bảng sinh viên và điểm
        def show_student_scores():
            # Xóa các widget cũ trong frame_display
            for widget in frame_display.winfo_children():
                widget.destroy()

            # Tạo tiêu đề bảng
            header = Frame(frame_display, bg="lightblue")
            header.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

            name_label = Label(header, text="Student Name", font=('Helvetica', 10, 'bold'))
            name_label.grid(row=0, column=0, padx=10, pady=5)

            score_label = Label(header, text="Score", font=('Helvetica', 10, 'bold'))
            score_label.grid(row=0, column=1, padx=10, pady=5)

            # Hiển thị thông tin sinh viên
            for i, student in enumerate(students, start=1):
                student_row = Frame(frame_display)
                student_row.grid(row=i, column=0, sticky="nsew", padx=5, pady=5)

                name = Label(student_row, text=student["name"], font=('Helvetica', 10))
                name.grid(row=0, column=0, padx=10, pady=5)

                score = Label(student_row, text=str(student["score"]), font=('Helvetica', 10))
                score.grid(row=0, column=1, padx=10, pady=5)

        # Đặt cấu hình của grid để phân chia tỷ lệ cột
        frame_content.grid_columnconfigure(0, weight=1)  # Cột 0 (frame_handle) chiếm 1 phần
        frame_content.grid_columnconfigure(1, weight=6)  # Cột 1 (frame_display) chiếm 4 phần

        # Tạo frame_handle chiếm 1/5 chiều rộng
        frame_handle = Frame(frame_content, bg="lightblue", bd=5)
        frame_handle.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)  # Sử dụng grid thay vì pack

        # Tạo các ô tính năng trong frame_handle
        buttons = [
            ("Feature 1", lambda: show_student_scores(), "icon_UI/hcmute.png"),
            ("Feature 2", lambda: print("Feature 2 clicked"), "icon_UI/home.png"),
            ("Feature 3", lambda: print("Feature 3 clicked"), "icon_UI/loupe.png"),
            ("Feature 4", lambda: print("Feature 4 clicked"), "icon_UI/group.png"),
            ("Feature 5", lambda: print("Feature 5 clicked"), "icon_UI/cells.png")
        ]
        
        for i, (text_content, command, icon_path) in enumerate(buttons, start=1):
            try:
                # Tải icon cho từng ô tính năng
                icon = PhotoImage(file=icon_path)
                icon = icon.subsample(20, 20)  # Điều chỉnh kích thước icon nếu cần
            except Exception as e:
                print(f"Không thể tải icon {icon_path}: {e}")
                icon = None

            # Tạo ô tính năng với icon và text
            button = Button(frame_handle,
                        text=text_content,
                        font=('Helvetica', 9),
                        fg="white",
                        bg="#000080",
                        width=20,
                        height=90,
                        anchor="center",
                        image=icon,  # Gắn icon vào label
                        command=command,
                        compound="top")  # Văn bản dưới icon
            button.grid(row=i, column=0, pady=5, padx=5, sticky="nsew")

            # Lưu tham chiếu đến icon để tránh mất ảnh
            if icon:
                button.image = icon

        # Đảm bảo các ô tính năng có thể giãn đầy đủ chiều dọc và chiều ngang
        frame_handle.grid_rowconfigure(0, weight=1)
        frame_handle.grid_columnconfigure(0, weight=1)
        
        # Tạo frame_display chiếm 4/5 chiều rộng
        frame_display = Frame(frame_content, bg="lightgray")
        frame_display.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)  # Sử dụng grid thay vì pack

# Cấu hình lưới chính
root.grid_rowconfigure(1, weight=1)  # Frame chính (nội dung)
root.grid_columnconfigure(1, weight=1)  # Frame nội dung chiếm không gian chính

# Tạo và hiển thị giao diện
makecenter(root)
create_features(root, change_content)
create_menu(root)
create_content(root )

root.mainloop()
