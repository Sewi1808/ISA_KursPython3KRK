MAX_BEERS = 99
MIN_BEERS = 0

current_amount_of_beers = MAX_BEERS
message = '{} beczek piwa na polce stalo, jedna spadal {} zostalo'
# beers = range(99, 0, -1)
#
# while beers > 0:
#     print(f'{beers} beczek piwa na polce stalo, jedna spadal {beers -1} zostalo')

while current_amount_of_beers > MIN_BEERS:
    print(message.format(current_amount_of_beers,current_amount_of_beers -1))
    current_amount_of_beers -=1