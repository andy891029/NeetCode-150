class wallet:
    def __init__(self,onwer_name: str):
        self.own = onwer_name
        self.start = 0
    def save(self,amount: int)-> None:
        if amount > 0:
            self.start += amount
            print(f"{self.own} 存入 {amount} 元")
    def take(self,amount:int)->int:
        if amount <= self.start:
            self.start -= amount
            return amount
        else:
            print(f"{self.own}沒錢!只剩下{self.start}")
            return 0
    def get_start(self) -> int:
        return self.start
my_wallet = wallet("xiao")
print(my_wallet.get_start())
my_wallet.save(500)
print(my_wallet.get_start())
my_wallet.take(200)

