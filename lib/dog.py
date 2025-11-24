APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    # ---- name property ----
    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, value):
        """Name must be a string between 1 and 25 characters in length"""
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            raise ValueError(
                "Name must be string between 1 and 25 characters."
            )

    # ---- breed property ----
    @property
    def breed(self):
        """The breed property"""
        return self._breed

    @breed.setter
    def breed(self, value):
        """Breed must be in the list of approved breeds"""
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            raise ValueError("Breed must be in list of approved breeds.")
