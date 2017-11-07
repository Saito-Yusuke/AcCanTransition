## libraries
import sys
import pyodbc
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

## initial setting
server = 'ECOLOGDB2016'
database = 'ECOLOGDBver3'
username = 'TOMMYLAB\saito'
password = ''

fp = FontProperties(fname=r'C:\Windows\Fonts\meiryo.ttc')

## 関数定義
### DB connectionを定義
def dbConnection(sv=server, db=database, un=username, pw=password):
    # Windows認証
    con = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server}; SERVER='+sv+'; DATABASE='+db+'; Trusted_Connection=yes')
    return con

#入力画面
class InputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QVBoxLayout()

        # Labelオブジェクト
        ## DRIVER ID
        driverIdLabel = QLabel('DRIVER ID')

        ##CAR ID
        carIdLabel = QLabel('CAR ID')

        ## TRIP DIRECTION
        tripDirectionLabel = QLabel('TRIP DIRECTION')

        ## TRIP TIME
        tripTimeLabel = QLabel('TRIP TIME [min]')
        tripTimeMaxLabel = QLabel('最大')
        tripTimeMinLabel = QLabel('最小')

        ## TEMPERATURE
        temperatureLabel = QLabel('TEMPERATURE [℃]')
        temperatureMaxLabel = QLabel('最大')
        temperatureMinLabel = QLabel('最小')

        ## HUMIDITY
        humidityLabel = QLabel('HUMIDITY [%]')
        humidityMaxLabel = QLabel('最大')
        humidityMinLabel = QLabel('最小')

        ## PRECIPITATION
        precipitationLabel = QLabel('PRECIPITATION')

        ##WIND
        windLabel = QLabel('WIND')
        windSpeedLabel = QLabel('WIND SPEED [m/s]')
        windSpeedMaxLabel = QLabel('最大')
        windSpeedMinLabel = QLabel('最小')
        dwindDrectionLabel = QLabel('WIND DIRECTION')

        ## SUN LIGHT
        sunLightLabel = QLabel('SUN LIGHT [min]')
        sunLightMaxLabel = QLabel('最大')
        sunLightMinLabel = QLabel('最小')


        # LineEditオブジェクト
        self.temperatureMaxQle = QLineEdit(self)
        self.temperatureMinQle = QLineEdit(self)
        self.humidityMaxQle = QLineEdit(self)
        self.humidityMinQle = QLineEdit(self)
        self.humidityMaxQle.setText("100")
        self.humidityMinQle.setText("0")


        # ComboBoxオブジェクト
        ## DRIVER ID
        self.driverIdComboBox = QComboBox(self)
        self.driverIdComboBox.addItem("1（富井先生）")
        self.driverIdComboBox.addItem("4（森先生）")
        self.driverIdComboBox.addItem("16（本藤先生）")

        ## CAR ID
        self.carIdComboBox = QComboBox(self)
        self.carIdComboBox.addItem("3（LEAF）")
        self.carIdComboBox.addItem("8（LEAF_XXXXXX）")

        ## TRIP DIRECTION
        self.tripDirectionComboBox = QComboBox(self)
        self.tripDirectionComboBox.addItem("outward")
        self.tripDirectionComboBox.addItem("homeward")
        self.tripDirectionComboBox.addItem("other")

        ## TRIP TIME
        self.tripTimeMaxComboBox = QComboBox(self)
        self.tripTimeMaxComboBox.addItems(["150", "140", "130", "120", "110", "100", "90", "80", "70", "60", "50", "40", "30", "20", "10"])
        self.tripTimeMinComboBox = QComboBox(self)
        self.tripTimeMinComboBox.addItems(["140", "130", "120", "110", "100", "90", "80", "70", "60", "50", "40", "30", "20", "10", "0"])

        ## TEMPERATURE
        self.temperatureMaxComboBox = QComboBox(self)
        self.temperatureMaxComboBox.addItems(["45", "40", "35", "30", "25", "20", "15", "10", "5", "0", "-5", "-10", "-15", "-20"])
        self.temperatureMinComboBox = QComboBox(self)
        self.temperatureMinComboBox.addItems(["40", "35", "30", "25", "20", "15", "10", "5", "0", "-5", "-10", "-15", "-20", "-25"])

        ## HUMIDITY
        self.humidityMaxComboBox = QComboBox(self)
        self.humidityMaxComboBox.addItems(["100", "90", "80", "70", "60", "50", "40", "30", "20", "10"])
        self.humidityMinComboBox = QComboBox(self)
        self.humidityMinComboBox.addItems(["90", "80", "70", "60", "50", "40", "30", "20", "10", "0"])

        ##WIND SPEED
        self.windSpeedMaxComboBox = QComboBox(self)
        self.windSpeedMaxComboBox.addItems(["20", "18", "16", "14", "12", "10", "8", "6", "4", "2", "0"])
        self.windSpeedMinComboBox = QComboBox(self)
        self.windSpeedMinComboBox.addItems(["18", "16", "14", "12", "10", "8", "6", "4", "2", "0"])

        ## SUN LUGHT
        self.sunLightMaxComboBox = QComboBox(self)
        self.sunLightMaxComboBox.addItems(["150", "140", "130", "120", "110", "100", "90", "80", "70", "60", "50", "40", "30", "20", "10", "0"])
        self.sunLightMinComboBox = QComboBox(self)
        self.sunLightMinComboBox.addItems(["140", "130", "120", "110", "100", "90", "80", "70", "60", "50", "40", "30", "20", "10", "0"])

        # RadioButtonオブジェクト
        ## PRECIPITATION
        self.precipitationNonRadioButton = QRadioButton("降水なし")
        self.precipitationWeakRadioButton = QRadioButton("弱い雨")
        self.precipitationSlightlyStrongRadioButton = QRadioButton("やや強い雨")
        self.precipitationStrongRadioButton = QRadioButton("強い雨")
        self.precipitationViolentRadioButton = QRadioButton("激しい雨")
        self.precipitationVeryViolentRadioButton = QRadioButton("非常に激しい雨")
        self.precipitationImpetuousRadioButton = QRadioButton("猛烈な雨")
        self.precipitationNonRadioButton.setChecked(True)


        # TRIP条件を指定するWidgetグループ
        self.tripGroupBox = QGroupBox("TRIP")
        tripBox = QHBoxLayout()

        ## DRIVER ID
        driverIdLayout = QVBoxLayout()
        driverIdLayout.addWidget(driverIdLabel)
        driverIdLayout.addWidget(self.driverIdComboBox)

        ## CAR ID
        carIdLayout = QVBoxLayout()
        carIdLayout.addWidget(carIdLabel)
        carIdLayout.addWidget(self.carIdComboBox)

        ## TRIP DIRECTION
        tripDirectionLayout = QVBoxLayout()
        tripDirectionLayout.addWidget(tripDirectionLabel)
        tripDirectionLayout.addWidget(self.tripDirectionComboBox)

        ## TRIP TIME
        tripTimeMaxLayout = QHBoxLayout()
        tripTimeMaxLayout.addWidget(tripTimeMaxLabel)
        tripTimeMaxLayout.addWidget(self.tripTimeMaxComboBox)

        tripTimeMinLayout = QHBoxLayout()
        tripTimeMinLayout.addWidget(tripTimeMinLabel)
        tripTimeMinLayout.addWidget(self.tripTimeMinComboBox)

        tripTimeLayout = QVBoxLayout()
        tripTimeLayout.addWidget(tripTimeLabel)
        tripTimeLayout.addLayout(tripTimeMaxLayout)
        tripTimeLayout.addLayout(tripTimeMinLayout)

        ## まとめ
        tripBox.addLayout(driverIdLayout)
        tripBox.addLayout(carIdLayout)
        tripBox.addLayout(tripDirectionLayout)
        tripBox.addLayout(tripTimeLayout)

        self.tripGroupBox.setLayout(tripBox)
        grid.addWidget(self.tripGroupBox)


        # WEATHER条件を指定するグループ
        self.weatherGroupBox = QGroupBox("WEATHER")
        weatherBox = QVBoxLayout()
        weatherBox1 = QHBoxLayout()

        ## TEMPERATURE
        temperatureMaxLayout = QHBoxLayout()
        temperatureMaxLayout.addWidget(temperatureMaxLabel)
        temperatureMaxLayout.addWidget(self.temperatureMaxQle)

        temperatureMinLayout = QHBoxLayout()
        temperatureMinLayout.addWidget(temperatureMinLabel)
        temperatureMinLayout.addWidget(self.temperatureMinQle)

        temperatureLayout = QVBoxLayout()
        temperatureLayout.addWidget(temperatureLabel)
        temperatureLayout.addLayout(temperatureMaxLayout)
        temperatureLayout.addLayout(temperatureMinLayout)

        ## HUMIDITY
        humidityMaxLayout = QHBoxLayout()
        humidityMaxLayout.addWidget(humidityMaxLabel)
        humidityMaxLayout.addWidget(self.humidityMaxQle)

        humidityMinLayout = QHBoxLayout()
        humidityMinLayout.addWidget(humidityMinLabel)
        humidityMinLayout.addWidget(self.humidityMinQle)

        humidityLayout = QVBoxLayout()
        humidityLayout.addWidget(humidityLabel)
        humidityLayout.addLayout(humidityMaxLayout)
        humidityLayout.addLayout(humidityMinLayout)

        ## PRECIPITATION
        precipitationRadioButtonLayout = QHBoxLayout()
        precipitationRadioButtonLayout.addWidget(self.precipitationNonRadioButton)
        precipitationRadioButtonLayout.addWidget(self.precipitationWeakRadioButton)
        precipitationRadioButtonLayout.addWidget(self.precipitationSlightlyStrongRadioButton)
        precipitationRadioButtonLayout.addWidget(self.precipitationStrongRadioButton)
        precipitationRadioButtonLayout.addWidget(self.precipitationViolentRadioButton)
        precipitationRadioButtonLayout.addWidget(self.precipitationVeryViolentRadioButton)
        precipitationRadioButtonLayout.addWidget(self.precipitationImpetuousRadioButton)

        precipitationLayout = QVBoxLayout()
        precipitationLayout.addWidget(precipitationLabel)
        precipitationLayout.addLayout(precipitationRadioButtonLayout)

        ## WIND SPEED
        windSpeedMaxLayout = QHBoxLayout()
        windSpeedMaxLayout.addWidget(windSpeedMaxLabel)
        windSpeedMaxLayout.addWidget(self.windSpeedMaxComboBox)

        windSpeedMinLayout = QHBoxLayout()
        windSpeedMinLayout.addWidget(windSpeedMinLabel)
        windSpeedMinLayout.addWidget(self.windSpeedMinComboBox)

        windSpeedLayout = QVBoxLayout()
        windSpeedLayout.addWidget(windSpeedLabel)
        windSpeedLayout.addLayout(windSpeedMaxLayout)
        windSpeedLayout.addLayout(windSpeedMinLayout)

        ## SUN LIGHT
        sunLightMaxLayout = QHBoxLayout()
        sunLightMaxLayout.addWidget(sunLightMaxLabel)
        sunLightMaxLayout.addWidget(self.sunLightMaxComboBox)

        sunLightMinLayout = QHBoxLayout()
        sunLightMinLayout.addWidget(sunLightMinLabel)
        sunLightMinLayout.addWidget(self.sunLightMinComboBox)

        sunLightLayout = QVBoxLayout()
        sunLightLayout.addWidget(sunLightLabel)
        sunLightLayout.addLayout(sunLightMaxLayout)
        sunLightLayout.addLayout(sunLightMinLayout)

        ## まとめ
        weatherBox1.addLayout(temperatureLayout)
        weatherBox1.addLayout(humidityLayout)
        weatherBox1.addLayout(windSpeedLayout)
        weatherBox1.addLayout(sunLightLayout)
        weatherBox.addLayout(weatherBox1)
        weatherBox.addLayout(precipitationLayout)

        self.weatherGroupBox.setLayout(weatherBox)
        grid.addWidget(self.weatherGroupBox)

        # Outputボタン
        outPutButton = QPushButton("Output", self)
        outPutButton.resize(outPutButton.sizeHint())
        outPutButton.clicked.connect(self.outPutButtonClicked)
        grid.addWidget(outPutButton)


        self.setLayout(grid)
        self.setWindowTitle('AC CAN Transition')
        self.setWindowIcon(QIcon('rusi.png'))
        self.show()

    # 出力ボタンが押された時の処理
    def outPutButtonClicked(self):
        sender = self.sender()

        ## 入力されている値を取得・コンソールに出力
        print("CONDITION")

        ### DRIVER ID
        if self.driverIdComboBox.currentIndex() == 0:
            driverId = 1
        elif self.driverIdComboBox.currentIndex() == 1:
            driverId = 4
        elif self.driverIdComboBox.currentIndex() == 2:
            driverId = 16
        else:
            print("無効なDRIVER ID")
        print("DRIVER ID : " + str(driverId))
        
        ### CAR ID
        if self.carIdComboBox.currentIndex() == 0:
            carId = 3
        elif self.carIdComboBox.currentIndex() == 1:
            carId = 8
        else:
            print("無効なCAR ID")
        print("CAR ID : " + str(carId))

        ### TRIP DIRECTION
        if self.tripDirectionComboBox.currentIndex() == 0:
            tripDirection = "outward"
        elif self.tripDirectionComboBox.currentIndex() == 1:
            tripDirection = "homeward"
        elif self.tripDirectionComboBox.currentIndex() == 2:
            tripDirection = "other"
        else:
            print("無効なTRIP DIRECTION")
        print("TRIP DIRECTION : " + tripDirection)

        ### TRIP TIME
        tripTimeMax = int(self.tripTimeMaxComboBox.currentText())
        tripTimeMin = int(self.tripTimeMinComboBox.currentText())
        print("TRIP TIME : " + str(tripTimeMin) +"min ～ " + str(tripTimeMax) + "min")

        ### TEMPERATURE
        temperatureMax = int(self.temperatureMaxQle.text())
        temperatureMin = int(self.temperatureMinQle.text())
        print("TEMPERATURE : " + str(temperatureMin) +"℃ ～ " + str(temperatureMax) + "℃")

        ### HUMIDITY
        humidityMax = int(self.humidityMaxQle.text())
        humidityMin = int(self.humidityMinQle.text())
        print("HUMIDITY : " + str(humidityMin) +"% ～ " + str(humidityMax) + "%")

        ### PRECIPITATION
        if self.precipitationNonRadioButton.isChecked():
            precipitationMax = 0
            precipitationMin = 0
            precipitationString = u"PRECIPITATION : 降水なし (" + str(precipitationMin) + "mm)"
        elif self.precipitationWeakRadioButton.isChecked():
            precipitationMax = 10
            precipitationMin = 0
            precipitationString = u"PRECIPITATION : 弱い雨 (" + str(precipitationMin) + u"mm/h ～ " + str(precipitationMax) + "mm/h)"
        elif self.precipitationSlightlyStrongRadioButton.isChecked():
            precipitationMax = 20
            precipitationMin = 10
            precipitationString = u"PRECIPITATION : やや強い雨 (" + str(precipitationMin) + u"mm/h ～ " + str(precipitationMax) + "mm/h)"
        elif self.precipitationStrongRadioButton.isChecked():
            precipitationMax = 30
            precipitationMin = 20
            precipitationString = u"PRECIPITATION : 強い雨 (" + str(precipitationMin) + u"mm/h ～ " + str(precipitationMax) + "mm/h)"
        elif self.precipitationViolentRadioButton.isChecked():
            precipitationMax = 50
            precipitationMin = 30
            precipitationString = u"PRECIPITATION : 激しい雨 (" + str(precipitationMin) + u"mm/h ～ " + str(precipitationMax) + "mm/h)"
        elif self.precipitationVeryViolentRadioButton.isChecked():
            precipitationMax = 80
            precipitationMin = 50
            precipitationString = u"PRECIPITATION : 非常に激しい雨 (" + str(precipitationMin) + u"mm/h ～ " + str(precipitationMax) + "mm/h)"
        elif self.precipitationImpetuousRadioButton.isChecked():
            precipitationMax = 1000
            precipitationMin = 80
            precipitationString = u"PRECIPITATION : 猛烈な雨 (" + str(precipitationMin) + u"mm/h ～)"
        else:
            print("無効なPRECIPITATION")
        print(precipitationString)

        ### WIND SPEED
        windSpeedMax = int(self.windSpeedMaxComboBox.currentText())
        windSpeedMin = int(self.windSpeedMinComboBox.currentText())
        print("WIND SPEED : " + str(windSpeedMin) +"m/s ～ " + str(windSpeedMax) + "m/s")

        ### SUN LIGHT
        sunLightMax = int(self.sunLightMaxComboBox.currentText())
        sunLightMin = int(self.sunLightMinComboBox.currentText())
        print("SUN LIGHT : " + str(sunLightMin) +"min ～ " + str(sunLightMax) + "min")

        conditionString = "DRIVER ID : " + str(driverId) + "\nCAR ID : " + str(carId) + "\nTRIP DIRECTION : " + tripDirection + "\nTRIP TIME : " + str(tripTimeMin) + u"min ～ " + str(tripTimeMax) + "min"\
        + "\nTEMPERATURE : " + str(temperatureMin) + u"℃ ～ " + str(temperatureMax) + u"℃" + "\nHUMIDITY : " + str(humidityMin) + u"% ～ " + str(humidityMax) + "%\n" + precipitationString\
        + "\nWIND SPEED : " + str(windSpeedMin) +u"m/s ～ " + str(windSpeedMax) + "m/s" + "\nSUN LIGHT : " + str(sunLightMin) + u"min ～ " + str(sunLightMax) + "min"

        print("\nクエリ生成開始. \n")

        ##クエリ生成
        getTripQuery = "select TRIP_ID from TRIPS_WEATHER_View where DRIVER_ID = " + str(driverId) + " and CAR_ID = " + str(carId)\
        + " and (SENSOR_ID = 12 or SENSOR_ID = 16) and TRIP_DIRECTION = '" + tripDirection + "'"\
        + " and TRIP_TIME >=" + str(tripTimeMin * 60) + " and TRIP_TIME <= " + str(tripTimeMax * 60)\
        + " and TRIP_TEMPERATURE >= " + str(temperatureMin) + " and TRIP_TEMPERATURE <= " + str(temperatureMax)\
        + " and TRIP_HUMIDITY >= " + str(humidityMin) + " and TRIP_HUMIDITY <= " + str(humidityMax)\
        + " and TRIP_PRECIPITATION >= " + str(precipitationMin) + " * TRIP_TIME / 3600 and TRIP_PRECIPITATION <= " + str(precipitationMax) + " * TRIP_TIME / 3600"\
        + " and TRIP_WIND_SPEED >= " + str(windSpeedMin) + " and TRIP_WIND_SPEED <= " + str(windSpeedMax)\
        + " and TRIP_SUN_LIGHT >= " + str(sunLightMin) + " and TRIP_SUN_LIGHT <= " + str(sunLightMax)

        ## DBにアクセスして実行
        print("クエリ生成終了. DBにアクセス開始. \n")
        cur = dbConnection().cursor()
        cur.execute(getTripQuery)
        
        tripRows = cur.fetchall()
        tripCounter = 0

        query1 = "select LEAFSPY_RAW2.AC_PWR_250W * 250.0 / 1000.0 from LEAFSPY_RAW2, TRIPS_WEATHER_View where LEAFSPY_RAW2.TRIP_ID = "
        query2 = " and LEAFSPY_RAW2.TRIP_ID = TRIPS_WEATHER_View.TRIP_ID and LEAFSPY_RAW2.DATETIME >= TRIPS_WEATHER_View.START_TIME and LEAFSPY_RAW2.DATETIME <= TRIPS_WEATHER_View.END_TIME order by LEAFSPY_RAW2.DATETIME"
        getLeafSpyQueryList = []
        leafSpyList = []
        
        for tripRow in tripRows:
            print("TRIP ID : %d" % (tripRow[0]))
            tripCounter += 1

            # グラフを描く
            ## トリップを1つ指定して該当するCANデータを取ってくる
            ### クエリ生成
            getLeafSpyQueryList.append(query1 + str(tripRow[0]) + query2)
            ### クエリ実行
            cur.execute(getLeafSpyQueryList[tripCounter - 1])
            ### 結果を格納
            leafSpyList.append(cur.fetchall())
            ### グラフを描画
            plt.plot(leafSpyList[tripCounter - 1], label = "TRIP ID : " + str(tripRow[0]))

        print("\n以上%d件のトリップが該当しました. \n描画したグラフを表示します. " % tripCounter)
        plt.legend()
        plt.title("AC CAN Transiton")
        plt.ylabel("AC POWER from LEAF SPY [kW]")
        plt.ylim(0, 5.0)
        plt.figtext(0.58, 0.71, conditionString, fontproperties=fp)
        plt.show()

        dbConnection().commit()
        dbConnection().close()
        print("\n正常終了. \n")

if __name__ == "__main__":

    ## 入力画面
    ### ウィンドウ
    app = QApplication(sys.argv)
    win = InputWindow()
    sys.exit(app.exec_())

    