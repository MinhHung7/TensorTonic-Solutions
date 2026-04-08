import numpy as np

def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    image = np.array(image).flatten()

    ans = [0] * 256
    
    frequencies = np.unique(image, return_counts=True)
    
    for i in range(len(frequencies[0])):
        ans[frequencies[0][i]] = frequencies[1][i]

    return ans