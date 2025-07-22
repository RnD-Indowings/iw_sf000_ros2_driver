#-----------------------------------Code for I2C connection with RPI4/5 and SF000/B--------------------------------------------------------------------------------# 
import time
import smbus2
import logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

I2C_BUS = 1
#I2C_ADDR = 0x66
READ_REG = 0x00
I2C_ADDR = 0x66
bus = smbus2.SMBus(1)

def read_distance_cm(bus, addr):
    try:
        # read 2 bytes from register 0x00
        data = bus.read_i2c_block_data(addr, READ_REG, 2)
        # i2cget returned 0x1f00, which means little endian (low byte first)
        dist_cm = (data[1] << 8) + data[0]
        return dist_cm
    except Exception as e:
        logging.error(f"Failed to read from SF000: {e}")
        return None

def main():
    bus = smbus2.SMBus(I2C_BUS)
    print("[INFO] Starting IW-SF000/B LiDAR I2C reader...")

    try:
        while True:
            data = bus.read_i2c_block_data(I2C_ADDR, 0x00, 2)
            dist_cm = (data[0] << 8) + data[1]  # High byte first, low byte second
            dist_m = dist_cm / 100.0
            logging.info(f"[DISTANCE] {dist_m:.2f} m")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        bus.close()
        print("[INFO] I2C bus closed.")

if __name__ == "__main__":
    main()
