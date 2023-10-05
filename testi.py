

class Dog:

    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill


    def showSKill(self):

        return f'dig {self.name} skill is {self.skill}'


class Band:
    def __init__(self, band_name, music_genre, number_of_gold_records= 0, number_of_platinum_records= 0):
        self.band_name = band_name
        self.music_genre = music_genre
        self.number_of_gold_records = number_of_gold_records
        self.number_of_platinum_records = number_of_platinum_records
    
    def set_number_of_gold_records(self, number):
        self.number_of_gold_records = number
    
    def set_number_of_platinum_records(self, number):
        self.number_of_platinum_records = number

    def is_active(self):
        return f' is active or is not active'

    def __str__(self):

        return f'{self.band_name} {self.music_genre} {self.number_of_gold_records} {self.number_of_platinum_records}'



dog_1 = Dog('jaakko', 23, 'fetching ball')


band_1 = Band('jaakkos band', 'classic')
print(band_1)
band_1.set_number_of_gold_records(number=5)

band_1.set_number_of_platinum_records(number=8)

print(band_1)
