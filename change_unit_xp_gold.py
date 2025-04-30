import sys

def fun(mul,url='old/npc_units.txt'):
    with open(url, 'r') as f:
        ls = f.readlines()

    ls2 = []
    for i in ls:
        if 'BountyXP' in i or 'BountyGoldMin' in i or 'BountyGoldMax' in i:
            i = i.split('"')
            i[3] = str(int(i[3]) * mul)
            j = '"'.join(i)
            ls2.append(j)
            print(j, end='')
        else:
            ls2.append(i)

    with open('npc_units.txt', 'w') as f:
        f.writelines(ls2)


if __name__ == '__main__':
        if len(sys.argv) > 1:
            # 获取拖动的文件路径
            p = sys.argv[1]
            m = int(input('输入修改经验和金钱的倍数：'))
            fun(m,p)
        else:
            m = int(input('输入修改经验和金钱的倍数：'))
            fun(m)
        input("按回车键退出...")