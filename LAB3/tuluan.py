class QuanLiDiemHS:
    def __init__(self, hoten, lop, truong, diemtoan, diemanh, diemvan):
        self.hoten = hoten
        self.lop = lop
        self.truong = truong
        self.diemtoan = diemtoan
        self.diemvan = diemvan
        self.diemanh = diemanh


# tao object
hs1 = QuanLiDiemHS(
    hoten="Au Ngoc Diep", lop=0, truong="ABC", diemanh=5, diemvan=5, diemtoan=4
)
print(hs1.diemtoan)


class ToaDo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


#  tao object
tdA = ToaDo(x=7, y=4)
print(tdA.x)