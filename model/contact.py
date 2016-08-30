from sys import maxsize

class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None, nickname=None, title=None, company=None, address=None, home=None,
                 mobile=None, email=None, homepage=None, bday=None, bmonth=None, byear=None, work=None, fax=None, email2=None, email3=None,
                 aday=None, amonth=None, ayear=None, address2=None, phone2=None, notes=None, all_phones_from_home_page=None):

        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.id = id
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.email = email
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.work = work
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page


    def __repr__(self):
        return "%s:%s" % (self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and self.firstname == other.firstname

    def lastname_or_max(self):
        if self.lastname:
            return int(self.lastname)
        else:
            return maxsize
