
from CheckingAccount import CheckingAccount

if __name__ == "__main__":
    
    account1 = CheckingAccount("Paul LeBlanc","3rd Street AU,Maine",5004330,50.00)

    print('WELCOME TO UNITED BANK:')
    
    account1.credtitAccount(50.00)

    account1.debitAccount(350.00)

    account1.debitAccount(9.00)

    account1.showBalance()

