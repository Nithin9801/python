# weather app
import requests
import sys
from PyQt5.QtWidgets import QWidget,QApplication,QVBoxLayout,QLabel,QPushButton,QLineEdit
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the city name :",self)
        self.city_name = QLineEdit(self)
        self.get_weather_button = QPushButton("Get weather",self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.InitUI()

    def InitUI(self):

        self.setGeometry(700,300,500,400)

        vbox = QVBoxLayout()
        
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_name)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_name.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_name.setObjectName("city_name")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel,QPushButton{
                           font-family:calibri;}
            QLabel#city_label{
                           font-size:50px;
                           font-style:bold;}
            QLineEdit#city_name{
                           font-size:20px;
                           font-style:italic;}
            QPushButton#get_weather_button{
                           font-size:30px;
                           font-style:semibold;}
            QLabel#temperature_label{
                           font-size:40px;}
            QLabel#emoji_label{
                           font-size:40px;
                           font-family:segoe UI emoji}
            QLabel#description_label{
                           font-size:30px;
                           font-style:semiitalic}
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
    
    def get_weather(self):
        
        api="api-key" #your openweather api key
        cityname = self.city_name.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={api}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request\n Please check your input")
                case 401:
                    self.display_error("Unauthorized\n invalid api key")
                case 403:
                    self.display_error("Forbidden\n Acess is denied")
                case 404:
                    self.display_error("Not found\n city not found")
                case 500:
                    self.display_error("Internal server error\n Please try again later")
                case 502:
                    self.display_error("Bad gateway\n Invalid response from the server")
                case 503:
                    self.display_error("service Unavailable\n service is down")
                case 504:
                    self.display_error("Gateway timeout\n No response from the server")
                case _:
                    self.display_error(f"something error like {http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("connection error\n please check your internet")
        except requests.exceptions.Timeout:
            self.display_error("timeout error\n the request is timedout")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\n check your url")
        except requests.exceptions.RequestException as request_error:
            self.display_error(f"Request error: {request_error}")


    def display_error(self,message):
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self,data):
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k -  273.15
        temperature_f = (temperature_k * 9/5) - 459.67
        
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        self.description_label.setText(weather_description)
        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(self.get_emoji(weather_id))
    
    @staticmethod
    def get_emoji(weather_id):

        if 200<= weather_id <= 232:
            return "⛈️"
        elif 300<= weather_id <=321:
            return "🌦️"
        elif 500<= weather_id <=531:
            return "🌧️"
        elif 600<= weather_id <=6221:
            return "❄️"
        elif 701<= weather_id <=741:
            return "🌬️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif 801<= weather_id <=804:
            return "☁️"
        else:
            return ""
        
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wetherwindow = WeatherApp()
    wetherwindow.show()
    sys.exit(app.exec_())
