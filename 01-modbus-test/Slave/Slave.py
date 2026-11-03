# slave.py
from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.device import ModbusDeviceIdentification
import logging

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

# دیتاستور (Holding Registers از آدرس 0 تا 99)
store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [0]*100),   # Discrete Inputs
    co=ModbusSequentialDataBlock(0, [0]*100),   # Coils
    hr=ModbusSequentialDataBlock(0, [0]*100),   # Holding Registers
    ir=ModbusSequentialDataBlock(0, [0]*100)    # Input Registers
)
context = ModbusServerContext(slaves=store, single=True)

# اطلاعات دستگاه
identity = ModbusDeviceIdentification()
identity.VendorName = 'MySlave'
identity.ProductCode = 'PM'
identity.VendorUrl = 'http://github.com/pymodbus'
identity.ProductName = 'Modbus Slave'
identity.ModelName = 'Modbus Server'
identity.MajorMinorRevision = '1.0'

print("Modbus Slave در حال اجرا روی 192.168.1.10:502 ...")
StartTcpServer(
    context=context,
    identity=identity,
    address=("192.168.1.10", 502)
)
