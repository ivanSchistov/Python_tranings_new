__author__ = 'ichistov'
from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname='test_contact'))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New contact")
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.lastname_or_max) == sorted(new_contacts, key=Contact.lastname_or_max)


