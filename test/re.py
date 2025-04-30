import sys

def print_file_info(file_path):
    try:
        # 打印文件路径
        print(f"文件路径: {file_path}")

        # 读取并打印文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("文件内容:")
            print(content)
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 未找到。")
    except Exception as e:
        print(f"发生未知错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # 获取拖动的文件路径
        file_path = sys.argv[1]
        print_file_info(file_path)
    else:
        # 提示用户手动输入文件路径
        file_path = input("没有拖动文件，请手动输入文件路径: ")
        if file_path:
            print_file_info(file_path)
        else:
            print("未输入有效的文件路径。")
        
    print("\n"*3)
    input('输入回车退出...')