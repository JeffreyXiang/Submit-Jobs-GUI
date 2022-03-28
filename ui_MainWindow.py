# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowvpJfmX.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(888, 900)
        self.actionSave_Config = QAction(MainWindow)
        self.actionSave_Config.setObjectName(u"actionSave_Config")
        self.actionLoad_Config = QAction(MainWindow)
        self.actionLoad_Config.setObjectName(u"actionLoad_Config")
        self.actionAuthor_Info = QAction(MainWindow)
        self.actionAuthor_Info.setObjectName(u"actionAuthor_Info")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setAutoFillBackground(True)
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_cluster = QGroupBox(self.tab)
        self.groupBox_cluster.setObjectName(u"groupBox_cluster")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_cluster.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_cluster)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget_cluster = QTabWidget(self.groupBox_cluster)
        self.tabWidget_cluster.setObjectName(u"tabWidget_cluster")
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50)
        self.tabWidget_cluster.setFont(font1)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.tableWidget_cluster = QTableWidget(self.tab_3)
        self.tableWidget_cluster.setObjectName(u"tableWidget_cluster")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget_cluster.sizePolicy().hasHeightForWidth())
        self.tableWidget_cluster.setSizePolicy(sizePolicy1)
        self.tableWidget_cluster.setFont(font1)
        self.tableWidget_cluster.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_cluster.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_5.addWidget(self.tableWidget_cluster)

        self.widget_3 = QWidget(self.tab_3)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(16)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_clusterlist = QPushButton(self.widget_3)
        self.pushButton_clusterlist.setObjectName(u"pushButton_clusterlist")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_clusterlist.sizePolicy().hasHeightForWidth())
        self.pushButton_clusterlist.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pushButton_clusterlist)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.comboBox_clustername = QComboBox(self.widget_3)
        self.comboBox_clustername.setObjectName(u"comboBox_clustername")

        self.horizontalLayout_2.addWidget(self.comboBox_clustername)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_gpus = QSpinBox(self.widget_3)
        self.spinBox_gpus.setObjectName(u"spinBox_gpus")
        sizePolicy2.setHeightForWidth(self.spinBox_gpus.sizePolicy().hasHeightForWidth())
        self.spinBox_gpus.setSizePolicy(sizePolicy2)
        self.spinBox_gpus.setMinimumSize(QSize(64, 0))

        self.horizontalLayout_2.addWidget(self.spinBox_gpus)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.tabWidget_cluster.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_2 = QWidget(self.tab_4)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy4)
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setSpacing(16)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 9, 0, -1)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_3.addWidget(self.label_12)

        self.comboBox_singularityvirtualcluster = QComboBox(self.widget)
        self.comboBox_singularityvirtualcluster.addItem("")
        self.comboBox_singularityvirtualcluster.addItem("")
        self.comboBox_singularityvirtualcluster.addItem("")
        self.comboBox_singularityvirtualcluster.setObjectName(u"comboBox_singularityvirtualcluster")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox_singularityvirtualcluster.sizePolicy().hasHeightForWidth())
        self.comboBox_singularityvirtualcluster.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.comboBox_singularityvirtualcluster)

        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_14)

        self.lineEdit_singularityinstancetype = QLineEdit(self.widget)
        self.lineEdit_singularityinstancetype.setObjectName(u"lineEdit_singularityinstancetype")

        self.horizontalLayout_3.addWidget(self.lineEdit_singularityinstancetype)

        self.label_13 = QLabel(self.widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_13)

        self.comboBox_singularityslatier = QComboBox(self.widget)
        self.comboBox_singularityslatier.addItem("")
        self.comboBox_singularityslatier.addItem("")
        self.comboBox_singularityslatier.addItem("")
        self.comboBox_singularityslatier.setObjectName(u"comboBox_singularityslatier")
        self.comboBox_singularityslatier.setFont(font1)

        self.horizontalLayout_3.addWidget(self.comboBox_singularityslatier)


        self.verticalLayout_7.addWidget(self.widget)

        self.label_singularityhelp = QLabel(self.widget_2)
        self.label_singularityhelp.setObjectName(u"label_singularityhelp")
        sizePolicy4.setHeightForWidth(self.label_singularityhelp.sizePolicy().hasHeightForWidth())
        self.label_singularityhelp.setSizePolicy(sizePolicy4)
        self.label_singularityhelp.setOpenExternalLinks(True)

        self.verticalLayout_7.addWidget(self.label_singularityhelp)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.tabWidget_cluster.addTab(self.tab_4, "")

        self.verticalLayout_3.addWidget(self.tabWidget_cluster)


        self.verticalLayout.addWidget(self.groupBox_cluster)

        self.groupBox_storage = QGroupBox(self.tab)
        self.groupBox_storage.setObjectName(u"groupBox_storage")
        self.groupBox_storage.setFont(font)
        self.formLayout = QFormLayout(self.groupBox_storage)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(16)
        self.label_3 = QLabel(self.groupBox_storage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_accountname = QLineEdit(self.groupBox_storage)
        self.lineEdit_accountname.setObjectName(u"lineEdit_accountname")
        self.lineEdit_accountname.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_accountname)

        self.label_4 = QLabel(self.groupBox_storage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_containername = QLineEdit(self.groupBox_storage)
        self.lineEdit_containername.setObjectName(u"lineEdit_containername")
        self.lineEdit_containername.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_containername)

        self.label_5 = QLabel(self.groupBox_storage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_datastorename = QLineEdit(self.groupBox_storage)
        self.lineEdit_datastorename.setObjectName(u"lineEdit_datastorename")
        self.lineEdit_datastorename.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_datastorename)

        self.label_6 = QLabel(self.groupBox_storage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_accountkey = QLineEdit(self.groupBox_storage)
        self.lineEdit_accountkey.setObjectName(u"lineEdit_accountkey")
        self.lineEdit_accountkey.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_accountkey)


        self.verticalLayout.addWidget(self.groupBox_storage)

        self.groupBox_environment = QGroupBox(self.tab)
        self.groupBox_environment.setObjectName(u"groupBox_environment")
        self.groupBox_environment.setFont(font)
        self.groupBox_environment.setFlat(False)
        self.groupBox_environment.setCheckable(False)
        self.formLayout_2 = QFormLayout(self.groupBox_environment)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(16)
        self.label_7 = QLabel(self.groupBox_environment)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.lineEdit_dockerimage = QLineEdit(self.groupBox_environment)
        self.lineEdit_dockerimage.setObjectName(u"lineEdit_dockerimage")
        self.lineEdit_dockerimage.setFont(font1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_dockerimage)


        self.verticalLayout.addWidget(self.groupBox_environment)

        self.groupBox_experiment = QGroupBox(self.tab)
        self.groupBox_experiment.setObjectName(u"groupBox_experiment")
        self.groupBox_experiment.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox_experiment)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.label_8 = QLabel(self.groupBox_experiment)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_experiment)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)

        self.lineEdit_expname = QLineEdit(self.groupBox_experiment)
        self.lineEdit_expname.setObjectName(u"lineEdit_expname")
        self.lineEdit_expname.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_expname, 0, 2, 1, 1)

        self.lineEdit_workdir = QLineEdit(self.groupBox_experiment)
        self.lineEdit_workdir.setObjectName(u"lineEdit_workdir")
        self.lineEdit_workdir.setFont(font1)

        self.gridLayout.addWidget(self.lineEdit_workdir, 0, 4, 1, 1)

        self.label_9 = QLabel(self.groupBox_experiment)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 0, 3, 1, 1)

        self.textEdit_script = QTextEdit(self.groupBox_experiment)
        self.textEdit_script.setObjectName(u"textEdit_script")
        sizePolicy1.setHeightForWidth(self.textEdit_script.sizePolicy().hasHeightForWidth())
        self.textEdit_script.setSizePolicy(sizePolicy1)
        self.textEdit_script.setMinimumSize(QSize(0, 48))
        self.textEdit_script.setMaximumSize(QSize(16777215, 48))
        self.textEdit_script.setFont(font1)

        self.gridLayout.addWidget(self.textEdit_script, 1, 2, 1, 3)


        self.verticalLayout.addWidget(self.groupBox_experiment)

        self.widget_submit = QWidget(self.tab)
        self.widget_submit.setObjectName(u"widget_submit")
        sizePolicy5.setHeightForWidth(self.widget_submit.sizePolicy().hasHeightForWidth())
        self.widget_submit.setSizePolicy(sizePolicy5)
        self.horizontalLayout = QHBoxLayout(self.widget_submit)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton_submit = QPushButton(self.widget_submit)
        self.pushButton_submit.setObjectName(u"pushButton_submit")

        self.horizontalLayout.addWidget(self.pushButton_submit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.widget_submit)

        self.textBrowser_output = QTextBrowser(self.tab)
        self.textBrowser_output.setObjectName(u"textBrowser_output")

        self.verticalLayout.addWidget(self.textBrowser_output)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setAutoFillBackground(True)
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(24)
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_11)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 888, 23))
        self.menuConfig = QMenu(self.menuBar)
        self.menuConfig.setObjectName(u"menuConfig")
        self.menuInfo = QMenu(self.menuBar)
        self.menuInfo.setObjectName(u"menuInfo")
        self.menuInfo.setSeparatorsCollapsible(False)
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuConfig.menuAction())
        self.menuBar.addAction(self.menuInfo.menuAction())
        self.menuConfig.addAction(self.actionSave_Config)
        self.menuConfig.addAction(self.actionLoad_Config)
        self.menuInfo.addAction(self.actionAuthor_Info)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_cluster.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Submit Jobs", None))
        self.actionSave_Config.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.actionLoad_Config.setText(QCoreApplication.translate("MainWindow", u"Load Config", None))
        self.actionAuthor_Info.setText(QCoreApplication.translate("MainWindow", u"About This", None))
        self.groupBox_cluster.setTitle(QCoreApplication.translate("MainWindow", u"Cluster", None))
