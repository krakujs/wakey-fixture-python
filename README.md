# wakey-fixture-python

Intentionally buggy Python service used to verify the wakey fix loop
end-to-end (E1-T5). `get_idempotency_key` raises KeyError for orders
missing the key; the planted test expects `None`.
