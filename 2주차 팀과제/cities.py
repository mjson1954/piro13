class City:
    def __init__(self, name, land_price=0, is_island=False):
        self.name = name
        self.land_price = land_price
        self.is_island = is_island
        self.has_apt = False
        self.has_house = False
        self.apt_price = int(self.land_price * 0.1)
        self.house_price = int(land_price * 0.05)
        self.toll = int(
            (self.land_price + self.apt_price + self.house_price) * 0.2)
        self.owner = 0

    def build_apt(self):
        self.has_apt = True

    def build_house(self):
        self.has_house = True
    
    def change_owner(self, player):
        self.owner = player


start = City("출발")
incheon = City("인천", 35)
gangwon = City("강원", 20)
gwangju = City("광주", 20)
quarantine = City("자가격리")
sejong = City("세종", 45)
busan = City("부산", 40)
golden_key = City("황금열쇠")
jeju = City("제주도", 30, is_island=True)
chungcheong = City("충청", 30)
ulsan = City("울산", 25)
daegu = City("대구", 30)
dokdo = City("독도", 50, is_island=True)
gyeonggi = City("경기", 40)
daejeon = City("대전", 25)
seoul = City("서울", 90)

cities = [start, incheon, gangwon, gwangju, quarantine, sejong, busan, golden_key, jeju,
          chungcheong, ulsan, daegu, dokdo, gyeonggi, daejeon, seoul]