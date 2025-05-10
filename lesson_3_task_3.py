from address import Address
from mailing import Mailing
to_address = Address("123456", "Москва", "Ленина", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "20", "15")
mailing = Mailing(to_address=to_address, from_address=from_address, cost=250.0, track="AB123456789RU")
print(mailing)