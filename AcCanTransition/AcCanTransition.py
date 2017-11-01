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
class Button(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # Labelオブジェクト
        driverIdLabel = QLabel('DRIVER ID')
        carIdLabel = QLabel('CAR ID')
        tripTimeLabel = QLabel('TRIP TIME')
        temperatureLabel = QLabel('TEMPERATURE')
        humidityLabel = QLabel('HUMIDITY')
        precipitationLabel = QLabel('PRECIPITATION')
        sunlightLabel = QLabel('SUN LIGHT')
        windLabel = QLabel('WIND')
        windSpeedLabel = QLabel('WIND SPEED')
        dwindDrectionLabel = QLabel('WIND DIRECTION')
        maxLabel = QLabel('MAX')
        minLabel = QLabel('MIN')

        # LineEditオブジェクト
        driverIdQle = QLineEdit()
        carIdQle = QLineEdit()
        tripTimeQle = QLineEdit()
        temperatureQle = QLineEdit()
        humidityQle = QLineEdit()
        precipitationQle = QLineEdit()
        sunlightQle = QLineEdit()
        windQle = QLineEdit()
        windSpeedQle = QLineEdit()
        windDirectionQle = QLineEdit()
        maxQle = QLineEdit()
        minQle = QLineEdit()

        # TRIP条件を指定するWidgetグループ
        self.tripGroupBox = QGroupBox("TRIP")

        # WEATHER条件を指定するグループ
        self.weatherGroupBox = QGroupBox("WEATHER")

        # Outputボタン
        outPutButton = QPushButton("Output", self)
        outPutButton.clicked.connect(self.outPutButtonClicked)

        self.statusBar()
        self.resize(500, 500)
        self.setWindowTitle('AC CAN Transition')
        self.setWindowIcon(QIcon('rusi.png'))
        self.show()

    # 出力ボタンが押された時の処理
    def outPutButtonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' has been pushed.')

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
    win = Button()
    sys.exit(app.exec_())

    