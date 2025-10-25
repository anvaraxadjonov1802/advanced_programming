 # ❌ 1. Tahlil qilish (analysis)
 # ❌ 2. Konsolga chiqarish
 # ❌ 3. Faylga yozish

class WeatherAnalyzer:
    def __init__(self, temps):
        self.temps = temps

    def analyze(self):
        avg = sum(self.temps) / len(self.temps)
        high = max(self.temps)
        low = min(self.temps)
        #1
        report = f"Average: {avg:.1f}°C\nHigh: {high}°C\nLow: {low}°C\n"
        #2
        print(report)
        #3
        with open("weather_report.txt", "w") as f:
            f.write(report)

        return report
