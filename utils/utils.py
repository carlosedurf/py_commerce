def price_formated(val):
    return f'R$ {val:.2f}'.replace('.', ',')

def cart_total_qtd(car):
    return sum([item['quantity'] for item in car.values()])