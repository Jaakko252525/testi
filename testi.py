import random

class Dog:
    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill

    def showSkill(self):
        return f'{self.name} skill is {self.skill}'

class Band:
    def __init__(self, band_name, music_genre, number_of_gold_records=0, number_of_platinum_records=0):
        self.band_name = band_name
        self.music_genre = music_genre
        self.number_of_gold_records = number_of_gold_records
        self.number_of_platinum_records = number_of_platinum_records

    def set_number_of_gold_records(self, number):
        self.number_of_gold_records = number

    def set_number_of_platinum_records(self, number):
        self.number_of_platinum_records = number

    def is_active(self):
        return 'is active' if self.number_of_platinum_records > 0 else 'is not active'

    def __str__(self):
        return f'{self.band_name} ({self.music_genre}) - Gold Records: {self.number_of_gold_records}, Platinum Records: {self.number_of_platinum_records}'

class CoverBand(Band):
    def __init__(self, band_name, music_genre, covered_bands_and_performers=[]):
        super().__init__(band_name, music_genre)
        self.covered_bands_and_performers = covered_bands_and_performers

    def add_covered_band(self, band):
        self.covered_bands_and_performers.append(band)

    def get_covered_bands_and_performers(self):
        return self.covered_bands_and_performers

    def __str__(self):
        return f'{super().__str__()} - Covers: {", ".join(self.covered_bands_and_performers)}'

# Create instances of CoverBand and call its methods
cover_band = CoverBand("Cover Masters", "Variety", ["The Beatles", "Queen"])
cover_band.add_covered_band("Elvis Presley")
cover_band.set_number_of_gold_records(2)
cover_band.set_number_of_platinum_records(1)

print(cover_band)
print(f'{cover_band.band_name} {cover_band.is_active()}')
print(f'Covered Bands and Performers: {", ".join(cover_band.get_covered_bands_and_performers())}')

# Coin flipping function
def toss_coin():
    return random.choice(["Heads", "Tails"])

# Toss the coin 10, 20, and 50 times
for num_tosses in [10, 20, 50]:
    results = [toss_coin() for _ in range(num_tosses)]
    heads_count = results.count("Heads")
    tails_count = results.count("Tails")
    print(f'Tossing the coin {num_tosses} times - Heads: {heads_count}, Tails: {tails_count}')
