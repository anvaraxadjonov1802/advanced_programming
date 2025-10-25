# 🧪 Unit Test — Greeter Example

## 🎯 Maqsad
Ushbu vazifada Python dasturlash tilida **unit test** yozish va **mock obyektlardan foydalanish** amaliyoti bajarildi.  
Testlar yordamida `Greeter` sinfi turli vaqt oralig‘ida to‘g‘ri salomlashuv xabarini qaytarishini tekshiradi.

---

## 📁 Loyihaning tuzilishi
```
greeter.py
test_greeter.py
```

---

## 📄 greeter.py
Ushbu faylda ikkita sinf mavjud:
- **`TimeProvider`** — tizim vaqtini (soatni) olish uchun mo‘ljallangan.
- **`Greeter`** — foydalanuvchini ayni soatga qarab salomlaydi.

```python
from datetime import datetime


class TimeProvider:
    def now_hour(self):
        """Ayni damdagi soatni oladi"""
        return datetime.now().hour


class Greeter:
    def __init__(self, time_provider: TimeProvider):
        self.time_provider = time_provider

    def greet(self, name):
        hour = self.time_provider.now_hour()
        if 5 <= hour < 12:
            return f"Good Morning, {name}!"
        elif 12 <= hour < 18:
            return f"Good Afternoon, {name}!"
        else:
            return f"Good Evening, {name}!"
```

---

## 🧩 test_greeter.py
Bu faylda `unittest` va `unittest.mock` kutubxonalari yordamida testlar yozilgan.  
**Mock obyekt** orqali vaqtni (soatni) sun’iy tarzda belgilab, `Greeter` sinfi izolyatsiya qilingan holda test qilinadi.

```python
import unittest
from unittest.mock import Mock
from greeter import Greeter


class TestGreeter(unittest.TestCase):
    def test_greeter_morning(self):
        mock = Mock()
        mock.now_hour.return_value = 8
        greeter = Greeter(mock)
        self.assertEqual(greeter.greet("Anvar"), "Good Morning Jasur!")
    
    def test_greeter_afternoon(self):
        mock = Mock()
        mock.now_hour.return_value = 15
        greeter = Greeter(mock)
        self.assertEqual(greeter.greet("Olim"), "Good Afternoon, Olim!")
        
    def test_greeter_morning(self):
        mock = Mock()
        mock.now_hour.return_value = 21
        greeter = Greeter(mock)
        self.assertEqual(greeter.greet("Bobur"), "Good Evening, Bobur!")

if __name__ == "__main__":
    unittest.main()
```

---

## ⚙️ Testni ishga tushirish
Terminal yoki buyruq satrida quyidagi buyruqni bajarish kifoya:
```bash
python -m unittest test_greeter.py
```

---

## 🧠 Xulosa
| Bo‘lim | Mazmuni |
|--------|----------|
| **Prinsip** | Unit test va mocking |
| **Mock maqsadi** | `TimeProvider` sinfini sun’iy soat bilan almashtirish |
| **Test natijasi** | Har xil vaqt oralig‘ida to‘g‘ri salomlashuv qaytariladi |
| **Foyda** | Haqiqiy vaqtga bog‘liq bo‘lmagan, barqaror testlar yaratiladi |

---

## ✅ Yakuniy fikr
Bu vazifada `Mock` obyekt yordamida **haqiqiy vaqtga bog‘liqlik bartaraf etildi**.  
Natijada testlar **aniq, tezkor va takrorlanadigan** holga keltirildi.
