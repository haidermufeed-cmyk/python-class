import importlib

sensors = importlib.import_module("06_sensors")

readings = [45, 68, 79, 91]

print("Alert limit:", sensors.ALERT_LIMIT)
print("Average:", sensors.mean_reading(readings))

for value in readings:
    status = "ALERT" if sensors.above_limit(value) else "NORMAL"
    print(value, "->", status)


print("Main module:", __name__)
print("Sensor module:", sensors.__name__)


from importlib import import_module

sensor_tools = import_module("06_sensors")
check = sensor_tools.above_limit

print(check(70))
print(sensor_tools.mean_reading([12, 18, 24]))


ALERT_LIMIT = 100.0

print("Local limit:", ALERT_LIMIT)
print("Sensor result:", check(75))