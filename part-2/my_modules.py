import numpy as np

def mean_filter(image):
    new_img = np.copy(image)
    row, col = image.shape
    for i in range(3, row-3):
        for j in range(3, col-3):
            kernal = []
            for fx in range(-1, 2):
                for fy in range(-1, 2):
                    a = image.item(i+fx, j+fy)
                    kernal.append(a)
            mean = sum(kernal)/len(kernal)
            new_img[i,j] = mean
    return new_img

def median_filter(image):
    new_img = np.copy(image)
    row, col = image.shape
    for i in range(2, row-2):
        for j in range(2, col-2):
            kernel = []
            for fx in range(-2, 3):
                for fy in range(-2, 3):
                    a = image.item(i+fx, j+fy)
                    kernel.append(a)
            kernel.sort()
            median = kernel[13]
            new_img[i, j] = median
    return new_img

def gaussian_noise(image):

    row,col = image.shape
    mean = 0
    var = 500
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col))
    gauss = gauss.reshape(row,col)
    noisy = image + gauss
    return noisy

def salt_pepper_noise(image):
    
    s_vs_p = 0.5
    amount = 0.2
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    out[coords] = 0
    return out

def salt_noise(image):
    s_vs_p = 0.5
    amount = 0.2
    out = np.copy(image)
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[coords] = 1
    return out

def pepper_noise(image):
    s_vs_p = 0.5
    amount = 0.1
    out = np.copy(image)
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    out[coords] = 0
    return out