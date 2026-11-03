# master.py
from pymodbus.client import ModbusTcpClient
import time

# اتصال به اسلیو
client = ModbusTcpClient('192.168.1.10', port=502)

if not client.connect():
    print("نتونستم به اسلیو وصل بشم!")
    exit()

print("متصل شدم به اسلیو")

try:
    while True:
        # نوشتن مقدار در Holding Register شماره 0
        value = int(time.time()) % 1000          # یک عدد نمونه
        client.write_register(0, value)
        print(f"نوشتم: {value}")

        # خواندن Holding Register شماره 0
        result = client.read_holding_registers(0, 1)
        if not result.isError():
            print(f"خوندم: {result.registers[0]}")
        else:
            print("خطا در خواندن")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nقطع شد")
finally:
    client.close()
