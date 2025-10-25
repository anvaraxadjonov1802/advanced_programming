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
