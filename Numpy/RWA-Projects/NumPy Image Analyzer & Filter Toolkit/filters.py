import numpy as np


def to_grayscale(image):
    return np.dot(image[..., :3], [0.299, 0.587, 0.114])


def normalize(image):
    return image / 255.0


def adjust_brightness(image, factor):
    return np.clip(image + factor, 0, 255)


def adjust_contrast(image, factor):
    mean = np.mean(image)
    return np.clip((image - mean) * factor + mean, 0, 255)
