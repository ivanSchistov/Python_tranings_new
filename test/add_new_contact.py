# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_contact_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='John', middlename='S', lastname='Smith', nickname='JS', title='QQ', company='altego',
                       address='123', home='12456', mobile='123', email='123@ro.ru', homepage='www.site.com', bday='10',
                       bmonth='April', byear='1990', work='123', fax='1456987', email2='dad@gmail.com',
                       email3='dad1@gmail.com', aday='10', amonth='May', ayear='1989', address2='gadf12', phone2='123', notes='Hello!')
    app.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.lastname_or_max) == sorted(new_contacts, key=Contact.lastname_or_max)
    app.session.logout()

def test_add_new_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.open_contact_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname='', middlename='', lastname='', nickname='', title='', company='',
                       address='', home='', mobile='', email='', homepage='', bday='',
                       bmonth='', byear='', work='', fax='', email2='',
                       email3='', aday='', amonth='', ayear='', address2='', phone2='', notes='')
    app.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.lastname_or_max) == sorted(new_contacts, key=Contact.lastname_or_max)
    app.session.logout()

