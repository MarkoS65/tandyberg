# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tandylayout.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(929, 418)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.presetLayout = QtWidgets.QVBoxLayout()
        self.presetLayout.setObjectName("presetLayout")
        self.preset1 = QtWidgets.QPushButton(self.centralwidget)
        self.preset1.setObjectName("preset1")
        self.presetLayout.addWidget(self.preset1)
        self.preset2 = QtWidgets.QPushButton(self.centralwidget)
        self.preset2.setObjectName("preset2")
        self.presetLayout.addWidget(self.preset2)
        self.preset3 = QtWidgets.QPushButton(self.centralwidget)
        self.preset3.setObjectName("preset3")
        self.presetLayout.addWidget(self.preset3)
        self.preset4 = QtWidgets.QPushButton(self.centralwidget)
        self.preset4.setObjectName("preset4")
        self.presetLayout.addWidget(self.preset4)
        self.preset5 = QtWidgets.QPushButton(self.centralwidget)
        self.preset5.setObjectName("preset5")
        self.presetLayout.addWidget(self.preset5)
        self.preset6 = QtWidgets.QPushButton(self.centralwidget)
        self.preset6.setObjectName("preset6")
        self.presetLayout.addWidget(self.preset6)
        self.preset7 = QtWidgets.QPushButton(self.centralwidget)
        self.preset7.setObjectName("preset7")
        self.presetLayout.addWidget(self.preset7)
        self.preset8 = QtWidgets.QPushButton(self.centralwidget)
        self.preset8.setObjectName("preset8")
        self.presetLayout.addWidget(self.preset8)
        self.preset9 = QtWidgets.QPushButton(self.centralwidget)
        self.preset9.setObjectName("preset9")
        self.presetLayout.addWidget(self.preset9)
        self.preset10 = QtWidgets.QPushButton(self.centralwidget)
        self.preset10.setObjectName("preset10")
        self.presetLayout.addWidget(self.preset10)
        self.horizontalLayout.addLayout(self.presetLayout)
        self.slewLayout = QtWidgets.QGridLayout()
        self.slewLayout.setObjectName("slewLayout")
        self.upbutton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.upbutton.sizePolicy().hasHeightForWidth())
        self.upbutton.setSizePolicy(sizePolicy)
        self.upbutton.setMinimumSize(QtCore.QSize(60, 60))
        self.upbutton.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.upbutton.setFont(font)
        self.upbutton.setObjectName("upbutton")
        self.slewLayout.addWidget(self.upbutton, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.leftbutton = QtWidgets.QPushButton(self.centralwidget)
        self.leftbutton.setMinimumSize(QtCore.QSize(60, 60))
        self.leftbutton.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.leftbutton.setFont(font)
        self.leftbutton.setObjectName("leftbutton")
        self.slewLayout.addWidget(self.leftbutton, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.resetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.resetbutton.setMinimumSize(QtCore.QSize(60, 60))
        self.resetbutton.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.resetbutton.setFont(font)
        self.resetbutton.setObjectName("resetbutton")
        self.slewLayout.addWidget(self.resetbutton, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.downbutton = QtWidgets.QPushButton(self.centralwidget)
        self.downbutton.setMinimumSize(QtCore.QSize(60, 60))
        self.downbutton.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.downbutton.setFont(font)
        self.downbutton.setObjectName("downbutton")
        self.slewLayout.addWidget(self.downbutton, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.rightbutton = QtWidgets.QPushButton(self.centralwidget)
        self.rightbutton.setMinimumSize(QtCore.QSize(60, 60))
        self.rightbutton.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rightbutton.setFont(font)
        self.rightbutton.setObjectName("rightbutton")
        self.slewLayout.addWidget(self.rightbutton, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.slewLayout)
        self.zoomLayout = QtWidgets.QVBoxLayout()
        self.zoomLayout.setObjectName("zoomLayout")
        self.telebutton = QtWidgets.QPushButton(self.centralwidget)
        self.telebutton.setMinimumSize(QtCore.QSize(70, 50))
        self.telebutton.setMaximumSize(QtCore.QSize(70, 50))
        self.telebutton.setObjectName("telebutton")
        self.zoomLayout.addWidget(self.telebutton, 0, QtCore.Qt.AlignHCenter)
        self.widebutton = QtWidgets.QPushButton(self.centralwidget)
        self.widebutton.setMinimumSize(QtCore.QSize(70, 50))
        self.widebutton.setMaximumSize(QtCore.QSize(70, 50))
        self.widebutton.setObjectName("widebutton")
        self.zoomLayout.addWidget(self.widebutton)
        self.horizontalLayout.addLayout(self.zoomLayout)
        self.controlsLayout = QtWidgets.QGridLayout()
        self.controlsLayout.setObjectName("controlsLayout")
        self.wbslider = QtWidgets.QSlider(self.centralwidget)
        self.wbslider.setOrientation(QtCore.Qt.Vertical)
        self.wbslider.setObjectName("wbslider")
        self.controlsLayout.addWidget(self.wbslider, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.wblabel = QtWidgets.QLabel(self.centralwidget)
        self.wblabel.setObjectName("wblabel")
        self.controlsLayout.addWidget(self.wblabel, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.wbauto = QtWidgets.QPushButton(self.centralwidget)
        self.wbauto.setCheckable(True)
        self.wbauto.setObjectName("wbauto")
        self.controlsLayout.addWidget(self.wbauto, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.irisslider = QtWidgets.QSlider(self.centralwidget)
        self.irisslider.setOrientation(QtCore.Qt.Vertical)
        self.irisslider.setObjectName("irisslider")
        self.controlsLayout.addWidget(self.irisslider, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gainslider = QtWidgets.QSlider(self.centralwidget)
        self.gainslider.setOrientation(QtCore.Qt.Vertical)
        self.gainslider.setObjectName("gainslider")
        self.controlsLayout.addWidget(self.gainslider, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.focusauto = QtWidgets.QPushButton(self.centralwidget)
        self.focusauto.setCheckable(True)
        self.focusauto.setObjectName("focusauto")
        self.controlsLayout.addWidget(self.focusauto, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.exposureauto = QtWidgets.QPushButton(self.centralwidget)
        self.exposureauto.setCheckable(True)
        self.exposureauto.setChecked(False)
        self.exposureauto.setObjectName("exposureauto")
        self.controlsLayout.addWidget(self.exposureauto, 2, 1, 1, 2)
        self.focusslider = QtWidgets.QSlider(self.centralwidget)
        self.focusslider.setOrientation(QtCore.Qt.Vertical)
        self.focusslider.setObjectName("focusslider")
        self.controlsLayout.addWidget(self.focusslider, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.focuslabel = QtWidgets.QLabel(self.centralwidget)
        self.focuslabel.setEnabled(True)
        self.focuslabel.setObjectName("focuslabel")
        self.controlsLayout.addWidget(self.focuslabel, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.gainlabel = QtWidgets.QLabel(self.centralwidget)
        self.gainlabel.setObjectName("gainlabel")
        self.controlsLayout.addWidget(self.gainlabel, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.irislabel = QtWidgets.QLabel(self.centralwidget)
        self.irislabel.setObjectName("irislabel")
        self.controlsLayout.addWidget(self.irislabel, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gammalabel = QtWidgets.QLabel(self.centralwidget)
        self.gammalabel.setObjectName("gammalabel")
        self.controlsLayout.addWidget(self.gammalabel, 0, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.gammaslider = QtWidgets.QSlider(self.centralwidget)
        self.gammaslider.setOrientation(QtCore.Qt.Vertical)
        self.gammaslider.setObjectName("gammaslider")
        self.controlsLayout.addWidget(self.gammaslider, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.gammaauto = QtWidgets.QPushButton(self.centralwidget)
        self.gammaauto.setCheckable(True)
        self.gammaauto.setObjectName("gammaauto")
        self.controlsLayout.addWidget(self.gammaauto, 2, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.controlsLayout)
        self.togglesLayout = QtWidgets.QVBoxLayout()
        self.togglesLayout.setObjectName("togglesLayout")
        self.backlightbox = QtWidgets.QCheckBox(self.centralwidget)
        self.backlightbox.setObjectName("backlightbox")
        self.togglesLayout.addWidget(self.backlightbox)
        self.mirrorbox = QtWidgets.QCheckBox(self.centralwidget)
        self.mirrorbox.setObjectName("mirrorbox")
        self.togglesLayout.addWidget(self.mirrorbox)
        self.flipbox = QtWidgets.QCheckBox(self.centralwidget)
        self.flipbox.setObjectName("flipbox")
        self.togglesLayout.addWidget(self.flipbox)
        self.promptbox = QtWidgets.QCheckBox(self.centralwidget)
        self.promptbox.setObjectName("promptbox")
        self.togglesLayout.addWidget(self.promptbox)
        self.irctlbox = QtWidgets.QCheckBox(self.centralwidget)
        self.irctlbox.setObjectName("irctlbox")
        self.togglesLayout.addWidget(self.irctlbox)
        self.horizontalLayout.addLayout(self.togglesLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 26))
        self.menubar.setObjectName("menubar")
        self.menuSpeed = QtWidgets.QMenu(self.menubar)
        self.menuSpeed.setObjectName("menuSpeed")
        self.menuPort = QtWidgets.QMenu(self.menubar)
        self.menuPort.setObjectName("menuPort")
        self.menuSet_Preset = QtWidgets.QMenu(self.menubar)
        self.menuSet_Preset.setObjectName("menuSet_Preset")
        self.menuZoom_Speed = QtWidgets.QMenu(self.menubar)
        self.menuZoom_Speed.setObjectName("menuZoom_Speed")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.slews1 = QtWidgets.QAction(MainWindow)
        self.slews1.setCheckable(True)
        self.slews1.setObjectName("slews1")
        self.slews3 = QtWidgets.QAction(MainWindow)
        self.slews3.setCheckable(True)
        self.slews3.setChecked(False)
        self.slews3.setObjectName("slews3")
        self.slews5 = QtWidgets.QAction(MainWindow)
        self.slews5.setCheckable(True)
        self.slews5.setObjectName("slews5")
        self.slews7 = QtWidgets.QAction(MainWindow)
        self.slews7.setCheckable(True)
        self.slews7.setObjectName("slews7")
        self.slews9 = QtWidgets.QAction(MainWindow)
        self.slews9.setCheckable(True)
        self.slews9.setObjectName("slews9")
        self.slews11 = QtWidgets.QAction(MainWindow)
        self.slews11.setCheckable(True)
        self.slews11.setObjectName("slews11")
        self.slews13 = QtWidgets.QAction(MainWindow)
        self.slews13.setCheckable(True)
        self.slews13.setObjectName("slews13")
        self.slews15 = QtWidgets.QAction(MainWindow)
        self.slews15.setCheckable(True)
        self.slews15.setObjectName("slews15")
        self.spreset1 = QtWidgets.QAction(MainWindow)
        self.spreset1.setObjectName("spreset1")
        self.spreset2 = QtWidgets.QAction(MainWindow)
        self.spreset2.setObjectName("spreset2")
        self.spreset3 = QtWidgets.QAction(MainWindow)
        self.spreset3.setObjectName("spreset3")
        self.spreset4 = QtWidgets.QAction(MainWindow)
        self.spreset4.setObjectName("spreset4")
        self.spreset5 = QtWidgets.QAction(MainWindow)
        self.spreset5.setObjectName("spreset5")
        self.spreset6 = QtWidgets.QAction(MainWindow)
        self.spreset6.setObjectName("spreset6")
        self.spreset7 = QtWidgets.QAction(MainWindow)
        self.spreset7.setObjectName("spreset7")
        self.spreset8 = QtWidgets.QAction(MainWindow)
        self.spreset8.setObjectName("spreset8")
        self.spreset9 = QtWidgets.QAction(MainWindow)
        self.spreset9.setObjectName("spreset9")
        self.spreset10 = QtWidgets.QAction(MainWindow)
        self.spreset10.setObjectName("spreset10")
        self.zoomslow = QtWidgets.QAction(MainWindow)
        self.zoomslow.setCheckable(True)
        self.zoomslow.setObjectName("zoomslow")
        self.zoomfast = QtWidgets.QAction(MainWindow)
        self.zoomfast.setCheckable(True)
        self.zoomfast.setObjectName("zoomfast")
        self.menuSpeed.addAction(self.slews1)
        self.menuSpeed.addAction(self.slews3)
        self.menuSpeed.addAction(self.slews5)
        self.menuSpeed.addAction(self.slews7)
        self.menuSpeed.addAction(self.slews9)
        self.menuSpeed.addAction(self.slews11)
        self.menuSpeed.addAction(self.slews13)
        self.menuSpeed.addAction(self.slews15)
        self.menuSet_Preset.addAction(self.spreset1)
        self.menuSet_Preset.addAction(self.spreset2)
        self.menuSet_Preset.addAction(self.spreset3)
        self.menuSet_Preset.addAction(self.spreset4)
        self.menuSet_Preset.addAction(self.spreset5)
        self.menuSet_Preset.addAction(self.spreset6)
        self.menuSet_Preset.addAction(self.spreset7)
        self.menuSet_Preset.addAction(self.spreset8)
        self.menuSet_Preset.addAction(self.spreset9)
        self.menuSet_Preset.addAction(self.spreset10)
        self.menuZoom_Speed.addAction(self.zoomslow)
        self.menuZoom_Speed.addAction(self.zoomfast)
        self.menubar.addAction(self.menuSpeed.menuAction())
        self.menubar.addAction(self.menuZoom_Speed.menuAction())
        self.menubar.addAction(self.menuPort.menuAction())
        self.menubar.addAction(self.menuSet_Preset.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera Control"))
        self.preset1.setToolTip(_translate("MainWindow", "Recall Preset 1"))
        self.preset1.setText(_translate("MainWindow", "1"))
        self.preset2.setToolTip(_translate("MainWindow", "Recall Preset 2"))
        self.preset2.setText(_translate("MainWindow", "2"))
        self.preset3.setToolTip(_translate("MainWindow", "Recall Preset 3"))
        self.preset3.setText(_translate("MainWindow", "3"))
        self.preset4.setToolTip(_translate("MainWindow", "Recall Preset 4"))
        self.preset4.setText(_translate("MainWindow", "4"))
        self.preset5.setToolTip(_translate("MainWindow", "Recall Preset 5"))
        self.preset5.setText(_translate("MainWindow", "5"))
        self.preset6.setToolTip(_translate("MainWindow", "Recall Preset 6"))
        self.preset6.setText(_translate("MainWindow", "6"))
        self.preset7.setToolTip(_translate("MainWindow", "Recall Preset 7"))
        self.preset7.setText(_translate("MainWindow", "7"))
        self.preset8.setToolTip(_translate("MainWindow", "Recall Preset 8"))
        self.preset8.setText(_translate("MainWindow", "8"))
        self.preset9.setToolTip(_translate("MainWindow", "Recall Preset 9"))
        self.preset9.setText(_translate("MainWindow", "9"))
        self.preset10.setToolTip(_translate("MainWindow", "Recall Preset 10"))
        self.preset10.setText(_translate("MainWindow", "10"))
        self.upbutton.setToolTip(_translate("MainWindow", "Slew Up"))
        self.upbutton.setText(_translate("MainWindow", "🡅"))
        self.leftbutton.setToolTip(_translate("MainWindow", "Slew left"))
        self.leftbutton.setText(_translate("MainWindow", "🡄"))
        self.resetbutton.setToolTip(_translate("MainWindow", "Center and Rehome Servos"))
        self.resetbutton.setText(_translate("MainWindow", "✖"))
        self.downbutton.setToolTip(_translate("MainWindow", "Slew Down"))
        self.downbutton.setText(_translate("MainWindow", "🡇"))
        self.rightbutton.setToolTip(_translate("MainWindow", "Slew Right"))
        self.rightbutton.setText(_translate("MainWindow", "🡆"))
        self.telebutton.setToolTip(_translate("MainWindow", "Zoom Telephoto"))
        self.telebutton.setText(_translate("MainWindow", "Tele"))
        self.widebutton.setToolTip(_translate("MainWindow", "Zoom Wide"))
        self.widebutton.setText(_translate("MainWindow", "Wide"))
        self.wblabel.setText(_translate("MainWindow", "WB"))
        self.wbauto.setText(_translate("MainWindow", "Auto"))
        self.focusauto.setText(_translate("MainWindow", "Auto"))
        self.exposureauto.setText(_translate("MainWindow", "Auto"))
        self.focuslabel.setText(_translate("MainWindow", "Focus"))
        self.gainlabel.setText(_translate("MainWindow", "Gain"))
        self.irislabel.setText(_translate("MainWindow", "Iris"))
        self.gammalabel.setText(_translate("MainWindow", "Gamma"))
        self.gammaauto.setText(_translate("MainWindow", "Auto"))
        self.backlightbox.setText(_translate("MainWindow", "Backlight"))
        self.mirrorbox.setText(_translate("MainWindow", "Mirror"))
        self.flipbox.setText(_translate("MainWindow", "Flip"))
        self.promptbox.setText(_translate("MainWindow", "Prompt Light"))
        self.irctlbox.setText(_translate("MainWindow", "IR Control"))
        self.menuSpeed.setTitle(_translate("MainWindow", "Slew Speed"))
        self.menuPort.setTitle(_translate("MainWindow", "Port"))
        self.menuSet_Preset.setTitle(_translate("MainWindow", "Set Preset"))
        self.menuZoom_Speed.setTitle(_translate("MainWindow", "Zoom Speed"))
        self.slews1.setText(_translate("MainWindow", "1"))
        self.slews3.setText(_translate("MainWindow", "3"))
        self.slews5.setText(_translate("MainWindow", "5"))
        self.slews7.setText(_translate("MainWindow", "7"))
        self.slews9.setText(_translate("MainWindow", "9"))
        self.slews11.setText(_translate("MainWindow", "11"))
        self.slews13.setText(_translate("MainWindow", "13"))
        self.slews15.setText(_translate("MainWindow", "15"))
        self.spreset1.setText(_translate("MainWindow", "1"))
        self.spreset2.setText(_translate("MainWindow", "2"))
        self.spreset3.setText(_translate("MainWindow", "3"))
        self.spreset4.setText(_translate("MainWindow", "4"))
        self.spreset5.setText(_translate("MainWindow", "5"))
        self.spreset6.setText(_translate("MainWindow", "6"))
        self.spreset7.setText(_translate("MainWindow", "7"))
        self.spreset8.setText(_translate("MainWindow", "8"))
        self.spreset9.setText(_translate("MainWindow", "9"))
        self.spreset10.setText(_translate("MainWindow", "10"))
        self.zoomslow.setText(_translate("MainWindow", "Low"))
        self.zoomfast.setText(_translate("MainWindow", "High"))