#if QT_CONFIG(tooltip)
        self.tab_3.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_clusterlist.setText(QCoreApplication.translate("MainWindow", u"Load Cluster List", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cluster Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"GPUs", None))
        self.tabWidget_cluster.setTabText(self.tabWidget_cluster.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"ITP", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Virtual Cluster", None))
        self.comboBox_singularityvirtualcluster.setItemText(0, QCoreApplication.translate("MainWindow", u"msroctovc", None))
        self.comboBox_singularityvirtualcluster.setItemText(1, QCoreApplication.translate("MainWindow", u"msrpilot", None))
        self.comboBox_singularityvirtualcluster.setItemText(2, QCoreApplication.translate("MainWindow", u"msrresrchvc", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Instance Type", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"SLA tier", None))
        self.comboBox_singularityslatier.setItemText(0, QCoreApplication.translate("MainWindow", u"Premium", None))
        self.comboBox_singularityslatier.setItemText(1, QCoreApplication.translate("MainWindow", u"Standard", None))
        self.comboBox_singularityslatier.setItemText(2, QCoreApplication.translate("MainWindow", u"Basic", None))

        self.label_singularityhelp.setText(QCoreApplication.translate("MainWindow", u"<a href=\"https://singularitydocs.azurewebsites.net/docs/overview/instance_types/#gpu-instance-types\">Which instance type should I choose?", None))
        self.tabWidget_cluster.setTabText(self.tabWidget_cluster.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Singularity", None))
        self.groupBox_storage.setTitle(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Account Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Container Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Datastore Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Account Key", None))
        self.groupBox_environment.setTitle(QCoreApplication.translate("MainWindow", u"Environment", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Docker Image", None))
        self.groupBox_experiment.setTitle(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Script", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Working Directory", None))
        self.pushButton_submit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Submit Jobs", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"To be continue...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Synchronize Files", None))
        self.menuConfig.setTitle(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

