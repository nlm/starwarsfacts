# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import random

class SWQuoteGenerator(object):

    episodes = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    characters = [
        #'4-LOM',
        'Aayla Secura',
        'Admiral Ackbar',
        'Admiral Thrawn',
        'Ahsoka Tano',
        'Anakin Solo',
        'Anakin Skywalker',
        #'Asajj Ventress',
        'Aurra Sing',
        'Senator Bail Organa',
        'Barriss Offee',
        'Bastila Shan',
        'BB-8',
        'Ben Skywalker',
        #'Bib Fortuna',
        'Boba Fett',
        #'Bossk',
        #'Brakiss',
        'C-3PO',
        'Cad Bane',
        'Cade Skywalker',
        'Callista Ming',
        'Captain Rex',
        #'Carnor Jax',
        'Chewbacca',
        'Clone Commander Cody',
        'Count Dooku',
        'Darth Bane',
        'Darth Krayt',
        'Darth Malgus',
        'Darth Maul',
        'Darth Nihilus',
        'Darth Vader',
        'Dash Rendar',
        #'Dengar',
        #'Durge',
        'Emperor Palpatine',
        'Exar Kun',
        'Galen Marek',
        'General Crix Madine',
        'General Dodonna',
        'General Grievous',
        #'General Veers',
        #'Gilad Pellaeon',
        'Grand Moff Tarkin',
        'Greedo',
        'Han Solo',
        'IG 88',
        'Jabba The Hutt',
        'Jacen Solo',
        'Jaina Solo',
        'Jango Fett',
        'Jarael',
        #'Jerec',
        #'Joruus C\'Baoth',
        #'Ki-Adi-Mundi',
        #'Kir Kanos',
        #'Kit Fisto',
        #'Kueller',
        'Kyle Katarn',
        'Kylo Ren',
        #'Kyp Durron',
        'Lando Calrissian',
        'Leia Organa',
        'Luke Skywalker',
        #'Luminara Unduli',
        #'Lumiya',
        'Mace Windu',
        'Mara Jade',
        'Mission Vao',
        'Natasi Daala',
        #'Nom Anor',
        'Obi-Wan Kenobi',
        'Padmé Amidala',
        'Plo Koon',
        #'Pre Vizsla',
        'Prince Xizor',
        'Princess Leia',
        'Qui-Gon Jinn',
        'Quinlan Vos',
        'R2-D2',
        'Rahm Kota',
        #'Revan',
        #'Satele Shan',
        #'Savage Opress',
        #'Sebulba',
        'Shaak Ti',
        #'Talon Karrde',
        #'Ulic Qel-Droma',
        'Visas Marr',
        'Watto',
        #'Wedge Antilles',
        'Yoda',
        #'Zam Wesell',
        #'Zayne Carrick',
        #'Zuckuss',
    ]

    planets = [
        'Abregado-rae',
        'Adumar',
        'Agamar',
        'Alderaan',
        'Almania',
        'Ambria',
        'Atzerri',
        'AHCH-TO',
        'Base',
        'Bakura',
        'Bandomeer',
        'Bastion',
        'Bespin',
        'Brodo',
        'Bonadan',
        'Borleias',
        'Bothawui',
        'Brentaal',
        'Byss',
        'Carida',
        'Cato',
        'Chandrila',
        'Corellia',
        'Corulag',
        'Coruscant',
        'Cymoon',
        'Dac',
        'Dagobah',
        'Dantooine',
        'Dathomir',
        'Devaron',
        'Duro',
        'Dorin',
        'D\'Qar',
        'Endor',
        'Eriadu',
        'Etti',
        'Falleen',
        'Fondor',
        'Felucia',
        'Géonosis',
        'Glee',
        'Gyndine',
        'Hapes',
        'Honoghr',
        'Hoth',
        'Ilum',
        'Ithor',
        'Jabiim',
        'Jakku',
        'Kalarba',
        'Kamino',
        'Kashyyyk',
        'Kiffex',
        'Kiffy',
        'Klatooine',
        'Korriban',
        'Kothlis',
        'Kuat',
        'Kubindi',
        'Lothal',
        'Malastare',
        'Mandalore',
        'Mustafar',
        'Muunilist',
        'Mygeeto',
        'Myrkr',
        'Naboo',
        'Nal',
        'Nar',
        'Obroa-skai',
        'Onderon',
        'Ord',
        'Ossus',
        'Polis',
        'Ralltiir',
        'Raxus',
        'Rishi',
        'Rodia',
        'Ruusan',
        'Ryloth',
        'Saleucami',
        'Selonia',
        'Sernpidal',
        'Stewjon',
        'Sullust',
        'Sulon',
        'Talus',
        'Taris',
        'Tatooine',
        'Telos',
        'Tralus',
        'Trandosha',
        'Tython',
        'Takodana',
        'Umbara',
        'Utapau',
        'Vanqor',
        'Vjun',
        'Vortex',
        'Wayland',
        'Yaga',
        'Yavin',
        'Yinchorr',
        'Ylesia',
        'Ziost',
        'Zonama',
        'Zygerria',
    ]

    death_circumstances = [
        'eaten by a giant worm',
        'burned by a volcano',
        'crushed by an enormous rock',
        'falling from a mountain',
        'exploding in space',
        'eaten by desert creatures',
        'cut in half by a lightsaber',
        'bleeding to death',
        'force-choked',
        'eaten by ewoks',
        'killed by the jetpack explosion',
        'sucked in a blackhole',
        'absorbed by quicksands',
        'sliced by a laser beam',
        'shot by a storm trooper',
    ]

    creatures = [
        'an ewok',
        'a robot',
        'a giant worm',
        'a droid',
        'a space creature',
        'a lizard',
        'Jar-Jar Binks',
    ]

    roles = [
        'a Jedi',
        'a Sith',
        'a senator of the republic',
        'a bounty hunter',
        'a space pilote from the rebellion',
        'a space pirate',
        'a pod racer',
        'a sith lord',
        'a jedi master',
        'a stormtrooper',
    ]

    weapons = [
        'a lightsaber',
        'the death star',
        'a laser gun',
        'the force',
        'a spaceship',
    ]

    spoils = [
        'In Episode {episode}, {char1} kills {char2} on planet {planet} using {weapon}',
        'In Episode {episode}, it is revealed that {char1} is actually the father of {char2}',
        'In Episode {episode}, {char1}\'s starship is attacked by {char2} and its army, to get a grip on {char3}',
        'When {char1} fights {char2} in episode {episode}, {char3} has set up a trap to capture them both',
        '{char1} is actually seen in episode {episode}, secretly hiding under the identity of {char2}',
        'When {char1} fights {char2} on {planet}, nobody knows {char3} is responsible for it',
        'As {role}, {char1} builds {weapon} to obliterate {char2}\'s home planet {planet}',
        '{char1} is declared ruler of {planet} by {char2} in episode {episode}',
        '{char1} dies in episode {episode}, {circumstance} on {planet}',
        'In Episode {episode}, {char1} is shot by {char2} in a duel',
        '{char1} sacrifices its life to protect {char2} from {char3} on {planet}',
        '{char1} betrays {char2} and {char3} in episode {episode} and kills both of them with {weapon}',
        'In Episode {episode}, {char1}\'s real name is revealed to be {char2}',
        '{char1} is actually {creature}',
        '{char1} is actually {role}',
        'When {char1}\'s ship is intercepted by {char2}\'s detroyer, {char3} was hiding inside',
        'It is discovered in episode {episode} that {char1} had a secret child with {char2}: {char3}',
        'In Episode {episode}, {char1} betrays {char2}, abandoning him on {planet}',
        'In Episode {episode}, {char1} encouters {role}, fighting {creature} and saves {char2}\'s life',
        '{char1} placed {creature} to get rid of {char2}\'s ship during {planet}\'s battle in episode {episode}',
        '{char1} eats {creature} to survive a storm in episode {episode}',
        '{char1}\'s parents were killed by {char2} using {weapon} in episode {episode}',
        '{char1} actually smiled when {char2} was {circumstance} in episode {episode}',
        '{char1}, {circumstance}, just had the time to reveal that {char2} was {creature}',
        '{char1} was actually not {circumstance} in episode {episode}',
        'In Episode {episode}, {creature} became {char1}\'s friend during the long stay on {planet}',
        'In Episode {episode}, {char1} reveals that {char2} is indeed {role}',
        'One of {char1}\'s parents was {role}, who died during its childhood, {circumstance}',
        'The new Jedi master in episode {episode} was {role} seen at the beginning of the movie',
        'Episode {episode} reveals that {char1} was on the other side of the force from the very beginning',
        'After {char1} saves {char2} in the ancient ruins on planet {planet}, they are betrayed by {char3}',
        '{char1} dies accidentaly while playing with {weapon}',
        'In Episode {episode}, {char1} orders {char2} to infitrate the enemy by faking being {role}',
        '{char1} is secretly in love with {char2} since episode {episode}',
        'In Episode {episode}, {char1} tries to convice {char2} that {char3} is {role}',
    ]

    facts = [
        'The actors playing {char1}, {char2} and {char3} were harmed during {weapon} fight',
    ]

    def generate(self):
        return random.choice(self.facts + self.spoils).format(episode=random.choice(self.episodes),
                                                              char1=random.choice(self.characters),
                                                              char2=random.choice(self.characters),
                                                              char3=random.choice(self.characters),
                                                              planet=random.choice(self.planets),
                                                              circumstance=random.choice(self.death_circumstances),
                                                              creature=random.choice(self.creatures),
                                                              role=random.choice(self.roles),
                                                              weapon=random.choice(self.weapons))

def main():
    swg = SWQuoteGenerator()
    print(swg.generate())

if __name__ == '__main__':
    main()
