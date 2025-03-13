import machine
import time

SPI configuration using your chosen pins:
SCLK: GPIO6 (MTCK), MOSI: GPIO5 (MTDI), MISO: GPIO7 (MTDO), CS: GPIO4 (MTMS)
spi = machine.SPI(1, baudrate=1000000, polarity=0, phase=0,
                  sck=machine.Pin(6), mosi=machine.Pin(5), miso=machine.Pin(7))
cs = machine.Pin(4, machine.Pin.OUT)
cs.value(1)  # Keep CS high when not in use


def read_mcp3008(channel):
    """
    Reads the MCP3008 on the specified channel (0-7) and returns a 10-bit ADC value.
    The command is sent as 3 bytes:
      - Byte 1: Start bit (0x01)
      - Byte 2: Contains single/diff bit and channel selection.
      - Byte 3: Dummy byte to clock out the result.
    The 10-bit result is returned from the received bytes.
    """
    # Construct command buffer:
    # Byte 1: Start bit = 0x01
    # Byte 2: For single-ended mode, the command is: (0x08 + channel) << 4.
    # For channel 0: (0x08 + 0) << 4 = 0x80, channel 1: 0x90, etc.
    buf = bytearray(3)
    buf[0] = 0x01
    buf[1] = (0x08 + channel) << 4
    buf[2] = 0x00

    cs.value(0)  # Activate chip select
    spi.write_readinto(buf, buf)
    cs.value(1)  # Deactivate chip select

    # The 10-bit result is composed of the lower 2 bits of buf[1] and all 8 bits of buf[2]
    result = ((buf[1] & 0x03) << 8) | buf[2]
    return result


while True:
    # Read channels 0 to 3, where each channel corresponds to one FSR voltage divider.
    adc0 = read_mcp3008(0)
    adc1 = read_mcp3008(1)
    adc2 = read_mcp3008(2)
    adc3 = read_mcp3008(3)

    print("ADC Values:")
    print("CH0:", adc0, "CH1:", adc1, "CH2:", adc2, "CH3:", adc3)
    time.sleep(0.5)