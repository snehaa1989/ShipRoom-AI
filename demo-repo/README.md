# Fictional Checkout API

A small, standard-library-only Python project demonstrating checkout total
calculation for a fictional API. This is a deliberately vulnerable
release-candidate demo: input validation is intentionally incomplete so the
audit tests for invalid inputs fail.

## Project structure

- `src/checkout.py` — subtotal and discount calculation.
- `src/__init__.py` — marks `src` as a package.
- `tests/test_checkout.py` — standard-library `unittest` tests.

## Run the tests

From the project root, run:

```sh
python -m unittest discover -s tests -v
```

The regular calculation, discount, and empty-order tests pass. Tests expecting
`ValueError` for negative quantities, negative prices, or discounts outside
0–100 fail by design because this release-candidate demo does not validate
those inputs.
