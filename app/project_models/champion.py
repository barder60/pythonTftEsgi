class Champion :
    def __init__(self, name, cost, traits, pngPath):
        self.name = name
        self.cost = cost
        self.traits = traits
        self.pngPath = pngPath

    def __str__(self):
        return self.name + " cout : " + str(self.cost) + " traits : " + " ".join(self.traits) + " lien png : " + self.pngPath
