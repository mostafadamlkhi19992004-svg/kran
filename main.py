from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import platform
import socket
import requests

class DeviceInfoApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.label = Label(text="اضغط على الزر لإرسال البيانات", font_size=18)
        
        btn = Button(text="إرسال البيانات", size_hint=(1, 0.3), background_color=(0.1, 0.6, 0.3, 1))
        btn.bind(on_press=self.send_data)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def send_data(self, instance):
        url = "https://webhook.site/43166c83-e2d3-49a1-a6aa-5c1f782f1a6e"
        payload = {
            "device": platform.node(),
            "os": platform.system()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                self.label.text = "تم إرسال البيانات بنجاح!"
            else:
                self.label.text = f"خطأ في الاستجابة: {response.status_code}"
        except Exception as e:
            self.label.text = "فشل الاتصال بالإنترنت"

if name == 'main':
    DeviceInfoApp().run()
