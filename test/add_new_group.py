# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group.create(Group(name="test_group", header="qwerty", footer="qwerty"))


def test_add_new_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


