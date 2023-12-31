import sqlite3
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QStackedWidget

from UI.main import Ui_Form
from add_change import ADD_CHANGE


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect('data/coffee.bd')
        self.search_words.clicked.connect(self.searching)
        self.data_search.clicked.connect(self.pushing)
        self.add_change.clicked.connect(self.adding_changing)

    def adding_changing(self):
        menu = ADD_CHANGE(widget)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def pushing(self):
        text_combo = self.atribute.currentText()
        text_search = self.text_atr.text()
        cur = self.con.cursor()
        if text_combo == 'ID':
            dates_one_id = cur.execute("SELECT ID FROM info WHERE id = ?", (text_search,)).fetchone()
            dates = cur.execute("SELECT ID FROM info WHERE id = ?", (text_search,)).fetchall()
            dates_one_name_sort = cur.execute("SELECT name_sort FROM info WHERE id = ?", (text_search,)).fetchone()
            dates_one_degree = cur.execute("SELECT degree_fried FROM info WHERE id = ?", (text_search,)).fetchone()
            dates_one_type = cur.execute("SELECT type FROM info WHERE id = ?", (text_search,)).fetchone()
            dates_one_name_descr = cur.execute("SELECT description FROM info WHERE id = ?", (text_search,)).fetchone()
            dates_one_price = cur.execute("SELECT price FROM info WHERE id = ?", (text_search,)).fetchone()
            dates_one_volume = cur.execute("SELECT volume FROM info WHERE id = ?", (text_search,)).fetchone()
            if self.id and self.name and self.degree and self.type and self.descript and self.price and self.volume:
                self.count_data.setText(str(len(dates)))
                self.id.setText(str(dates_one_id[0]))
                self.name.setText(dates_one_name_sort[0])
                self.degree.setText(dates_one_degree[0])
                self.type.setText(dates_one_type[0])
                self.descript.setText(dates_one_name_descr[0])
                self.price.setText(dates_one_price[0])
                self.volume.setText(dates_one_volume[0])
        if text_combo == 'Название сорта':
            dates_one_id = cur.execute("SELECT ID FROM info WHERE name_sort = ?", (text_search,)).fetchone()
            print(dates_one_id[0])
            dates = cur.execute("SELECT ID FROM info WHERE name_sort = ?", (text_search,)).fetchall()
            dates_one_name_sort = cur.execute("SELECT name_sort FROM info WHERE name_sort = ?",
                                              (text_search,)).fetchone()
            dates_one_degree = cur.execute("SELECT degree_fried FROM info WHERE name_sort = ?",
                                           (text_search,)).fetchone()
            dates_one_type = cur.execute("SELECT type FROM info WHERE name_sort = ?",
                                         (text_search,)).fetchone()
            dates_one_name_descr = cur.execute("SELECT description FROM info WHERE name_sort = ?",
                                               (text_search,)).fetchone()
            dates_one_price = cur.execute("SELECT price FROM info WHERE name_sort = ?",
                                          (text_search,)).fetchone()
            dates_one_volume = cur.execute("SELECT volume FROM info WHERE name_sort = ?",
                                           (text_search,)).fetchone()
            if self.id and self.name and self.degree and self.type and self.descript and self.price and self.volume:
                self.count_data.setText(str(len(dates)))
                self.id.setText(str(dates_one_id[0]))
                self.name.setText(dates_one_name_sort[0])
                print(dates_one_name_sort[0])
                self.degree.setText(dates_one_degree[0])
                self.type.setText(dates_one_type[0])
                self.descript.setText(dates_one_name_descr[0])
                self.price.setText(dates_one_price[0])
                self.volume.setText(dates_one_volume[0])

        if text_combo == 'Степень обжарки':
            dates_one_id = cur.execute("SELECT ID FROM info WHERE degree_fried = ?", (text_search,)).fetchone()
            dates = cur.execute("SELECT ID FROM info WHERE degree_fried = ?", (text_search,)).fetchall()
            dates_one_name_sort = cur.execute("SELECT name_sort FROM info WHERE degree_fried = ?",
                                              (text_search,)).fetchone()
            dates_one_degree = cur.execute("SELECT degree_fried FROM info WHERE degree_fried = ?",
                                           (text_search,)).fetchone()
            dates_one_type = cur.execute("SELECT type FROM info WHERE degree_fried = ?",
                                         (text_search,)).fetchone()
            dates_one_name_descr = cur.execute("SELECT description FROM info WHERE degree_fried = ?",
                                               (text_search,)).fetchone()
            dates_one_price = cur.execute("SELECT price FROM info WHERE degree_fried = ?", (text_search,)).fetchone()
            dates_one_volume = cur.execute("SELECT volume FROM info WHERE degree_fried = ?", (text_search,)).fetchone()
            if self.id and self.name and self.degree and self.type and self.descript and self.price and self.volume:
                self.count_data.setText(str(len(dates)))
                self.id.setText(str(dates_one_id[0]))
                self.name.setText(dates_one_name_sort[0])
                self.degree.setText(dates_one_degree[0])
                self.type.setText(dates_one_type[0])
                self.descript.setText(dates_one_name_descr[0])
                self.price.setText(dates_one_price[0])
                self.volume.setText(dates_one_volume[0])

        if text_combo == 'Молотый/в зернах':
            dates_one_id = cur.execute("SELECT ID FROM info WHERE type = ?", (text_search,)).fetchone()
            dates = cur.execute("SELECT ID FROM info WHERE type = ?", (text_search,)).fetchall()
            dates_one_name_sort = cur.execute("SELECT name_sort FROM info WHERE type = ?", (text_search,)).fetchone()
            dates_one_degree = cur.execute("SELECT degree_fried FROM info WHERE type = ?", (text_search,)).fetchone()
            dates_one_type = cur.execute("SELECT type FROM info WHERE type = ?", (text_search,)).fetchone()
            dates_one_name_descr = cur.execute("SELECT description FROM info WHERE type = ?", (text_search,)).fetchone()
            dates_one_price = cur.execute("SELECT price FROM info WHERE type = ?", (text_search,)).fetchone()
            dates_one_volume = cur.execute("SELECT volume FROM info WHERE type = ?", (text_search,)).fetchone()
            if self.id and self.name and self.degree and self.type and self.descript and self.price and self.volume:
                self.count_data.setText(str(len(dates)))
                if dates_one_id and dates_one_volume and dates_one_degree and dates_one_name_descr \
                        and dates_one_type and dates_one_price and dates_one_name_sort:
                    self.id.setText(str(dates_one_id[0]))
                    self.name.setText(dates_one_name_sort[0])
                    self.degree.setText(dates_one_degree[0])
                    self.type.setText(dates_one_type[0])
                    self.descript.setText(dates_one_name_descr[0])
                    self.price.setText(dates_one_price[0])
                    self.volume.setText(dates_one_volume[0])

        if text_combo == 'Описание вкуса':
            dates_one_id = cur.execute("SELECT ID FROM info WHERE description = ?", (text_search,)).fetchone()
            dates = cur.execute("SELECT ID FROM info WHERE description = ?", (text_search,)).fetchall()
            dates_one_name_sort = cur.execute("SELECT name_sort FROM info WHERE description = ?",
                                              (text_search,)).fetchone()
            dates_one_degree = cur.execute("SELECT degree_fried FROM info WHERE description = ?",
                                           (text_search,)).fetchone()
            dates_one_type = cur.execute("SELECT type FROM info WHERE description = ?",
                                         (text_search,)).fetchone()
            dates_one_name_descr = cur.execute("SELECT description FROM info WHERE description = ?",
                                               (text_search,)).fetchone()
            dates_one_price = cur.execute("SELECT price FROM info WHERE description = ?", (text_search,)).fetchone()
            dates_one_volume = cur.execute("SELECT volume FROM info WHERE description = ?", (text_search,)).fetchone()
            if self.id and self.name and self.degree and self.type and self.descript and self.price and self.volume:
                self.count_data.setText(str(len(dates)))
                if dates_one_id and dates_one_volume and dates_one_degree and dates_one_name_descr \
                        and dates_one_type and dates_one_price and dates_one_name_sort:
                    self.id.setText(str(dates_one_id[0]))
                    self.name.setText(dates_one_name_sort[0])
                    self.degree.setText(dates_one_degree[0])
                    self.type.setText(dates_one_type[0])
                    self.descript.setText(dates_one_name_descr[0])
                    self.price.setText(dates_one_price[0])
                    self.volume.setText(dates_one_volume[0])

        if text_combo == 'Цена':
            dates_one_id = cur.execute("SELECT ID FROM info WHERE price = ?", (text_search,)).fetchone()
            dates = cur.execute("SELECT ID FROM info WHERE price = ?", (text_search,)).fetchall()
            dates_one_name_sort = cur.execute("SELECT name_sort FROM info WHERE price = ?",
                                              (text_search,)).fetchone()
            dates_one_degree = cur.execute("SELECT degree_fried FROM info WHERE price = ?", (text_search,)).fetchone()
            dates_one_type = cur.execute("SELECT type FROM info WHERE price = ?", (text_search,)).fetchone()
            dates_one_name_descr = cur.execute("SELECT description FROM info WHERE price = ?",
                                               (text_search,)).fetchone()
            dates_one_price = cur.execute("SELECT price FROM info WHERE price = ?", (text_search,)).fetchone()
            dates_one_volume = cur.execute("SELECT volume FROM info WHERE price = ?", (text_search,)).fetchone()
            self.count_data.setText(str(len(dates)))
            if self.id and self.name and self.degree and self.type and self.descript and self.price and self.volume:
                self.count_data.setText(str(len(dates)))
                if dates_one_id and dates_one_volume and dates_one_degree and dates_one_name_descr \
                        and dates_one_type and dates_one_price and dates_one_name_sort:
                    self.id.setText(str(dates_one_id[0]))
                    self.name.setText(dates_one_name_sort[0])
                    self.degree.setText(dates_one_degree[0])
                    self.type.setText(dates_one_type[0])
                    self.descript.setText(dates_one_name_descr[0])
                    self.price.setText(dates_one_price[0])
                    self.volume.setText(dates_one_volume[0])

        if text_combo == 'Объём упаковки':
            dates_one_id = cur.execute("SELECT ID FROM info WHERE volume = ?", (text_search,)).fetchone()
            dates = cur.execute("SELECT ID FROM info WHERE volume = ?", (text_search,)).fetchall()
            dates_one_name_sort = cur.execute("SELECT name_sort FROM info WHERE volume = ?", (text_search,)).fetchone()
            dates_one_degree = cur.execute("SELECT degree_fried FROM info WHERE volume = ?", (text_search,)).fetchone()
            dates_one_type = cur.execute("SELECT type FROM info WHERE volume = ?", (text_search,)).fetchone()
            dates_one_name_descr = cur.execute("SELECT description FROM info WHERE volume = ?",
                                               (text_search,)).fetchone()
            dates_one_price = cur.execute("SELECT price FROM info WHERE volume = ?",
                                          (text_search,)).fetchone()
            dates_one_volume = cur.execute("SELECT volume FROM info WHERE volume = ?", (text_search,)).fetchone()
            self.count_data.setText(str(len(dates)))
            if self.id and self.name and self.degree and self.type and self.descript and self.price and self.volume:
                self.id.setText(str(dates_one_id[0]))
                self.name.setText(dates_one_name_sort[0])
                self.degree.setText(dates_one_degree[0])
                self.type.setText(dates_one_type[0])
                self.descript.setText(dates_one_name_descr[0])
                self.price.setText(dates_one_price[0])
                self.volume.setText(dates_one_volume[0])

    def searching(self):
        self.data_find.clear()
        cur = self.con.cursor()
        text_line = self.words.text()
        dates = cur.execute("SELECT * FROM info WHERE description LIKE ?", ('%' + text_line + '%',)).fetchall()
        if not dates:
            self.data_find.addItem('По вашему запросу ничего не было найдено')
        else:
            for date in range(len(dates[0]) - 1):
                self.data_find.addItem(dates[0][date])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    widget = QStackedWidget()
    widget.addWidget(ex)
    widget.setFixedWidth(1500)
    widget.setFixedHeight(1500)
    widget.show()
    sys.__excepthook__ = except_hook
    sys.exit(app.exec())
