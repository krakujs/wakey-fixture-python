"""Fixture billing module."""


def get_idempotency_key(order: dict) -> str | None:
    return order.get("idempotency_key")
