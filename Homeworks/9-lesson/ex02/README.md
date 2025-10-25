# Weather Analyzer — SRP Misoli

## 🎯 Maqsad
Ushbu misolda **Single Responsibility Principle (SRP)** buzilgan va to‘g‘rilangan (refactor qilingan) holat ko‘rsatildi.  
SRP — bu **har bir sinf faqat bitta mas’uliyatga ega bo‘lishi kerak** degan prinsip.

---

## 🚫 Broken Version
`WeatherAnalyzer` sinfi bir nechta ishni bajaradi:
1. Ob-havo ma’lumotlarini tahlil qiladi  
2. Natijani konsolga chiqaradi  
3. Natijani faylga saqlaydi  

👉 Bu **SRP**ga zid, chunki bitta sinfda bir nechta mas’uliyat mavjud.

```python
class WeatherAnalyzer:
    def __init__(self, temps):
        self.temps = temps

    def analyze(self):
        avg = sum(self.temps) / len(self.temps)
        high = max(self.temps)
        low = min(self.temps)

        report = f"Average: {avg:.1f}°C\nHigh: {high}°C\nLow: {low}°C\n"

        print(report)  # konsolga chiqarish
        with open("weather_report.txt", "w") as f:  # faylga yozish
            f.write(report)

        return report
```

---

## ✅ Fixed Version (SRP bilan)
Mas’uliyatlar alohida sinflarga ajratildi:
- `WeatherCalculator` — faqat tahlil qiladi  
- `ReportPrinter` — faqat natijani chiqaradi  
- `ReportSaver` — faqat faylga yozadi  
- `WeatherAnalyzer` — faqat jarayonni boshqaradi

```python
class WeatherCalculator:
    def calculate(self, temps):
        avg = sum(temps) / len(temps)
        high = max(temps)
        low = min(temps)
        return f"Average: {avg:.1f}°C\nHigh: {high}°C\nLow: {low}°C\n"


class ReportPrinter:
    def print(self, report):
        print(report)


class ReportSaver:
    def save(self, filename, report):
        with open(filename, "w") as f:
            f.write(report)


class WeatherAnalyzer:
    def __init__(self, calculator, printer, saver):
        self.calculator = calculator
        self.printer = printer
        self.saver = saver

    def analyze(self, temps):
        report = self.calculator.calculate(temps)
        self.printer.print(report)
        self.saver.save("weather_report.txt", report)
        return report
```

---

## 🧠 Xulosa
| Versiya | Holat | Izoh |
|----------|--------|------|
| **Broken** | ❌ SRP buzilgan | Hisoblash, chiqarish va saqlash bir joyda |
| **Fixed** | ✅ SRP to‘g‘rilangan | Har bir sinf faqat bitta mas’uliyatni bajaradi |

**Natija:** Kod modulli, oson kengaytiriladi va testlashga tayyor holga keltirilgan.
