# Unit Test — Greeter Example

## 🎯 Maqsad
Ushbu vazifada Python dasturlash tilida **unit test** yozish va **mock (sun’iy obyekt)** ishlatish amaliyoti bajarildi.  
Test orqali `Greeter` sinfining funksionalligini izolyatsiya qilingan holda tekshirish ko‘zda tutilgan.

---

## 🧩 Kod haqida
`Greeter` sinfi foydalanuvchini salomlashadi va bu xabarni `MessageService` orqali yuboradi.

```python
class MessageService:
    def send_message(self, message):
        print(f"Message sent: {message}")


class Greeter:
    def __init__(self, service):
        self.service = service

    def greet(self, name):
        message = f"Hello, {name}!"
        self.service.send_message(message)
        return message
```

---

## 🧪 Test haqida
Test `unittest` va `unittest.mock` kutubxonalari yordamida yozilgan.  
Asosiy maqsad — **`MessageService` haqiqiy chaqiruvini mock orqali almashtirish**.

```python
import unittest
from unittest.mock import Mock
from greeter import Greeter

class TestGreeter(unittest.TestCase):
    def test_greet_sends_message(self):
        mock_service = Mock()
        greeter = Greeter(mock_service)

        result = greeter.greet("Ali")

        mock_service.send_message.assert_called_once_with("Hello, Ali!")
        self.assertEqual(result, "Hello, Ali!")
```

---

## 🧠 Xulosa
| Bo‘lim | Mazmuni |
|--------|----------|
| **Prinsip** | Unit test va mocking |
| **Asosiy maqsad** | `Greeter` sinfini `MessageService`dan mustaqil test qilish |
| **Foyda** | Tizim qismlarini alohida sinovdan o‘tkazish, bog‘liqliklarni kamaytirish |
| **Natija** | Testlar muvaffaqiyatli o‘tdi, kod izolyatsiyalangan holda to‘g‘ri ishlaydi |

---

## ✅ Yakuniy fikr
Mock obyektlardan foydalanish orqali haqiqiy xizmatlar (`API`, `database`, `file I/O`) ishlamasdan test yozish imkoniyati yaratildi.  
Natijada, test tezroq, barqarorroq va ishonchli bo‘ldi.
