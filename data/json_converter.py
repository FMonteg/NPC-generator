import json
import os


project_prefix = "npc_"

file_name = "names"

table = { "Skaa" : ["Alagren (Gren)", "Andrewn (Drewn)", "Banden", "Baragen (Bareg)", "Bilgren (Bilg)", "Birchold (Birch)", "Burkwen (Burk)",
                    "Calden", "Camon", "Cladent (Clubs)", "Cormanson (Corm)", "Dannicken (Dan)", "Dockson (Dox)", "Dorningham (Dorn)",
                    "Dumé", "Erstwhem (Erst)", "Endibournes (Endi)", "Falstor", "Ferson (Fer)", "Garbeau (Gare)", "Habbender (Hab)",
                    "Hammond (Ham)", "Hutchine (Hutch)", "Jame", "Jelman", "Lestibournes (Spook)", "Kelsier (Kell)", "Manisteau (Mani)",
                    "Mennis", "Monymont (Money)", "Nureia (Nuri)", "Pallisten (Pally)", "Pharick (Fair)", "Philen (Lin)", "Quellion",
                    "Reen", "Rone", "Sallo", "Sastren", "Sordarm", "Sullewick (Sully)", "Tamenham (Tam)", "Tonnestor (Tone)", "Tulley",
                    "Yandam", "Yeden", "Yune", "Zolacaster (Zole)"],
         "Male" : ["Ashweather", "Barklaren", "Belmark", "Blarran", "Bornham", "Celler", "Damworth", "Derlem", "Dorran", "Eckham", "Enfram",
                    "Falcom", "Fallow", "Goradel", "Hyrum", "Jastes", "Joreau", "Ladrian", "Lemmelier", "Louik", "Milen", "Molsier", "Neuseu",
                    "Orreleum", "Pellikreau", "Postwick", "Purnow", "Ralston", "Rene", "Roussaw", "Samden", "Serneau", "Sorndeham",
                    "Straff", "Stroham", "Tanniker", "Tyden", "Yandrean", "Yomen", "Zane"],
         "Female" : ["Adassey", "Adelemay", "Allrianne", "Amyse", "Annika", "Bedula", "Beldre", "Bellere", "Carelee", "Cylee"
                     "Darialle", "Desirea", "Dromea", "Geriell", "Hersea", "Inrea", "Junella", "Kliss", "Krea", "Lamisse",
                     "Lariseau", "Marinesse", "Monelle", "Nebellea", "Olyeh", "Oralee", "Owandise", "Paramel", "Raynah",
                     "Reesee", "Rosalle", "Serray", "Shan", "Shellayah", "Talareu", "Tellaneau", "Uldaya", "Valette", "Veretta", "Wrayn"],
         "Family" : ["Ackroyal", "Artwar", "Barreneau", "Bondwarren", "Bylerum", "Cett", "Conrad", "Davenpleu", "Demoux", "Dilisteni", "Elariel",
                     "Entrone", "Erikeller", "Forrekellen", "Frandeu", "Frandren", "Gardre", "Geff enry", "Getrue", "Halbeck", "Hallieau",
                     "Hasting", "Hoff quarter", "Hordreu", "Larabeck", "Lekal", "Penrod", "Profoste", "Queade", "Randaller", "Rebou", "Renoux",
                     "Sandcrown", "Slowswift", "Tarnin", "Tekiel", "Tormander", "Urvon", "Venture", "Wardwick"],

}
    







file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), project_prefix+file_name+'.json')

with open(file_path, 'w') as json_file:
    json.dump(table, json_file, indent=4)