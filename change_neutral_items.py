import sys


def fun(url='old/neutral_items.txt'):
    with open(url, 'r') as f:
        ls = f.readlines()

        ls2 = []
        for i in ls:
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

    with open('neutral_items.txt', 'w') as f:
        f.writelines(ls2)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # 获取拖动的文件路径
        url_ = sys.argv[1]
        print(f'url : {url_}')
        fun(url_)
    else:
        fun()
    input("按回车键退出...")
