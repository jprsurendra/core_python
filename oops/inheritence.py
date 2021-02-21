# Single inheritence
class Apple:
    manufacturer = 'Apple Inc'
    contact_website = 'www.apple.com/contact'
    name = 'Apple'

    def contact_details(self):
        print('Contact us at ', self.contact_website)


class MacBook(Apple):
    def __init__(self):
        self.year_of_manufacture = 2018

    def manufacture_details(self):
        print('This MacBook was manufactured in {0}, by {1}.'
              .format(self.year_of_manufacture, self.manufacturer))


macbook = MacBook()
macbook.manufacture_details()


# Multiple inheritence
class OperatingSystem:
    multitasking = True
    name = 'Mac OS'


class MacTower(OperatingSystem, Apple):
    def __init__(self):
        if self.multitasking is True:
            print('Multitasking system')
        # if there are two superclasses with the sae attribute name
        # the attribute of the first inherited superclass will be called
        # the order of inhertence matters
        print('Name: {}'.format(self.name))


mactower = MacTower()


# Multilevel inheritence
class MusicalInstrument:
    num_of_major_keys = 12


class StringInstrument(MusicalInstrument):
    type_of_wood = 'Tonewood'


class Guitar(StringInstrument):
    def __init__(self):
        self.num_of_strings = 6
        print('The guitar consists of {0} strings,' +
              'it is made of {1} and can play {2} keys.'
              .format(self.num_of_strings,
                      self.type_of_wood, self.num_of_major_keys))


guitar = Guitar()