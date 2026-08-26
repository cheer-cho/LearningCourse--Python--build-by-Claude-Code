from ex02_class_attrs import Robot, Team


def test_first_robot_sets_count_to_one():
    Robot.count = 0
    Robot("R1")
    assert Robot.count == 1


def test_each_new_robot_increments_the_shared_count():
    Robot.count = 0
    Robot("R1")
    Robot("R2")
    Robot("R3")
    assert Robot.count == 3


def test_how_many_reflects_the_class_count():
    Robot.count = 0
    Robot("R1")
    Robot("R2")
    assert Robot.how_many() == 2


def test_robot_instances_do_not_shadow_the_class_counter():
    Robot.count = 0
    r1 = Robot("R1")
    Robot("R2")
    # r1.count reads the class attribute (no instance attribute exists)
    assert r1.count == 2


def test_two_teams_have_independent_member_lists():
    reds = Team("Reds")
    blues = Team("Blues")
    reds.add_member("Ada")
    assert reds.members == ["Ada"]
    assert blues.members == []


def test_adding_to_one_team_does_not_touch_another():
    reds = Team("Reds")
    blues = Team("Blues")
    blues.add_member("Bo")
    reds.add_member("Cy")
    assert blues.members == ["Bo"]
    assert reds.members == ["Cy"]
