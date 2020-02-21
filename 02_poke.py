# 发牌程序
# Cards Module
class Card():
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]         #牌面数字 1--13
    SUITS = ["梅", "方", "红", "黑"]                 #梅为梅花，方为方钻，红为红心，黑为黑桃

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank                            #指的是牌面数字 1--13
        self.suit = suit                            #suit指的是花色 
        self.is_face_up = face_up                   #是否显示牌正面，True为正面，False为牌背面

    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = 'XX'
        return rep

    def flip(self):                                 # 翻盘
        self.is_face_up = not self.is_face_up

    def pic_order(self):                            #牌的顺序号
        if self.rank=="A":
            FaceNum=1
        elif self.rank=="J":
            FaceNum=11       
        elif self.rank=="Q":
            FaceNum=12
        elif self.rank=="K":
            FaceNum=13
        else:
            FaceNum=int(self.rank) 
        if self.suit=="梅":
            Suit=1
        elif self.suit=="方":
            Suit=2
        elif self.suit=="红":
            Suit=3
        else:
            Suit=4
        return (Suit - 1) * 13 + FaceNum


class Hand():

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + '\t'
        else:
            rep = '无牌'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    @staticmethod
    def give(hand, other_hand, card):
        hand.cards.remove(card)
        other_hand.add(card)

class Poke(Hand):                                   # 可看作有52张牌的拍手，所以继承Hand
    
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 13):           # 默认没人13张牌
        for rounds in range(per_hand):
            for hand in hands:
                top_card = self.cards[0]
                self.cards.remove(top_card)
                hand.add(top_card)


if __name__ == '__main__':
    print('This is a module with classes for playing cards.')
    players = [Hand(),Hand(),Hand(),Hand()]
    poke1 = Poke()
    poke1.populate()                                # 生成一副牌
    poke1.shuffle()                                 # 洗牌
    poke1.deal(players, 13)                         # 每个玩家13张牌

    # 显示4位牌手的牌
    n = 1
    for hand in players:
        print('洗牌', n, end= ':')
        print(hand)
        n = n+1
    input('\nPress the enter key to exit.')