import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.browser import Ui_Form
from editor import Editor

class Browser(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 存储基础路径和完整文件列表
        self.base_path = "npc/heroes"
        self.all_files = []

        # 设置模型
        self.model = QtGui.QStandardItemModel()
        self.listView.setModel(self.model)

        # 初始化文件列表
        self.initialize_files()

        # 连接信号和槽
        self.lineEdit.textChanged.connect(self.filter_files)
        self.listView.doubleClicked.connect(self.on_double_click)

        # 禁用编辑功能
        self.listView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    def initialize_files(self):
        """初始化文件列表并显示"""
        try:
            # 确保路径存在
            if not os.path.exists(self.base_path):
                os.makedirs(self.base_path)

            # 获取所有文件
            self.all_files = []
            for root, _, files in os.walk(self.base_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, self.base_path)
                    self.all_files.append(relative_path)

            # 显示所有文件
            self.update_list_view(self.all_files)
        except Exception as e:
            print(f"初始化文件列表时出错: {e}")

    def update_list_view(self, files):
        """更新列表视图"""
        self.model.clear()
        for file in files:
            item = QtGui.QStandardItem(file)
            # 设置项目为不可编辑
            item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            self.model.appendRow(item)

    def filter_files(self, text):
        """根据文本过滤文件列表"""
        if not text:
            # 如果搜索框为空，显示所有文件
            self.update_list_view(self.all_files)
            return

        # 模糊搜索
        filtered_files = [file for file in self.all_files if text.lower() in file.lower()]
        self.update_list_view(filtered_files)

    def on_double_click(self, index):
        """处理双击事件"""
        if index.isValid():
            selected_file = self.model.data(index)
            full_path = os.path.join(self.base_path, selected_file)
            full_path = full_path.replace('\\','/')
            print(f"双击的文件路径: {full_path}")
            editor = Editor(full_path)
            editor.show()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Browser()
    window.show()
    sys.exit(app.exec_())    