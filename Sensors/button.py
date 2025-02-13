import utime
from machine import Pin

class Keypad:
    def __init__(self, column_count=4):
        # Define the keypad layout
        if column_count == 4:
            self.KEYPAD = [
                [0, 0, 1, 1],
                [0, 0, 1, 1],
                [2, 2, 3, 3],
                [2, 2, 3, 3]
            ]
        else:
            raise ValueError("Only 4-column keypads are supported.")

        # Define GPIO pins for rows and columns
        self.ROW_PINS = [5,4,3,2]
        self.COL_PINS = [6,7,8,9]

        # Initialize column pins as outputs and row pins as inputs
        self.rows = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in self.ROW_PINS]
        self.cols = [Pin(pin, Pin.OUT) for pin in self.COL_PINS]

    def get_key(self):
        """Scans the keypad and returns the pressed key."""
        # Set all columns to low
        for col in self.cols:
            col.value(0)

        # Check if any key is pressed by scanning row pins
        row_val = -1
        for i, row in enumerate(self.rows):
            if row.value() == 0:  # Key pressed (active low)
                row_val = i
                break
        if row_val == -1:  # No key pressed
            return None
        print(row_val)
        # Set all columns to input mode
        for col in self.cols:
            col.init(Pin.IN, Pin.PULL_DOWN)

        # Set the detected row as output high
        self.rows[row_val].init(Pin.OUT)
        self.rows[row_val].value(1)

        # Detect the column of the pressed key
        col_val = -1
        for j, col in enumerate(self.cols):
            if col.value() == 1:
                col_val = j
                break
        print(col_val)
        if col_val == -1:
            col_val = 0
        
        # Reset pins
        self.cleanup()

        return self.KEYPAD[row_val][col_val]

    def cleanup(self):
        """Resets all pins."""
        for row in self.rows:
            row.init(Pin.IN, Pin.PULL_UP)
        for col in self.cols:
            col.init(Pin.OUT)

if __name__ == "__main__":
    keypad = Keypad()

    while True:
        key = None
        print("waiting for button")
        while key is None:
            key = keypad.get_key()
        print("Key pressed:", key)
        utime.sleep(0.5)

