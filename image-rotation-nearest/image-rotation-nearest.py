import numpy as np

def rotate_image(image, angle_degrees):
    image = np.array(image)
    h, w = image.shape

    # center
    c_x = (w - 1) / 2
    c_y = (h - 1) / 2

    angle = np.radians(angle_degrees)
    cos_a = np.cos(angle)
    sin_a = np.sin(angle)

    rotated = np.zeros_like(image)

    for i in range(h):
        for j in range(w):
            # tọa độ relative tâm
            x = j - c_x
            y = i - c_y

            # inverse rotation
            src_x = c_x + x * cos_a - y * sin_a
            src_y = c_y + x * sin_a + y * cos_a

            # nearest neighbor
            src_x = int(round(src_x))
            src_y = int(round(src_y))

            if 0 <= src_x < w and 0 <= src_y < h:
                rotated[i, j] = image[src_y, src_x]
            else:
                rotated[i, j] = 0

    return rotated.tolist()