from ex02_fixtures import fake_clock, fresh_account, funded_account


def test_fresh_account_starts_at_zero_balance():
    assert fresh_account().balance == 0.0


def test_fresh_account_ids_are_unique():
    a = fresh_account()
    b = fresh_account()
    assert a.id != b.id


def test_funded_account_uses_given_balance():
    account = funded_account(250.0)
    assert account.balance == 250.0


def test_funded_account_ids_are_also_unique():
    a = funded_account(10.0)
    b = funded_account(10.0)
    assert a.id != b.id


def test_fresh_and_funded_share_the_same_id_sequence():
    a = fresh_account()
    b = funded_account(50.0)
    c = fresh_account()
    assert len({a.id, b.id, c.id}) == 3


def test_fake_clock_now_returns_start():
    clock = fake_clock(1_000.0)
    assert clock.now() == 1_000.0


def test_fake_clock_defaults_to_zero():
    assert fake_clock().now() == 0.0


def test_fake_clock_advance_moves_time_forward():
    clock = fake_clock(0.0)
    clock.advance(30.0)
    assert clock.now() == 30.0
    clock.advance(15.0)
    assert clock.now() == 45.0


def test_fake_clock_instances_are_isolated():
    first = fake_clock(100.0)
    second = fake_clock(100.0)
    first.advance(500.0)
    assert first.now() == 600.0
    assert second.now() == 100.0
