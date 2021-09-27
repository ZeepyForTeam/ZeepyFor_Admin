class Review():
    def __init__(self):
        self.communicationTendency = {
            "칼 같은 우리 사이, 비즈니스형": "BUSINESS",
            "따뜻해 녹아내리는 중! 친절형": "KIND",
            "자유롭게만 살아다오, 방목형": "GRAZE",
            "겉은 바삭 속은 촉촉! 츤데레형": "SOFTY",
            "할말은 많지만 하지 않을래요 :(": "BAD",
            "-": "UNKNOWN",
        }
        self.lessorGender = {
            "남성": "MALE",
            "여성": "MALE",
            "-": "UNKNOWN",
        }
        self.lessorAge = {
            "10대": "TEN",
            "20대": "TWENTY",
            "30대": "THIRTY",
            "40대": "FOURTY",
            "50대": "FIFTY",
            "60대": "SIXTY",
            "60대 이상": "SIXTY",
            "-": "UNKNOWN",
        }
        self.roomCount = {
            "1개": "ONE",
            "2개": "TWO",
            "3개": "THREEORMORE",
            "3개 이상": "THREEORMORE",
            "-": "UNKNOWN",
        }
        self.soundInsulation = {
            "좋아요": "GOOD",
            "적당해요": "PROPER",
            "별로에요": "BAD",
            "-": "UNKNOWN",
        }
        self.pest = {
            "없어요": "GOOD",
            "없음": "GOOD",
            "가끔 나와요": "PROPER",
            "많아요": "BAD",
            "-": "UNKNOWN",
        }
        self.lightning = {
            "좋아요": "GOOD",
            "적당해요": "PROPER",
            "별로에요": "BAD",
            "-": "UNKNOWN",
        }
        self.waterPressure = {
            "좋아요": "GOOD",
            "적당해요": "PROPER",
            "별로에요": "BAD",
            "-": "UNKNOWN",
        }
        self.furnitures = {
            "에어컨": "AIRCONDITIONAL", 
            "세탁기": "WASHINGMACHINE", 
            "침대": "BED",
            "옷장": "CLOSET", 
            "책상": "DESK", 
            "책장": "DESK",
            "냉장고": "REFRIDGERATOR",
            "인덕션": "INDUCTION", 
            "가스레인지": "BURNER", 
            "전자레인지": "MICROWAVE",
        }
        self.totalEvaluation = {
            "다음에도 여기 살고 싶어요!": "GOOD",
            "완전 추천해요!": "SOSO",
            "그닥 추천하지 않아요.": "BAD",
            "-": "UNKNOWN",
        }

    def return_furniture_list(self, furnitures):
        result = []
        if len(furnitures) == 0 or furnitures[0] == "-":
            return result
        for furniture in furnitures:
            result.append(self.furnitures[furniture])
        return result