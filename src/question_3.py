import json
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

JSON_FILE = 'images/f46456de-0522-465e-9a9d-0efc88aebf43.jpeg'
IMAGE_FILE = 'annotations/RBD13_24543036_BLUE_DOUBLE.json'


def get_rois(file_name: str) -> list:
    """Get list of ROIs from a JSON file.
    
    Args:
        file_name (str): Path to the JSON file.
        
    Returns:
        list: List of ROIs.
    """
    
    return 


def get_polygons(roi_list: list) -> list:
    """Return a list of np.array for each polygon.
    
    Args:
        roi_list (list): List of ROIs.
        
    Returns:
        list: List of numpy arrays representing polygons.
    """
    return 


def save_image(image_name: str, img: np.ndarray):
    """Save an image locally.
    
    Args:
        image_name (str): Path where the image will be saved.
        img (np.ndarray): Image to save.
    """
    


def view_image(img: np.ndarray):
    """Display an image using matplotlib.
    
    Args:
        img (np.ndarray): Image to display.
    """
    


def add_polygons_to_image(img: np.ndarray, point_array_list: list) -> np.ndarray:
    """Add polygons to an image.
    
    Args:
        img (np.ndarray): Original image.
        point_array_list (list): List of point arrays representing polygons.
        
    Returns:
        np.ndarray: Image with polygons added.
    """
    
    return 


def create_mask_image(img: np.ndarray, point_array_list: list, class_num: int) -> np.ndarray:
    """Create a mask image from polygons.
    
    Args:
        img (np.ndarray): Original image.
        point_array_list (list): List of point arrays representing polygons.
        class_num (int): Class number to fill the mask.
        
    Returns:
        np.ndarray: Mask image.
    """
    
    return 


def get_rgb_image(file_name: str) -> np.ndarray:
    """Load an image and convert to RGB.
    
    Args:
        file_name (str): Path to the image file.
        
    Returns:
        np.ndarray: RGB image.
    """
    
    return 


def main():
    pass

if __name__ == "__main__":
    main()