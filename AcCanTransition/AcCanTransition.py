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

        # Labelオブジェクト
        ## DRIVER ID
        driverIdLabel = QLabel('DRIVER ID')

        ##CAR ID
        carIdLabel = QLabel('CAR ID')

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
        precipitationLabel = QLabel('PRECIPITATION [mm]')

        ## SUN LIGHT
        sunlightLabel = QLabel('SUN LIGHT')

        ##WIND
        windLabel = QLabel('WIND')
        windSpeedLabel = QLabel('WIND SPEED')
        dwindDrectionLabel = QLabel('WIND DIRECTION')


        # LineEditオブジェクト
        driverIdQle = QLineEdit()
        carIdQle = QLineEdit()
        tripTimeMaxQle = QLineEdit()
        tripTimeMinQle = QLineEdit()
        temperatureQle = QLineEdit()
        humidityQle = QLineEdit()
        precipitationQle = QLineEdit()
        sunlightQle = QLineEdit()
        windQle = QLineEdit()
        windSpeedQle = QLineEdit()
        windDirectionQle = QLineEdit()


        # BOXレイアウトオブジェクト
        grid = QVBoxLayout()


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

        ## TRIP TIME
        self.tripTimeMaxComboBox = QComboBox(self)
        self.tripTimeMaxComboBox.addItems(["10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140", "150"])
        self.tripTimeMinComboBox = QComboBox(self)
        self.tripTimeMinComboBox.addItems(["0", "10", "20", "30", "40", "50", "60", "70", "80", "90", "100", "110", "120", "130", "140"])


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
        tripBox.addLayout(tripTimeLayout)

        self.tripGroupBox.setLayout(tripBox)
        grid.addWidget(self.tripGroupBox)


        # WEATHER条件を指定するグループ
        self.weatherGroupBox = QGroupBox("WEATHER")
        weatherBox = QVBoxLayout()

        temperatureLayout = QHBoxLayout()
        temperatureLayout.addWidget(temperatureLabel)
        temperatureLayout.addWidget(temperatureQle)

        humidityLayout = QHBoxLayout()
        humidityLayout.addWidget(humidityLabel)
        humidityLayout.addWidget(humidityQle)

        weatherBox.addLayout(temperatureLayout)
        weatherBox.addLayout(humidityLayout)

        self.weatherGroupBox.setLayout(weatherBox)
        grid.addWidget(self.weatherGroupBox)

        # Outputボタン
        outPutButton = QPushButton("Output", self)
        outPutButton.clicked.connect(self.outPutButtonClicked)
        grid.addWidget(outPutButton)

        self.setLayout(grid)
        self.resize(500, 500)
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

    