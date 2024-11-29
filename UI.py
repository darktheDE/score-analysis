from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import plot.aveSco
import plot.commonPlot
import plot.heatmap
import plot.perHis
from utils.CRUD import CRUD
from itertools import islice
import subprocess
from tkinter import ttk 
from plot import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import plot
# Tạo cửa sổ chính
root = Tk()
root.title("Phân tích điểm thi 2024 và 2023 THPTQG HCM")

# Đặt kích thước cửa sổ cố định
window_width = 1200
window_height = 630

# Khai báo các frame toàn cục
frame_feature = None
frame_menu = None
frame_content = None
page =1
# Hàm để hiển thị màn hình ở giữa
def makecenter(root):
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (window_width // 2)
    y = (root.winfo_screenheight() // 2) - (window_height // 2) - 30
    root.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))

# Tạo các chức năng của Frame bên trái (Features)
def create_features(root, change_content_callback):
    global frame_feature
    frame_feature = Frame(root, bg="#000080" )
    frame_feature.grid(column=0, row=0, rowspan=2,sticky="nswe")  # Kéo dài toàn bộ chiều dọc

    # Đặt chiều rộng tối thiểu cho frame chứa các nút
    frame_feature.grid_columnconfigure(0, minsize=100)
    # Tạo danh sách nút bên dưới logo
    buttons = [
        ("\n \n ", lambda: change_content_callback(""), r"icon_UI\hcmute.png"),
        ("Home", lambda: change_content_callback("Home"), r"icon_UI\home.png"),
        ("Search", lambda: change_content_callback("Search"), r"icon_UI\loupe.png"),
        ("Student List", lambda: change_content_callback("Student List"), r"icon_UI\cells.png"),
        ("Chart", lambda: change_content_callback("Chart"), r"icon_UI\char.png"),
        ("Document", lambda: change_content_callback("Document"), r"icon_UI\documents.png"),
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
    Label(frame_menu, text = ' Chương trình phân tích điểm thi 2023 và 2024 THPTQG HCM ' , font=('Arial',20), fg= 'white', justify='center',
        bg="#104E8B").grid(column=0, row=0, padx=10, pady=5)

# Tạo nội dung (Nội dung chính)
def create_content(root):
    global frame_content
    frame_content = Frame(root, bg="white")
    frame_content.grid(column=1, row=1, sticky="nsew")
    def create_label_with_image(frame, row, col, image_file, text):
        # Tạo Label chính
        label = Label(frame, bg="lightblue", relief="solid")
        label.grid(column=col, row=row, padx=18, pady=5, sticky="nsew")  # Dùng sticky để giãn rộng Label
        
        # Thêm Label hiển thị thông tin vào Label
        text_label = Label(label, bg="lightblue", justify='left', anchor='w', text=text, font=('Arial', 9))
        text_label.grid(column=1, row=0, sticky="ns")  # sticky="nswe" giúp giãn Label theo cả chiều ngang và dọc

        # Thêm ảnh vào Label bên trong Label
        try:
            img = PhotoImage(file=image_file)
            img = img.subsample(5, 5)  # Thay đổi kích thước ảnh theo tỷ lệ
            img_info = Label(label, image=img, bg="lightblue")
            img_info.grid(column=0, row=0, sticky="nswe")  # Đặt ảnh vào vị trí cột 0, hàng 0 của label
            label.image = img  # Giữ tham chiếu đến ảnh để tránh mất ảnh
        except Exception as e:
            print(f"Không thể tải ảnh: {e}")

        return label

    for widget in frame_content.winfo_children():
        widget.destroy()

    # Tạo các label với ảnh và thông tin
    text_info='Tên: Phan Trọng Phú \n MSSV: 23133056 \n Nhiệm vụ: Thiết kế UI'
    create_label_with_image(frame_content, row=0, col=0, image_file= 'icon_UI/phu.png', 
                            text='Tên: Phan Trọng Phú \n MSSV: 23133056 \n Nhiệm vụ: Thiết kế UI')
    create_label_with_image(frame_content, row=1, col=0, image_file= 'icon_UI/qui.png',
                                text='Tên: Phan Trọng Quí \n MSSV: 23133061 \n Nhiệm vụ: Lọc và xử lý data')
    create_label_with_image(frame_content, row=2, col=0, image_file= 'icon_UI/hung.png', 
                            text='Tên: Đỗ Kiến Hưng \n MSSV: 23133030 \n Nhiệm vụ: Vẽ và xử lý biểu đồ')
    create_label_with_image(frame_content, row=0, col=1, image_file= 'icon_UI/khoa.png', 
                            text='Tên: Lê Đăng Khoa \n MSSV: 23133036 \n Nhiệm vụ: Xây dựng chức năng và CRUD')
    create_label_with_image(frame_content, row=1, col=1, image_file='icon_UI/danh.png',
                                text='Tên: Trần Thành Danh \n MSSV: 23133010 \n Nhiệm vụ: Xây dựng chức năng và CRUD')
    return frame_content

# Hàm để thay đổi nội dung khi nhấn nút
def change_content(content):
    #hàm khởi tạo đối tượng
    file_pa = CRUD(r'data\diem2023.csv')
    student_data = file_pa.read_score()
    # Hàm để tạo một Label với ảnh và thông tin
    def create_label_with_image(frame, row, col, image_file, text):
        # Tạo Label chính
        label = Label(frame, bg="lightblue", relief="solid")
        label.grid(column=col, row=row, padx=18, pady=5, sticky="nsew")  # Dùng sticky để giãn rộng Label
        
        # Thêm Label hiển thị thông tin vào Label
        text_label = Label(label, bg="lightblue", justify='left', anchor='w', text=text, font=('Arial', 9))
        text_label.grid(column=1, row=0, sticky="ns")  # sticky="nswe" giúp giãn Label theo cả chiều ngang và dọc

        # Thêm ảnh vào Label bên trong Label
        try:
            img = PhotoImage(file=image_file)
            img = img.subsample(5, 5)  # Thay đổi kích thước ảnh theo tỷ lệ
            img_info = Label(label, image=img, bg="lightblue")
            img_info.grid(column=0, row=0, sticky="nswe")  # Đặt ảnh vào vị trí cột 0, hàng 0 của label
            label.image = img  # Giữ tham chiếu đến ảnh để tránh mất ảnh
        except Exception as e:
            print(f"Không thể tải ảnh: {e}")

        return label

    for widget in frame_content.winfo_children():
        widget.destroy()

    if content == 'Home':

        # Tạo các label với ảnh và thông tin
        text_info='Tên: Phan Trọng Phú \n MSSV: 23133056 \n Nhiệm vụ: Thiết kế UI'
        create_label_with_image(frame_content, row=0, col=0, image_file= 'icon_UI/phu.png', 
                                text='Tên: Phan Trọng Phú \n MSSV: 23133056 \n Nhiệm vụ: Thiết kế UI')
        create_label_with_image(frame_content, row=1, col=0, image_file= 'icon_UI/qui.png',
                                 text='Tên: Phan Trọng Quí \n MSSV: 23133061 \n Nhiệm vụ: Lọc và xử lý data')
        create_label_with_image(frame_content, row=2, col=0, image_file= 'icon_UI/hung.png', 
                                text='Tên: Đỗ Kiến Hưng \n MSSV: 23133030 \n Nhiệm vụ: Vẽ và xử lý biểu đồ')
        create_label_with_image(frame_content, row=0, col=1, image_file= 'icon_UI/khoa.png', 
                                text='Tên: Lê Đăng Khoa \n MSSV: 23133036 \n Nhiệm vụ: Xây dựng chức năng và CRUD')
        create_label_with_image(frame_content, row=1, col=1, image_file='icon_UI/danh.png',
                                 text='Tên: Trần Thành Danh \n MSSV: 23133010 \n Nhiệm vụ: Xây dựng chức năng và CRUD')
    elif content == 'Search':
        # Nút xác nhận
        def on_confirm_click():
            # Lấy dữ liệu từ các entry
            student_id = entry_id.get()  # Số báo danh thí sinh từ Entry
            term = str(entry_term.get())  # Học kỳ từ Entry (nếu cần)

            # Kiểm tra học kỳ và đặt đúng đường dẫn file
            if term == '2023':
                file_path = r'data\diem2023.csv'
            elif term == '2024':
                file_path = r'data\diem2024.csv' 
            else:
                file_path = None  # Nếu không phải 2023 hoặc 2024, gán None

            # Nếu file_path là None thì không tiếp tục
            if file_path is None:
                print("Học kỳ không hợp lệ.")
                return

            # Tạo đối tượng CRUD và tìm kiếm sinh viên
            find_score = CRUD(file_path)
            student_data_find = find_score.find_by_sbd(student_id)

            # Kiểm tra nếu tìm thấy thí sinh
            if student_data_find:
                print("Thông tin thí sinh:", student_data_find)

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

                # Điền điểm vào các Entry
                entry_math.insert(0, student_data_find[1])
                entry_physics.insert(0, student_data_find[2])
                entry_chemistry.insert(0, student_data_find[3])
                entry_literature.insert(0, student_data_find[4])
                entry_english.insert(0, student_data_find[5])
                entry_biology.insert(0, student_data_find[6])
                entry_history.insert(0, student_data_find[7])
                entry_geography.insert(0, student_data_find[8])
                entry_gdcd.insert(0, student_data_find[9])
                
            else:
                print("Không tìm thấy thí sinh.")

        frame_search = Frame(frame_content, bg="lightblue", bd =5)
        frame_search.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        
        label_search  = Label(frame_search, text="Search Panel", font=("Arial", 14), bg="lightblue", width=10, height=2)
        label_search.grid(columnspan=2, row=0, pady=50, padx=80)
        labele_title = Label(frame_search, text="Thí sinh nhập số báo \n danh và năm học ở dưới", font=("Arial", 14), bg="lightblue")
        labele_title.grid(columnspan=2, row = 1, padx=30)

        labele_id = Label(frame_search, text="Số báo danh", font=("Arial", 14), bg="lightblue")
        labele_id.grid(column=0, row = 2, padx=30)
        entry_id = Entry(frame_search, font=('Arial', 9))
        entry_id.grid(column=1, row = 2, pady= 20, padx=30)

        labele_term = Label(frame_search, text="Năm học", font=("Arial", 14), bg="lightblue")
        labele_term.grid(column=0, row = 3, padx=30)
        entry_term = Entry(frame_search, font=('Arial', 9))
        entry_term.grid(column=1, row = 3, pady= 10)

        button_search = Button(frame_search, text = 'Xác nhận',command=on_confirm_click )
        button_search.grid(column=1, row = 4)

        # # Frame chứa thông tin sinh viên và điểm các môn
        frame_display = Frame(frame_content, bg="lightgray")
        frame_display.pack(side=RIGHT, fill=BOTH,expand=TRUE, padx=5, pady=5)
        label_title = Label(frame_display , text="Thông tin cá nhân", font=("Arial", 14),justify='center')
        label_title.grid(columnspan=5, row=0 , pady=20)

        # Hiển thị thô cho từng môn học
        label_math = Label(frame_display, text="Toán", font=("Arial", 12), bg="lightgray")
        label_math.grid(column=0, row=1)
        entry_math = Entry(frame_display, font=('Arial', 12))
        entry_math.grid(column=1, row=1)

        label_physics = Label(frame_display, text="Văn", font=("Arial", 12), bg="lightgray")
        label_physics.grid(column=0, row=2)
        entry_physics = Entry(frame_display, font=('Arial', 12))
        entry_physics.grid(column=1, row=2)

        label_chemistry = Label(frame_display, text="Ngoại ngữ", font=("Arial", 12), bg="lightgray")
        label_chemistry.grid(column=0, row=3)
        entry_chemistry = Entry(frame_display, font=('Arial', 12))
        entry_chemistry.grid(column=1, row=3)

        label_literature = Label(frame_display, text="Lý", font=("Arial", 12), bg="lightgray")
        label_literature.grid(column=0, row=4)
        entry_literature = Entry(frame_display, font=('Arial', 12))
        entry_literature.grid(column=1, row=4)

        label_english = Label(frame_display, text="Hóa", font=("Arial", 12), bg="lightgray")
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
    elif content == 'Chart':
        # Hàm chạy chương trình python từ tệp .py
        def run_program(file_path):
            try:
                # Sử dụng subprocess để chạy tệp Python
                subprocess.run(["python", file_path], check=True)
                messagebox.showinfo("Thông báo", f"Chương trình {file_path} đã chạy thành công!")
            except subprocess.CalledProcessError:
                messagebox.showerror("Lỗi", f"Không thể chạy chương trình {file_path}!")
            except Exception as e:
                messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {str(e)}")

        def run1():
            # path = 'plot/cmp_1comb.py'
            # run_program(path)
            plot.aveSco.plot_average_scores()
        def run2():
            # Tạo một cửa sổ mới khi run2() được gọi
            combobox_window = Toplevel(root)  # Mở cửa sổ mới
            combobox_window.title("Chọn lựa các quan hệ tương quan")
            combobox_window.geometry('300x100')

            # Tạo combo box với các lựa chọn
            combo = ttk.Combobox(combobox_window,width=35, values=["Ma trận tương quan giữa các môn 2024", 
                                                          "Ma trận tương quan giữa các môn 2023",
                                                          "Ma trận tương quan giữa các tổ hợp 2024",
                                                          "Ma trận tương quan giữa các tổ hợp 2023"])
            combo.pack(pady=20)

            # Gắn sự kiện cho combo box khi người dùng chọn một tùy chọn
            combo.bind("<<ComboboxSelected>>", lambda event: on_combobox_select_run2(combo, combobox_window))

        def on_combobox_select_run2(combo, combobox_window):
            # Lấy lựa chọn từ combo box
            selected_option = combo.get()
            data2023 = pd.read_csv(r"data\diem2023.csv")
            data2024 = pd.read_csv(r"data\diem2024.csv")
            # Kiểm tra lựa chọn và gọi hàm tương ứng
            if selected_option == "Ma trận tương quan giữa các môn 2024":
                plot.heatmap.heatmapSubject(data2024, 2024)
            elif selected_option == "Ma trận tương quan giữa các môn 2023":
                plot.heatmap.heatmapSubject(data2023, 2023)
            elif selected_option == "Ma trận tương quan giữa các tổ hợp 2024":
                plot.heatmap.heatmapComb(data2024, 2024)
            elif selected_option == "Ma trận tương quan giữa các tổ hợp 2023":
                plot.heatmap.heatmapComb(data2023, 2023)
            else:
                print("Lựa chọn không hợp lệ")
            combobox_window.destroy()  # Đóng cửa sổ combo box sau khi chọn

        def run3():
            path = 'plot/freqSub.py'
            run_program(path)

        def run4():
            path = 'plot/disCompa.py'
            run_program(path)

        def run5():
            # Tạo một cửa sổ mới khi run2() được gọi
            combobox_window = Toplevel(root)  # Mở cửa sổ mới
            combobox_window.title("Chọn môn")
            combobox_window.geometry('250x100')

            # Tạo combo box với các lựa chọn
            combo = ttk.Combobox(combobox_window, values=["Toan", "Van", "Ngoai ngu","Vat ly", "Hoa hoc", "Sinh hoc","Lich su", "Dia li","GDCD"])
            combo.pack(pady=20)

            # Gắn sự kiện cho combo box khi người dùng chọn một tùy chọn
            combo.bind("<<ComboboxSelected>>", lambda event: on_combobox_select_run5(combo, combobox_window))

            # Nút chạy để thực thi khi chọn một tùy chọn
            run_button = Button(combobox_window, text="Run", command=lambda: on_combobox_select_run5(combo, combobox_window))
            run_button.pack(pady=10)

        def on_combobox_select_run5(combo, combobox_window):
            # Lấy lựa chọn từ combo box
            selected_option = combo.get()
            # Kiểm tra lựa chọn và gọi hàm tương ứng
            #toan,ngu_van,Ngoai ngu",vat_li,hoa_hoc,sinh_hoc,lich_su,dia_li,gdcd
            #Toan", "Van", "Ngoai ngu","Vat ly", "Hoa hoc", "Sinh hoc","Lich su", "Dia li","GDCD"
            
            if selected_option == "Toan":
                plot.perHis.plot_percentage_histogram("toan")   
            elif selected_option == "Van":
                plot.perHis.plot_percentage_histogram("ngu_van") 
            elif selected_option == "Ngoai ngu":
                plot.perHis.plot_percentage_histogram("ngoai_ngu")   
            elif selected_option == "Vat ly":
                plot.perHis.plot_percentage_histogram("vat_li") 
            elif selected_option == "Hoa hoc":
                plot.perHis.plot_percentage_histogram("hoa_hoc") 
            elif selected_option == "Sinh hoc":
                plot.perHis.plot_percentage_histogram("sinh_hoc") 
            elif selected_option == "Lich su":
                plot.perHis.plot_percentage_histogram("lich_su") 
            elif selected_option == "Dia li":
                plot.perHis.plot_percentage_histogram("dia_li") 
            elif selected_option == "GDCD":
                plot.perHis.plot_percentage_histogram("gdcd")     
            else:
                print("Lựa chọn không hợp lệ")
            #combobox_window.destroy()  # Đóng cửa sổ combo box sau khi chọn
        def run6():
            # Tạo một cửa sổ mới khi run2() được gọi
            combobox_window = Toplevel(root)  # Mở cửa sổ mới
            combobox_window.title("Chọn môn hoặc tổ hợp")
            combobox_window.geometry('300x100')

            # Tạo combo box với các lựa chọn
            combo = ttk.Combobox(combobox_window, values=["2023:A00", "2023:A02", "2023:B00","2023:C00", "2023:C19", "2023:C20",
                                                          "2024:A00", "2024:A02", "2024:B00","2024:C00", "2024:C19", "2024:C20",
                                                          "2023:Toan", "2023:Van", "2023:Ngoai ngu","2023:Vat ly", "2023:Hoa hoc",
                                                          "2023:Sinh hoc","2023:Lich su", "2023:Dia li","2023:GDCD",
                                                          "2024:Toan", "2024:Van", "2024:Ngoai ngu","2024:Vat ly", "2024:Hoa hoc",
                                                          "2024:Sinh hoc","2024:Lich su", "2024:Dia li","2024:GDCD"])
            combo.pack(pady=20)

            # Gắn sự kiện cho combo box khi người dùng chọn một tùy chọn
            combo.bind("<<ComboboxSelected>>", lambda event: on_combobox_select_run6(combo, combobox_window))

            # Nút chạy để thực thi khi chọn một tùy chọn
            run_button = Button(combobox_window, text="Run", command=lambda: on_combobox_select_run6(combo, combobox_window))
            run_button.pack(pady=10)

        def on_combobox_select_run6(combo, combobox_window):
            # Lấy lựa chọn từ combo box
            selected_option = combo.get()
            # Ví dụ gọi hàm
            # plot_score_distribution_by_combination(data2024, "A00", 2024)

            # plot_score_distribution_by_subject(data2024, "ngu_van", 2024)

            # plot_score_distribution_pie(data2024, "A00", 2024)

            # plot_score_distribution_by_combinations(data2023, 2023)
             # Load dữ liệu
            data2023 = pd.read_csv(r"data\diem2023.csv")
            data2024 = pd.read_csv(r"data\diem2024.csv")

            # Ánh xạ lựa chọn vào hàm
            subject_mapping = {
                "Toan": "toan", "Van": "ngu_van", "Ngoai ngu": "ngoai_ngu", 
                "Vat ly": "vat_li", "Hoa hoc": "hoa_hoc", "Sinh hoc": "sinh_hoc",
                "Lich su": "lich_su", "Dia li": "dia_li", "GDCD": "gdcd"
            }
            combination_mapping = ["A00", "A02", "B00", "C00", "C19", "C20"]

            # Xử lý lựa chọn môn học
            for year, data in [(2023, data2023), (2024, data2024)]:
                for subject, code in subject_mapping.items():
                    if selected_option == f"{year}:{subject}":
                        plot.commonPlot.plot_score_distribution_by_subject(data, code, year)
                        print(f"Đã chọn môn {subject} năm {year}")
                        return

            # Xử lý lựa chọn tổ hợp
            for year, data in [(2023, data2023), (2024, data2024)]:
                for combination in combination_mapping:
                    if selected_option == f"{year}:{combination}":
                        plot.commonPlot.plot_score_distribution_pie(data, combination, year)
                        print(f"Đã chọn tổ hợp {combination} năm {year}")
                        return

            print("Lựa chọn không hợp lệ")

            combobox_window.destroy()  # Đóng cửa sổ combo box sau khi chọn
        
        # Xóa các widget cũ trong frame_content
        for widget in frame_content.winfo_children():
            widget.destroy()
        # Đặt cấu hình của grid để phân chia tỷ lệ cột
        frame_content.grid_columnconfigure(0, weight=1)  # Cột 0 (frame_handle) chiếm 1 phần
        frame_content.grid_columnconfigure(1, weight=6)  # Cột 1 (frame_display) chiếm 4 phần

        # Tạo frame_handle chiếm 1/5 chiều rộng
        frame_handle = Frame(frame_content, bg="lightblue", bd=5)
        frame_handle.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)  # Sử dụng grid thay vì pack
        # Tạo các ô tính năng trong frame_handle
        buttons = [
            ("Xu hướng điểm TB từng môn", lambda:run1(), "icon_UI/growth.png"),
            ("Ma trận tương quan", lambda: run2(), "icon_UI/matrix.png"),
            ("Phân bố điểm các tất cả môn THPT", lambda:run3(), "icon_UI/distribution.png"),
            ("Số lượng học sinh từng khung điểm", lambda:run4(), "icon_UI/graduation.png"),
            ("So sánh điểm các môn ở 2 năm", lambda: run5(), "icon_UI/cells.png"),
            ("Phổ điểm từng môn hoặc tổ hợp", lambda:  run6(), "icon_UI/range.png")
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
                        width=15,
                        height=73,
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
        frame_handle.grid_columnconfigure(0, weight=1,minsize=80)
        
        # Tạo frame_display chiếm 4/5 chiều rộng
        frame_display = Frame(frame_content, bg="lightgray")
        frame_display.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)  # Sử dụng grid thay vì pack
    elif content == 'Document':
        # Xóa các widget cũ trong frame_content
        for widget in frame_content.winfo_children():
            widget.destroy()
        # Đặt cấu hình của grid để phân chia tỷ lệ cột
        frame_content.grid_columnconfigure(0, weight=1)  # Cột 0 (frame_handle) chiếm 1 phần
        frame_content.grid_columnconfigure(1, weight=6)  # Cột 1 (frame_display) chiếm 4 phần

        # Tạo frame_handle chiếm 1/5 chiều rộng
        frame_handle = Frame(frame_content, bg="lightblue", bd=5)
        frame_handle.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)  # Sử dụng grid thay vì pack
        # Tạo các ô tính năng trong frame_handle
        buttons = [
            ("Thêm một sinh viên", lambda:run1(), "icon_UI/hcmute.png"),
            ("Xóa một sinh viên", lambda: run2(), "icon_UI/home.png"),
            ("Sắp  xếp", lambda:run3(), "icon_UI/loupe.png"),
            ("Chưa nâng cấp", lambda:run4(), "icon_UI/group.png"),
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
                        width=15,
                        height=80,
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
        frame_handle.grid_columnconfigure(0, weight=1,minsize=80)
        
        # Tạo frame_display chiếm 4/5 chiều rộng
        frame_display = Frame(frame_content, bg="lightgray")
        frame_display.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)  # Sử dụng grid thay vì pack
    elif content == 'Student List':
        # Xóa các widget cũ trong frame_content
        for widget in frame_content.winfo_children():
            widget.destroy()
        # Hàm hiển thị bảng sinh viên và điểm
        def show_student_scores():
            global page
            print(page)
            # Đảm bảo bạn có danh sách các môn học (subjects)
            subjects = ["toan", "ngu_van", "ngoai_ngu", "vat_li", "hoa_hoc", "sinh_hoc", "lich_su", "dia_li", "gdcd"]
            # Xóa các widget cũ trong frame_display
            for widget in frame_display.winfo_children():
                widget.destroy()
            

            # Tạo header cho các môn học
            header_row = Frame(frame_display)
            header_row.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

            name_subjects = ["Toán", "   Ngữ Văn", "Ngoại ngữ", "Vật lý", "  Hóa học", " Sinh học", "  Lịch sử", "  Địa lý", "      GDCD"]
            # Hiển thị tên các môn học trong header
            name_header = Label(header_row, text="SBD      ", font=('Helvetica', 10, 'bold'),width=9)
            name_header.grid(row=0, column=0, padx=10, pady=5)
            
            for j, subject in enumerate(name_subjects, start=1):
                subject_label = Label(header_row, text=subject, font=('Helvetica', 10, 'bold'))
                subject_label.grid(row=0, column=j, padx=10, pady=5)
            end_table = page * 10
            start_table = end_table -10
            # Hiển thị thông tin sinh viên
            for i, (sbd, score_dict) in enumerate(islice(student_data,start_table, end_table), start=1):
                student_row = Frame(frame_display)
                student_row.grid(row=i, column=0, sticky="nsew", padx=5, pady=5)

                # Hiển thị số báo danh
                name = Label(student_row, text=sbd, font=('Helvetica', 10))
                name.grid(row=0, column=0, padx=10, pady=5)

                # Hiển thị điểm cho từng môn học
                for j, subject in enumerate(subjects, start=1):
                    score = score_dict.get(subject)  # Lấy điểm từ score_dict theo môn học

                    # Nếu không có điểm, hiển thị 'N/A'
                    try:
                        # Kiểm tra nếu điểm hợp lệ (là số thực và trong khoảng 0-10)
                        score = float(score)  # Thử chuyển đổi điểm thành số thực
                        if score < 0 or score > 10:
                            score = 'N/A'
                    except (ValueError, TypeError):  # Nếu không thể chuyển đổi (chuỗi không phải là số)
                        score = 'N/A'

                    score_label = Label(student_row, text=str(score), font=('Helvetica', 10),width=7)
                    score_label.grid(row=0, column=j, padx=10, pady=5)

        def page_increase():
            global page
            page +=1
            show_student_scores()
        
        def page_decrease():
            global page
            if page > 1:
                page -= 1
            show_student_scores()

        def page_change():
            # Hiển thị hộp thoại yêu cầu người dùng nhập số trang
            new_page = simpledialog.askinteger("Nhập số trang", "Nhập số trang mới:")
            
            if new_page is None:
                return  # Người dùng nhấn 'Hủy'
            
            if new_page < 1:
                messagebox.showerror("Lỗi", "Số trang phải lớn hơn hoặc bằng 1!")
            else:
                global page
                page = new_page
                show_student_scores()  # Cập nhật lại bảng theo trang mới

        def page_reset():
            global page
            page = 1
            show_student_scores()



        # Đặt cấu hình của grid để phân chia tỷ lệ cột
        frame_content.grid_columnconfigure(0, weight=1)  # Cột 0 (frame_handle) chiếm 1 phần
        frame_content.grid_columnconfigure(1, weight=6)  # Cột 1 (frame_display) chiếm 4 phần

        # Tạo frame_handle chiếm 1/5 chiều rộng
        frame_handle = Frame(frame_content, bg="lightblue", bd=5)
        frame_handle.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)  # Sử dụng grid thay vì pack
        

        # Tạo các ô tính năng trong frame_handle
        buttons = [
            ("Hiển thị", lambda: show_student_scores(), "icon_UI/advertising.png"),
            ("Trang kế", lambda: page_increase(), "icon_UI/right-arrow.png"),
            ("Trang cũ", lambda: page_decrease(), "icon_UI/left-arrow.png"),
            ("Nhập trang", lambda: page_change(), "icon_UI/browser.png"),
            ("Làm mới", lambda: page_reset(), "icon_UI/arrow.png")
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
        frame_handle.grid_columnconfigure(0, weight=1,minsize=80)
        
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


