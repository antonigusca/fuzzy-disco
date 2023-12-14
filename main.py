class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.population_density = self.population/self.area

    def check_if_big(self):
        return self.population >15000000 or self.area >3000000
    def compare_populatio_density(self, other_country):
        if self.population > other_country.population:
            print("hello")


