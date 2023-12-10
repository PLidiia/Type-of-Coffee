import sqlite3

from PyQt5.QtWidgets import QWidget

from UI.addEditCoffeeForm import Ui_Form


class ADD_CHANGE(QWidget, Ui_Form):
    def __init__(self, widg):
        super().__init__()
        self.widget = widg
        self.setupUi(self)
        self.con = sqlite3.connect('data/coffee.bd')
        self.add.clicked.connect(self.adding)
        self.atribute.clear()
        cur = self.con.cursor()
        data = cur.execute("SELECT id FROM info").fetchall()
        for item in range(len(data) - 1):
            self.atribute.addItem(data[item][0])
        self.save.clicked.connect(self.saving)
        self.back.clicked.connect(self.backing)

    def backing(self):
        menu = ADD_CHANGE(self.widget)
        self.widget.addWidget(menu)
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def saving(self):
        cur_column = self.atribute.currentText()
        id = self.save_id.text()
        name = self.save_name.text()
        deg = self.save_degree.text()
        type = self.save_type.text()
        desc = self.save_descrpt.text()
        price = self.save_price.text()
        volume = self.save_volume.text()
        cur = self.con.cursor()
        cur.execute("UPDATE info SET ID = ?, name_sort = ?, degree_fried = ?, type = ?, "
                    "description = ?, price = ?, volume = ? WHERE id = ?",
                    (id, name, deg, type, desc, price, volume, cur_column))
        self.con.commit()

    def adding(self):
        cur = self.con.cursor()
        buttons_text = ['add_id', 'add_name', 'add_degree', 'add_type', 'add_descript', 'add_price', 'add_volume']
        texts = []
        text_cur = self.add_id.text()
        texts.append(text_cur)
        text_cur = self.add_name.text()
        texts.append(text_cur)
        text_cur = self.add_degree.text()
        texts.append(text_cur)
        text_cur = self.add_type.text()
        texts.append(text_cur)
        text_cur = self.add_descript.text()
        texts.append(text_cur)
        text_cur = self.add_price.text()
        texts.append(text_cur)
        text_cur = self.add_volume.text()
        texts.append(text_cur)
        print(texts)
        cur.execute("INSERT INTO info (ID, name_sort, degree_fried, type, description, price, volume) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)", (texts[0], texts[1], texts[2], texts[3], texts[4],
                                                     texts[5], texts[6]))
        self.con.commit()
