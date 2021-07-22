def price_formated(val):
    return f'R$ {val:.2f}'.replace('.', ',')

def cart_total_qtd(car):
    return sum([item['quantity'] for item in car.values()])

def cart_totals(car):
    return sum(
        [
            item.get('quantity_promotion_price')
            if item.get('quantity_promotion_price')
            else item.get('quantity_price')
            for item 
            in car.values()
        ]
    )