class Changer:
    def __init__(self, file_path: str, save_path: str):
        self.file_path: str = file_path
        self.save_path: str = save_path
        self.cache: list = []

    def change(self):
        self.__read_file('npc_units.txt')
        # self.__change_tower_hp(2)
        self.__change_xp_gold(5, 4)
        self.__save_file('npc_units.txt')

        self.__read_file('neutral_items.txt')
        self.__change_neutral_items()
        self.__save_file('neutral_items.txt')

        self.__read_file('items.txt')
        self.__change_items()
        self.__save_file('items.txt')

    def __read_file(self, file_name: str):
        with open(rf'{self.file_path}/{file_name}', 'r') as f:
            self.cache = f.readlines()

    def __save_file(self, file_name):
        with open(rf'{self.save_path}/{file_name}', 'w') as f:
            f.writelines(self.cache)

    def __change_tower_hp(self, mul):
        ls2 = []
        x = 1
        key = [1928, 2025, 2122,  # Good Tower 1
               2219, 2316, 2414,  # Good Tower 2
               2512, 2608, 2705,  # Good Tower 3
               2803,  # Good Tower 4
               2901, 2998, 3094,  # Bad Tower 1
               3191, 3288, 3385,  # Bad Tower 2
               3482, 3579, 3676,  # Bad Tower 3
               3773,  # Bad Tower 4
               5535,  # Good Guys Fort
               5623,  # Bad Guys Fort
               ]

        for i in self.cache:
            if x in key:
                i = i.split('"')
                i[3] = str(int(i[3]) * mul)
                j = '"'.join(i)
                ls2.append(j)
                print(j, end='')
            else:
                ls2.append(i)
            x += 1

        self.cache = ls2

    def __change_xp_gold(self, k, k2):
        ls2 = []
        good = [
            # BountyXP, BountyGoldMin, BountyGoldMax
            549, 550, 551,  # npc_dota_creep_goodguys_ranged
            640, 641, 642,  # npc_dota_creep_goodguys_ranged_upgraded
            731, 732, 733,  # npc_dota_creep_goodguys_ranged_upgraded_mega
            1365, 1366, 1367,  # npc_dota_creep_goodguys_melee
            1456, 1457, 1458,  # npc_dota_creep_goodguys_flagbearer
            1547, 1548, 1549,  # npc_dota_creep_goodguys_melee_upgraded
            1637, 1638, 1639,  # npc_dota_creep_goodguys_flagbearer_upgraded
            1727, 1728, 1729,  # npc_dota_creep_goodguys_melee_upgraded_mega
            1817, 1818, 1819,  # npc_dota_creep_goodguys_flagbearer_upgraded_mega
        ]
        for x, i in enumerate(self.cache, 1):
            if x in good:
                i = i.split('"')
                i[3] = str(int(i[3]) * k)
                j = '"'.join(i)
                ls2.append(j)
                print(x, j, end='')
            elif 'BountyXP' in i or 'BountyGoldMin' in i or 'BountyGoldMax' in i:
                i = i.split('"')
                i[3] = str(int(i[3]) * k2)
                j = '"'.join(i)
                ls2.append(j)
                print(x, j, end='')
            else:
                ls2.append(i)
        self.cache = ls2

    def __change_neutral_items(self):
        ls2 = []
        for x, i in enumerate(self.cache, 1):
            if '"70:00"' in i:
                i = i.replace('"70:00"', '"25:00"')
                print(x, i, end='')
            elif '"5:00"' in i:
                i = i.replace('"5:00"', '"0:00"')
                print(x, i, end='')
            elif '"15:00"' in i:
                i = i.replace('"15:00"', '"5:00"')
                print(x, i, end='')
            elif '"25:00"' in i:
                i = i.replace('"25:00"', '"10:00"')
                print(x, i, end='')
            elif '"35:00"' in i:
                i = i.replace('"35:00"', '"15:00"')
                print(x, i, end='')
            elif '"60:00"' in i:
                i = i.replace('"60:00"', '"20:00"')
                print(x, i, end='')
            else:
                i = i
            ls2.append(i)
        self.cache = ls2

    def __change_items(self):
        # Hand of Midas
        ls2 = []
        for x, i in enumerate(self.cache, 1):
            if x == 3575:
                i = i.replace('2.1', '5')
                print(x, i, end='')
            elif x == 3576:
                i = i.replace('160', '1000')
                print(x, i, end='')
            ls2.append(i)
        self.cache = ls2


if __name__ == '__main__':
    c = Changer(r'npc', r'vpk/pak01_dir/scripts/npc')
    c.change()
