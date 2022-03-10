def test_create_user(user, django_user_model):
    users = django_user_model.objects.all()
    assert len(users) == 2


def test_change_password(user):
    user.set_password('super_secret12')
    assert user.check_password('super_secret12') is True
