"""Fixture billing module — contains an intentional KeyError bug."""


def get_idempotency_key(order: dict) -> str | None:
    # BUG: raises KeyError for legacy orders missing the key (should default to None)
    return order["idempotency_key"]
