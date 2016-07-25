# -*- coding: utf-8 -*-
import time

import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_group(app):
        app.login(username="admin", password="secret")
        time.sleep(0.5)
        app.open_group_page()
        app.create_group(Group(group_name="test_group", header="qwerty", footer="qwerty"))
        app.logout()

def test_add_new_empty_group(app):
        app.login(username="admin", password="secret")
        app.open_group_page()
        app.create_group(Group(group_name="", header="", footer=""))
        app.logout()

