def price_after_discount(price: float, pct: float, tax: float) -> float:
    # Apply discount, then tax. Intentional gaps for teaching:
    # - No guard for pct < 0 or > 100
    # - Negative tax/price not checked
    # - Rounding policy unclear for currency
    discount = price * (pct / 100.0)
    after_discount = price - discount
    total = after_discount + (after_discount * tax)
    return round(total, 2)
