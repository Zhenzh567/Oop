class Discount:
    def __init__(self, percent):
        self.percent = percent

    def __call__(self, price):
        return price * (1 - self.percent / 100)

    def __enter__(self):
        print("Скидка активирована")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Скидка закончилась")
