from src.checkout import calculate_total

checks = [
    ("enormous discount", lambda: calculate_total([], 10**1000)),
    ("enormous unit price", lambda: calculate_total(
        [{"unit_price": 10**1000, "quantity": 1}]
    )),
]

for name, check in checks:
    try:
        check()
    except ValueError:
        print(f"PASS: {name} raises ValueError")
    except OverflowError:
        print(f"FAIL: {name} raises OverflowError")
    else:
        print(f"FAIL: {name} raises no exception")