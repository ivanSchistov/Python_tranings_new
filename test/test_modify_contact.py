__author__ = 'ichistov'
from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test_contact'))
    app.contact.modify_first_contact()
