import json
import os
from random import choice

# Set the working directory to the location of your project
project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)

class PNJ:
    def __init__(self, **kwargs):

        self.force = self.generate("forces")
        self.faiblesse = self.generate("faiblesses")
        self.manie = self.generate("manies")
        self.signe = self.generate("signes")
        self.caractere = self.generate("caracteres")
        self.qualite = self.generate("qualites")
        self.ideal = self.generate("ideaux")
        self.lien = self.generate("liens")

        pass

    def generate(self, trait):
        file_name = 'pnj_'+trait+'.json'
        with open(os.path.join('data', file_name), 'r') as json_file:
            table = json.load(json_file)

        alea = choice(list(table.values()))

        return alea

