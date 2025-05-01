from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui.ab2 import Ui_MainWindow
from PyQt6.QtCore import QStringListModel
from script.ability_script import update_charge_restore, update_value_more, update_value
from script.tab_script import tab_up, tab_down
import os


class Win(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Edited')
        self.init()
        self.url = ''
        self.file_name = ''
        self.undo_board = ''
        self.clip_board = []

    def init(self):
        # act
        self.actionopen.triggered.connect(self.open_)
        self.actionopen_now.triggered.connect(self.open2_)
        self.actionsave.triggered.connect(self.save_)
        self.actionsave_as.triggered.connect(lambda: self.save_(save_as=1))
        # btn
        self.pushButton_2.clicked.connect(lambda: self.open_(reload=1))
        self.pushButton.clicked.connect(self.write_)
        self.pushButton_3.clicked.connect(lambda: self.write_(cd=1))
        self.pushButton_10.clicked.connect(lambda: self.write_(ch=1))
        self.pushButton_8.clicked.connect(self.save_)
        self.pushButton_7.clicked.connect(self.up_)
        self.pushButton_9.clicked.connect(self.down_)
        self.pushButton_6.clicked.connect(self.undo_)
        self.pushButton_5.clicked.connect(self.cut_)
        self.pushButton_4.clicked.connect(self.paste_)
        self.pushButton_11.clicked.connect(lambda: self.write_(va=0))
        self.pushButton_12.clicked.connect(lambda: self.write_(va=1))
        self.pushButton_15.clicked.connect(lambda: self.write_(va=2))
        self.pushButton_14.clicked.connect(lambda: self.write_(va=3))
        self.pushButton_16.clicked.connect(lambda: self.write_(va=4))
        self.pushButton_13.clicked.connect(lambda: self.write_(va=5))
        self.pushButton_17.clicked.connect(lambda: self.write_(va=6))
        self.pushButton_19.clicked.connect(lambda: self.write_(va=7))
        self.pushButton_18.clicked.connect(lambda: self.write_(va=9))

        # 快捷键
        self.actionopen.setShortcut('ctrl+o')
        self.actionopen_now.setShortcut('f1')
        self.actionsave.setShortcut('ctrl+s')
        self.actionsave_as.setShortcut('shift+ctrl+s')

        self.pushButton_7.setShortcut('tab')
        self.pushButton_9.setShortcut('backspace')
        self.pushButton.setShortcut('space')
        self.pushButton_3.setShortcut('d')
        self.pushButton_6.setShortcut('z')
        self.pushButton_5.setShortcut('x')
        self.pushButton_4.setShortcut('v')
        self.pushButton_2.setShortcut('r')
        self.pushButton_10.setShortcut('c')
        self.pushButton_11.setShortcut('0')
        self.pushButton_12.setShortcut('1')
        self.pushButton_15.setShortcut('2')
        self.pushButton_14.setShortcut('3')
        self.pushButton_16.setShortcut('4')
        self.pushButton_13.setShortcut('5')
        self.pushButton_17.setShortcut('6')
        self.pushButton_19.setShortcut('7')
        self.pushButton_18.setShortcut('9')

    def open2_(self):
        url = self.url
        try:
            os.startfile(url)
            self.statusbar.showMessage(f"已成功打开文件: {url}")
        except FileNotFoundError:
            self.statusbar.showMessage(f"文件未找到: {url}")
        except Exception as e:
            self.statusbar.showMessage(f"打开文件时出现错误: {e}")

    def open_(self, reload=0):
        if reload == 1:
            url = self.url
        else:
            url, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "文本文件 (*.txt);;所有文件 (*)")  # 打开文件管理器

        if url:
            with open(url, 'r', encoding='utf-8', errors='ignore') as f:
                ls = f.readlines()
            m = QStringListModel()  # 建立模型
            m.setStringList(ls)  # 写入内容至模型
            self.listView.setModel(m)  # lv绑定模型
            self.file_name = url.split('/')[-1]  # 记忆文件名
            self.url = url  # 记忆路径
            self.statusbar.showMessage(f'操作：载入数据成功，路径：{url}')
        else:
            self.statusbar.showMessage(f'操作：载入数据路径为空！')

    def dragEnterEvent(self, event):
        """允许拖拽文件"""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        """处理拖放事件"""
        url = [u.toLocalFile() for u in event.mimeData().urls()][0]
        if url:
            with open(url, 'r', encoding='utf-8', errors='ignore') as f:
                ls = f.readlines()
            m = QStringListModel()  # 建立模型
            m.setStringList(ls)  # 写入内容至模型
            self.listView.setModel(m)  # lv绑定模型
            self.listView.setStyleSheet("font-family: Consolas; font-size: 12px; font-weight: bold;")
            self.file_name = url.split('/')[-1]  # 记忆文件名
            self.url = url  # 记忆路径
            self.statusbar.showMessage(f'操作：载入数据成功，路径：{url}')

    def read_(self):
        """
        读取选中行
        :return: 模型，行索引，行内容
        """
        try:
            m = self.listView.model()  # 读模型，QStringListModel
            ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
            i = ls[0]  # <PyQt6.QtCore.QModelIndex>
            t = m.data(i)  # 读
            return m, i, t
        except Exception as e:
            self.statusbar.showMessage(f'操作：读取模型失败，错误：{e}')
            return None, None, None

    def write_(self, cd=0, ch=0, va=-1):
        """
        写入选中行
        :param cd: -25%
        :param ch: AbilityChargeRestoreTime
        :param va: =0, =1, +25%, +33%, +5, +50, +500,
        :return:
        """
        m, i, t = self.read_()  # 模型，行索引，行内容
        if not t:
            self.statusbar.showMessage(f'操作：写入模型失败，错误：内容为空')
        else:
            x = t
            try:
                if ch == 1:
                    x = update_charge_restore(x)
                else:
                    if 'value' in x:
                        x = update_value(x)
                    else:
                        x = update_value_more(x)

                    if cd == 1 or 'Cooldown' in x or 'ManaCost' in x or 'CastPoint' in x or 'RestoreTime' in x:
                        x = x.replace('+50%', '-25%')
                    elif va == 0:
                        x = x.replace('+50%', '=0')
                    elif va == 1:
                        x = x.replace('+50%', '=1')
                    elif va == 2:
                        x = x.replace('+50%', '+25%')
                    elif va == 3:
                        x = x.replace('+50%', '+33%')
                    elif va == 4:
                        x = x.replace('+50%', '+5')
                    elif va == 5:
                        x = x.replace('+50%', '+50')
                    elif va == 6:
                        x = x.replace('+50%', '+500')
                    elif va == 7:
                        x = x.replace('+50%', '+75%')
                    elif va == 9:
                        x = x.replace('+50%', '+100%')



                # 开始写入
                m.setData(i, x)  # 写
                self.undo_board = f'{t}'  # 备份原字段
            except Exception as e:
                self.statusbar.showMessage(f'操作：写入模型失败，错误：{e}')

    def save_(self, save_as=0):
        """保存文件"""
        if save_as == 1:
            url, _ = QFileDialog.getSaveFileName(self, "保存文件", self.file_name, "文本文件 (*.txt);;所有文件 (*)")
        else:
            url = self.url
        try:
            if url:
                with open(url, 'w') as f:
                    m = self.listView.model()  # 读模型，QStringListModel
                    row = m.rowCount()  # 共多少行
                    ls = []
                    for r in range(row):
                        i = m.index(r, 0)  # r行0列
                        tx = m.data(i)  # 内容
                        ls.append(tx)  # 写入列表
                    f.writelines(ls)  # 写
                self.url = url
                self.statusbar.showMessage(f'操作：保存数据成功，路径：{url}')
        except Exception as e:
            self.statusbar.showMessage(f'操作：保存数据失败，错误：{e}')

    def up_(self):
        m, i, t = self.read_()  # 模型，行索引，行内容
        if t:
            x = tab_up(t)
            m.setData(i, x)  # 写

    def down_(self):
        m, i, t = self.read_()  # 模型，行索引，行内容
        if t:
            x = tab_down(t)
            m.setData(i, x)  # 写

    def undo_(self):
        """撤回"""
        m, i, t = self.read_()
        if self.undo_board:
            m.setData(i, self.undo_board)  # 写
            self.statusbar.showMessage(f'操作：撤回成功')

    def cut_(self):
        """剪切"""
        m, i, t = self.read_()
        if not t:
            self.statusbar.showMessage(f'操作：剪切失败，错误：内容为空')
        else:
            self.clip_board.append(tab_up(t))  # 剪切
            m.setData(i, '')  # 删
            self.statusbar.showMessage(f'操作：剪切成功，剪切板次数：{len(self.clip_board)}')

    def paste_(self):
        """粘贴"""
        if not self.clip_board:
            self.statusbar.showMessage(f'操作：粘贴失败，剪切板为空')
        else:
            m, i, t = self.read_()
            if not i:
                self.statusbar.showMessage(f'操作：粘贴失败，错误：索引值为空')
            else:
                m.setData(i, t + '\n'.join(self.clip_board))  # 写
                self.clip_board = []  # 清空剪切板
                self.statusbar.showMessage(f'操作：粘贴成功')


if __name__ == '__main__':
    app = QApplication([])
    win = Win()
    win.show()
    app.exec()
