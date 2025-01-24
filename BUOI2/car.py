# tao class car
class Xe:
    # attribute (thuoc tinh)
    # mau_sac = ""
    # gia = 0
    # so_cho_ngoi = 0
    # hang_xe = ""
    # constructor 
    def __init__(self, mau_sac, gia, hang_xe):
        self.mau_sac = mau_sac
        self.gia = gia
        self.hang_xe = hang_xe
        self.so_cho_ngoi = 7

# tao object
xeA = Xe(hang_xe='Toyota', gia=10000, mau_sac='Xanh den')
print(xeA.hang_xe)
xeB = Xe('', 0, '')
print(xeB.hang_xe)