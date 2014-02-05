# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Wed Feb  5 04:58:07 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from qt import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 656)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")
        self.fs2 = QtGui.QWidget()
        self.fs2.setObjectName("fs2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.fs2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gogextract = QtGui.QPushButton(self.fs2)
        self.gogextract.setObjectName("gogextract")
        self.verticalLayout_2.addWidget(self.gogextract)
        self.select = QtGui.QPushButton(self.fs2)
        self.select.setObjectName("select")
        self.verticalLayout_2.addWidget(self.select)
        self.fs2_bin = QtGui.QLabel(self.fs2)
        self.fs2_bin.setObjectName("fs2_bin")
        self.verticalLayout_2.addWidget(self.fs2_bin)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabs.addTab(self.fs2, "")
        self.mods = QtGui.QWidget()
        self.mods.setObjectName("mods")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.mods)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.modTree = QtGui.QTreeWidget(self.mods)
        self.modTree.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.modTree.setProperty("showDropIndicator", False)
        self.modTree.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.modTree.setAnimated(True)
        self.modTree.setExpandsOnDoubleClick(False)
        self.modTree.setObjectName("modTree")
        self.verticalLayout_3.addWidget(self.modTree)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.update = QtGui.QPushButton(self.mods)
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        self.apply_sel = QtGui.QPushButton(self.mods)
        self.apply_sel.setObjectName("apply_sel")
        self.horizontalLayout.addWidget(self.apply_sel)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabs.addTab(self.mods, "")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.aboutLabel = QtGui.QLabel(self.tab)
        self.aboutLabel.setObjectName("aboutLabel")
        self.verticalLayout_4.addWidget(self.aboutLabel)
        self.tabs.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 544, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mod Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.gogextract.setText(QtGui.QApplication.translate("MainWindow", "Install FS2 with the GOG installer", None, QtGui.QApplication.UnicodeUTF8))
        self.select.setText(QtGui.QApplication.translate("MainWindow", "Select installed FS2 (Open)", None, QtGui.QApplication.UnicodeUTF8))
        self.fs2_bin.setText(QtGui.QApplication.translate("MainWindow", "Selected FS2: ...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.fs2), QtGui.QApplication.translate("MainWindow", "FS2", None, QtGui.QApplication.UnicodeUTF8))
        self.modTree.setSortingEnabled(True)
        self.modTree.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.modTree.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.modTree.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.update.setText(QtGui.QApplication.translate("MainWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.apply_sel.setText(QtGui.QApplication.translate("MainWindow", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.mods), QtGui.QApplication.translate("MainWindow", "Mods", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutLabel.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Idea and implementation in Bash by Hellzed.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Port to Python by ngld.</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For feedback and updates go to:<br /><a href=\"http://www.hard-light.net/forums/index.php?topic=86364\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.hard-light.net/forums/index.php?topic=86364</span></a> (for now)</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Dependencies:</p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://python.org\"><span style=\" text-decoration: underline; color:#0000ff;\">Python</span></a> (2 or 3)</li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://qt-project.org/wiki/Category:LanguageBindings::PySide\"><span style=\" text-decoration: underline; color:#0000ff;\">PySide</span></a> or <a href=\"http://riverbankcomputing.co.uk/software/pyqt/intro\"><span style=\" text-decoration: underline; color:#0000ff;\">PyQt4</span></a></li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.7-zip.org/\"><span style=\" text-decoration: underline; color:#0000ff;\">7zip</span></a> (to extract downloaded archives)</li></ul></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
