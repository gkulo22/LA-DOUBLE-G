from django.db import models

class ATM(models.Model):
    five_gel_amount = models.IntegerField()
    ten_gel_amount = models.IntegerField()
    twenty_gel_amount = models.IntegerField()
    fifty_gel_amount = models.IntegerField()
    hundred_gel_amount = models.IntegerField()
    two_hundred_gel_amount = models.IntegerField()

    def __str__(self):
        return (f"5: {self.five_gel_amount}, "
                f"10: {self.ten_gel_amount}, "
                f"20: {self.twenty_gel_amount}, "
                f"50: {self.fifty_gel_amount}, "
                f"100: {self.hundred_gel_amount}, "
                f"200: {self.two_hundred_gel_amount}")

    def to_dict(self):
        return {
            '5': self.five_gel_amount,
            '10': self.ten_gel_amount,
            '20': self.twenty_gel_amount,
            '50': self.fifty_gel_amount,
            '100': self.hundred_gel_amount,
            '200': self.two_hundred_gel_amount,
        }
