class Changer:
    def __init__(self, file_path: str, save_path: str):
        self.file_path: str = file_path
        self.save_path: str = save_path
        self.cache: list = []

    def change(self):
        self.__read_file('npc_units.txt')
        # self.__change_tower_hp(2)
        self.__change_xp_gold(4)
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

    def __change_xp_gold(self, mul):
        ls2 = []
        for i in self.cache:
            if 'BountyXP' in i or 'BountyGoldMin' in i or 'BountyGoldMax' in i:
                i = i.split('"')
                i[3] = str(int(i[3]) * mul)
                j = '"'.join(i)
                ls2.append(j)
                print(j, end='')
            else:
                ls2.append(i)
        self.cache = ls2

    def __change_neutral_items(self):
        ls2 = []
        for i in self.cache:
            if '"70:00"' in i:
                i = i.replace('"70:00"', '"25:00"')
                print(i)
            elif '"5:00"' in i:
                i = i.replace('"5:00"', '"0:00"')
                print(i)
            elif '"15:00"' in i:
                i = i.replace('"15:00"', '"5:00"')
                print(i)
            elif '"25:00"' in i:
                i = i.replace('"25:00"', '"10:00"')
                print(i)
            elif '"35:00"' in i:
                i = i.replace('"35:00"', '"15:00"')
                print(i)
            elif '"60:00"' in i:
                i = i.replace('"60:00"', '"20:00"')
                print(i)
            else:
                i = i
            ls2.append(i)
        self.cache = ls2

    def __change_items(self):
        # Hand of Midas
        ls2 = []
        for i, x in enumerate(self.cache):
            if i  == 3574:
                x = x.replace('2.1', '5')
                print(x)
            elif i == 3575:
                x = x.replace('160', '1000')
                print(x)
            ls2.append(x)
        self.cache = ls2


if __name__ == '__main__':
    c = Changer(r'npc', r'vpk/pak01_dir/scripts/npc')
    c.change()
