import csv
import os

# define constant
SO = {
    "" : 0,
    "Sở Giáo dục và Đào tạo Hồ Chí Minh" : 1
}

PHONG = {
    "" : 0,
    "Phòng GDĐT quận 1" : 1,
    "Phòng GDĐT quận 2" : 2,
    "Phòng GDĐT quận 3" : 3,
    "Phòng GDĐT quận 4" : 4,
    "Phòng GDĐT quận 5" : 5,
    "Phòng GDĐT quận 6" : 6,
    "Phòng GDĐT quận 7" : 7,
    "Phòng GDĐT quận 8" : 8,
    "Phòng GDĐT quận 9" : 9,
    "Phòng GDĐT quận 10" : 10,
    "Phòng GDĐT quận 11" : 11,
    "Phòng GDĐT quận 12" : 12,
    "Phòng GDĐT Thủ Đức" : 13,
    "Phòng GDĐT Gò Vấp" : 14,
    "Phòng GDĐT Bình Tân" : 15,
    "Phòng GDĐT Tân Bình" : 16,
   "Phòng GDĐT Bình Thạnh" : 17,
    "Phòng GDĐT Tân Phú" : 18,
    "Phòng GDĐT Phú Nhuận" : 19,
    "Phòng GDĐT Củ Chi" : 20,
    "Phòng GDĐT Hóc Môn" : 21,
    "Phòng GDĐT Bình Chánh" : 22,
    "Phòng GDĐT Nhà Bè" : 23,
    "Phòng GDĐT Cần Giờ" : 24
}

LOAI_HINH = {
    "" : 0,
    "Công lập" : 1,
    "Tư thục" : 2,
    "Dân lập" : 3
}

LOAI_TRG = {
    "" : 0,
    "TT GDTX" : 1,
    "TT GDNN - GDTX (Sát nhập theo TTLT số 39/2015)" : 2,
    "Trường phổ thông" : 3,
    "Năng khiếu thể dục thể thao" : 4,
    "Trường chuyên" : 5,
    "Dân tộc bán trú" : 6
}

def main():

    with open(os.path.join("Phần 2", "out", "others.sql"), "a", encoding='utf8') as file:
        file.write("USE school;" + '\n' + '\n')
        for key in LOAI_TRG:
            script = "INSERT INTO loai_trg(ma, ten) VALUES(" + str(LOAI_TRG[key]) + ", " + "'" + key + "'" + ");"
            file.write(script + '\n')

        file.write('\n')

        for key in LOAI_HINH:
            script = "INSERT INTO loai_hinh(ma, ten) VALUES(" + str(LOAI_HINH[key]) + ", " + "'" + key + "'" + ");"
            file.write(script + '\n')
        
        file.write('\n')

        for key in PHONG:
            script = "INSERT INTO phong(ma, ten) VALUES(" + str(PHONG[key]) + ", " + "'" + key + "'" + ");"
            file.write(script + '\n')
    
        file.write('\n')

        for key in SO:
            script = "INSERT INTO so(ma, ten) VALUES(" + str(SO[key]) + ", " + "'" + key + "'" + ");"
            file.write(script + '\n')

    # define input/output paths
    names = ["gdtx", "mn", "tih", "thcs", "thpt"]
    paths = [os.path.join("Phần 2", "csv", name + ".csv") for name in names]
    outs = [os.path.join("Phần 2", "out", name + ".sql") for name in names]

    tables = {}

    for i in range(len(names)):
        tables[paths[i]] = names[i]

    # Running
    for (path, out) in zip(paths, outs):
        with open(out, "a", encoding='utf8') as file_out:
            with open(path, "r", encoding='utf8') as file:
                file_out.write("USE school;" + '\n' + '\n')
                reader = csv.DictReader(file)
                for row in reader:
                    script = ("INSERT INTO " + tables[path] + "(ma, ten, dc, so, phg, loai_hinh, loai_trg) VALUES (" + row['ma'] + ", " + 
                            "'" + row['ten'] + "'" + ", " + 
                            "'" + row['dc'] + "'" + ", " +
                            str(SO[row['so']]) + ", " +
                            str(PHONG[row['phong']]) + ", " +
                            str(LOAI_HINH[row['loai_hinh']]) + ", " +
                            str(LOAI_TRG[row['loai_trg']]) + ");"
                        )
                    file_out.write(script + '\n')

if __name__ == "__main__":
    main()