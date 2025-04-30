import sys

def fun(mul,url='old/npc_units.txt'):
    with open(url, 'r') as f:
        ls = f.readlines()

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

    for i in ls:
        if x in key:
            i = i.split('"')
            i[3] = str(int(i[3]) * mul)
            j = '"'.join(i)
            ls2.append(j)
            print(j, end='')
        else:
            ls2.append(i)
        x += 1

    with open('npc_units.txt', 'w') as f:
        f.writelines(ls2)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # 获取拖动的文件路径
        p = sys.argv[1]
        m = int(input('输入修改防御塔和基地生命的倍数：'))
        fun(m,p)
    else:
        m = int(input('输入修改防御塔和基地生命的倍数：'))
        fun(m)
    input("按回车键退出...")
