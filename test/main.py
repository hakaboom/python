import uiautomator2 as u2
import time
import re
_DEVICE_ID = "emulator-5562"
#_DEVICE_ID = "127.0.0.1:5563"

driver = u2.connect(_DEVICE_ID)
driver.system.init(1)
driver.touch.down(500,500)