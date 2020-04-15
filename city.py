class City:
    def __init__(self):
        self.name = ""
        self.mayor = ""
        self.est = ""
        self.buildings = []

    # def add_buildings(self, buildings):
    #     self.buildings.extend(buildings)

    def add_building(self, building):
        self.buildings.append(building)