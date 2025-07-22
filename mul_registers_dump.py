import smbus2
import time

I2C_BUS = 1
I2C_ADDR = 0x66

bus = smbus2.SMBus(I2C_BUS)

try:
    while True:
        print("Reading registers 0x00 to 0x0F:")
        for reg in range(0x10):
            try:
                data = bus.read_i2c_block_data(I2C_ADDR, reg, 2)
                val = (data[1] << 8) + data[0]
                print(f"  Reg 0x{reg:02X}: Raw bytes={data} Value={val}")
            except Exception as e:
                print(f"  Reg 0x{reg:02X}: Read error: {e}")
        print()
        time.sleep(1)
except KeyboardInterrupt:
    bus.close()
    print("Stopped.")
