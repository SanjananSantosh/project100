class ATM(object):
    def __init__(self, cardnumber, pinnumber):
        self.cardnumber=cardnumber
        self. pinnumber= pinnumber
        
    def cashWithdrawl(self):
        print("withdrawed")

    def balanceEnquiry(self):
        print("enquired")  

Atm1 =ATM(345425,4536)
Atm2 = ATM(737482,4562)

Atm1.cashWithdrawl()
Atm2.balanceEnquiry()

print(Atm1.pinnumber)
print(Atm1.cardnumber)
print(Atm2.pinnumber)
print(Atm2.cardnumber)

          


