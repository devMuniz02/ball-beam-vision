def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def normalize_angle(angle):
    while angle > 180:
        angle -= 360
    while angle < -180:
        angle += 360
    return angle

def load_camera_config(config_file):
    import yaml
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config