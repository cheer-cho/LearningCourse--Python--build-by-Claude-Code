from mod07_shop_pricing_impl import discounted


def cart_total(prices, percent_off=0):
    return round(sum(discounted(price, percent_off) for price in prices), 2)
