def normalize(dataPoint, min, max, new_min, new_max):
    
    top = dataPoint - min
    bottom = max - min
    ratio = top / bottom
    normalized_data = ratio * (new_max - new_min) + new_min

    return normalized_data