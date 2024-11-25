# dataProcess/checkID.py
import requests

# Viết các phần tử lại và đóng dấu xuống dòng (\n) để phân biệt các dòng
# Lưu ý mở ''' ''' để khởi tạo file text.txt trước, những lần sau đóng lại để tránh ghi đè
with open("text.txt", "w", encoding="utf-8") as file:
    file.write(
        "sbd,toan,ngu_van,ngoai_ngu,vat_li,hoa_hoc,sinh_hoc,lich_su,dia_li,gdcd\n"
    )

for i in range(2000001, 2000021):
    input_id = "0" + str(i)

    # URL của trang web cần lấy mã nguồn
    url = (
        "https://diemthi.vnexpress.net/index/detail/sbd/" + str(input_id) + "/year/2024"
    )

    # Gửi yêu cầu GET và lấy nội dung trang web
    response = requests.get(url)

    # Lưu mã nguồn vào biến data
    data = response.text

    # Mở file và ghi data vào file, với encoding utf-8 để tránh lỗi UnicodeEncodeError
    with open("raw_data.txt", "w", encoding="utf-8") as file:
        file.write(data)  # Ghi dữ liệu vào file

    # Mở file để đọc với encoding utf-8
    with open("raw_data.txt", "r", encoding="utf-8") as file:
        # Đọc page source code
        data = file.readlines()

    # Tách các dòng của data thành các phần tử của list để phân tích
    data = [line.strip() for line in data]  # loại bỏ khoảng trắng thừa

    # Xóa các phần trong các thẻ HTML
    for i in range(len(data)):
        tags = []
        begin = None
        for j in range(len(data[i])):
            if data[i][j] == "<":
                begin = j
            if data[i][j] == ">" and begin is not None:
                end = j
                tags.append(data[i][begin : end + 1])
                begin = None
        # Loại bỏ các thẻ HTML khỏi dòng
        for tag in tags:
            data[i] = data[i].replace(tag, "")

    # Xóa các kí tự khoảng trắng
    for i in range(len(data)):
        data[i].strip()

    # Xóa các kí tự trắng
    temp_data = []
    for i in range(len(data)):
        if data[i] != "":
            temp_data.append(data[i])
    data = temp_data

    # Tìm kiếm vị trí đầu tiên và cuối cùng của dữ liệu cần lấy
    for i in range(len(data)):
        # Toán là bắt đầu của điểm cần phân tích
        if data[i] == "Toán":
            index_start = i
        # Sinh học là môn cuối kỳ và ta cần lưu cả điểm của sinh học nên ta sẽ cộng 1
        if data[i] in ["Sinh học", "Giáo dục công dân"]:
            index_end = i + 1
    data = data[index_start : index_end + 1]

    # Xóa các \t thừa
    for i in range(len(data)):
        data[i] = data[i].strip("\t")

    # Thêm số báo danh vào đầu
    res = []
    # thêm số báo danh vào đầu
    res.append(input_id)
    # Khảo tạo count để ngoại lệ số báo danh bị lỗi
    count = 0
    # Thêm  các giá tri cần thiết
    for subject in [
        "Toán",
        "Ngữ văn",
        "Ngoại ngữ",
        "Vật lý",
        "Hóa học",
        "Sinh học",
        "Lịch sử",
        "Địa lý",
        "Giáo dục công dân",
    ]:
        if subject in data:
            score = data[data.index(subject) + 1]
            # Làm gọn điểm số
            if score.endswith(".00"):
                score = score[:-3]
            elif score.endswith("0"):
                score = score[:-1]
            res.append(score)
            count += 1
        else:
            res.append("")
    if count == 0:
        continue

    # Viết các phần tử lại và đóng dấu xuống dòng (\n) để phân biệt các dòng
    with open("text.txt", "a", encoding="utf-8") as file:
        for i in range(len(res)):
            if i == len(res) - 1:
                file.write(str(res[i]))
            else:
                file.write(str(res[i]) + ",")
        file.write("\n")
