ALERT_LIMIT = 65.0


def above_limit(reading):
    return reading > ALERT_LIMIT


def mean_reading(data):
    total = sum(data)
    return total / len(data)


if __name__ == "__main__":
    samples = [15, 25, 35]
    print("Sensor test:", above_limit(72), mean_reading(samples))