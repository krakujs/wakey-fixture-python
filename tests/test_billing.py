from billing import get_idempotency_key


def test_legacy_order_without_key_returns_none():
    assert get_idempotency_key({}) is None
