# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FilterWindow(object):
    def setupUi(self, FilterWindow):
        FilterWindow.setObjectName(_fromUtf8("FilterWindow"))
        FilterWindow.resize(554, 309)
        self.centralwidget = QtGui.QWidget(FilterWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.itt_btn = QtGui.QPushButton(self.centralwidget)
        self.itt_btn.setObjectName(_fromUtf8("itt_btn"))
        self.horizontalLayout.addWidget(self.itt_btn)
        self.itt_lbl = QtGui.QLabel(self.centralwidget)
        self.itt_lbl.setText(_fromUtf8(""))
        self.itt_lbl.setObjectName(_fromUtf8("itt_lbl"))
        self.horizontalLayout.addWidget(self.itt_lbl)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.destination_btn = QtGui.QPushButton(self.centralwidget)
        self.destination_btn.setObjectName(_fromUtf8("destination_btn"))
        self.horizontalLayout_3.addWidget(self.destination_btn)
        self.destination_lbl = QtGui.QLabel(self.centralwidget)
        self.destination_lbl.setText(_fromUtf8(""))
        self.destination_lbl.setObjectName(_fromUtf8("destination_lbl"))
        self.horizontalLayout_3.addWidget(self.destination_lbl)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        spacerItem6 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.filter_btn = QtGui.QPushButton(self.centralwidget)
        self.filter_btn.setObjectName(_fromUtf8("filter_btn"))
        self.horizontalLayout_2.addWidget(self.filter_btn)
        self.results_lbl = QtGui.QLabel(self.centralwidget)
        self.results_lbl.setText(_fromUtf8(""))
        self.results_lbl.setObjectName(_fromUtf8("results_lbl"))
        self.horizontalLayout_2.addWidget(self.results_lbl)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem8)
        FilterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FilterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        FilterWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FilterWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FilterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FilterWindow)
        QtCore.QMetaObject.connectSlotsByName(FilterWindow)

    def retranslateUi(self, FilterWindow):
        FilterWindow.setWindowTitle(_translate("FilterWindow", "itt Filter", None))
        self.label.setText(_translate("FilterWindow", "Locate the itt file to process:", None))
        self.itt_btn.setText(_translate("FilterWindow", "Browse...", None))
        self.label_2.setText(_translate("FilterWindow", "Select the destination for the filtered file:", None))
        self.destination_btn.setText(_translate("FilterWindow", "Browse...", None))
        self.filter_btn.setText(_translate("FilterWindow", "Filter itt", None))

