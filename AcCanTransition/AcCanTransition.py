## libraries
import sys
import pyodbc
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

## initial setting
server = 'ECOLOGDB2016'
database = 'ECOLOGDBver3'
username = 'TOMMYLAB\saito'
password = ''

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
        temperatureQle = QLineEdit()
        humidityQle = QLineEdit()
        precipitationQle = QLineEdit()
        sunlightQle = QLineEdit()
        windQle = QLineEdit()
        windSpeedQle = QLineEdit()
        windDirectionQle = QLineEdit()


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
        temperatureMaxLayout.addWidget(self.temperatureMaxComboBox)

        temperatureMinLayout = QHBoxLayout()
        temperatureMinLayout.addWidget(temperatureMinLabel)
        temperatureMinLayout.addWidget(self.temperatureMinComboBox)

        temperatureLayout = QVBoxLayout()
        temperatureLayout.addWidget(temperatureLabel)
        temperatureLayout.addLayout(temperatureMaxLayout)
        temperatureLayout.addLayout(temperatureMinLayout)

        ## HUMIDITY
        humidityMaxLayout = QHBoxLayout()
        humidityMaxLayout.addWidget(humidityMaxLabel)
        humidityMaxLayout.addWidget(self.humidityMaxComboBox)

        humidityMinLayout = QHBoxLayout()
        humidityMinLayout.addWidget(humidityMinLabel)
        humidityMinLayout.addWidget(self.humidityMinComboBox)

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

        ## 入力されている値を取得

        ##クエリ生成
        sampleQuery = "SELECT TRIP_ID, DATETIME, AC_PWR_250W FROM LEAFSPY_RAW2 WHERE DATETIME >= '2017-10-30' ORDER BY DATETIME"

        ## DBにアクセスして実行
        cur = dbConnection().cursor()
        cur.execute(sampleQuery)
        
        rows = cur.fetchall()
        
        for row in rows:
            print("%d %s %d" % (row[0], row[1], row[2]))
            
        dbConnection().commit()
        dbConnection().close()

if __name__ == "__main__":

    ## 入力画面
    ### ウィンドウ
    app = QApplication(sys.argv)
    win = InputWindow()
    sys.exit(app.exec_())

    