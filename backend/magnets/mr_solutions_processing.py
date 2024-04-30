"""
Module: mr_solutions_processing.py

Description:
This module contains functions specific to processing HP MRI data from MR Solutions magnets.
It includes functions to handle image retrieval, data processing, and other tasks
specific to the MR Solutions equipment configurations and data formats.

Functions:
- process_proton_picture(slider_value): Retrieves and processes proton images based on slider inputs.
- process_hpmri_data(epsi_value, threshold): Processes and filters HP MRI data using a dynamic threshold, specific to MR Solutions data characteristics.
- read_epsi_plot(epsi_value, threshold): Reads and processes EPSI plots, adjusting parameters and data visibility based on MR Solutions standards.

Author:
Benjamin Yoon

Date:
2024

Version:
1.0.0
"""

# Import statements
import numpy as np
from flask import jsonify, send_file
import os
import traceback
from PIL import Image
import cv2
import pydicom
import io

# Constants
DICOM_FOLDER = "/Users/benjaminyoon/Desktop/PIGI folder/Projects/Project4 HP MRI Web Application/hp-mri-web-application-yoonbenjamin/data/data MRS/proton/1/"


# Example of function definition
def process_proton_picture(slider_value, data):
    """
    Retrieves and processes a proton image based on a slider value for MR Solutions magnets.
    This function adjusts image processing parameters to fit the characteristics of MR Solutions equipment.

    Args:
        slider_value (int): The index to determine which image to load.
        data (dict): Additional data necessary for processing the image, such as contrast settings or other parameters.

    Returns:
        Flask Response: Image file as PNG or an error message in JSON format.
    """
    try:
        filename = f"5091_{slider_value:05d}.dcm"
        dicom_path = os.path.join(DICOM_FOLDER, filename)

        if not os.path.exists(dicom_path):
            return jsonify({"error": "DICOM file not found"}), 404

        dcm = pydicom.dcmread(dicom_path)
        slice_image = dcm.pixel_array
        slice_image[slice_image < 5] = 0

        normalized_image = (slice_image - np.min(slice_image)) / (
            np.max(slice_image) - np.min(slice_image)
        )
        normalized_image[normalized_image < 0.05] = 0.0

        contrast = data.get("contrast", 1)
        clahe = cv2.createCLAHE(clipLimit=contrast, tileGridSize=(8, 8))
        clahe_image = clahe.apply(np.uint8(normalized_image * 255))
        clahe_image[clahe_image < 5] = 0
        rescaled_image = clahe_image / 255.0
        rescaled_image[rescaled_image < 0.05] = 0.0

        buffer = io.BytesIO()
        pil_image = Image.fromarray((rescaled_image * 255).astype(np.uint8))
        pil_image.save(buffer, format="PNG")
        buffer.seek(0)

        return send_file(buffer, mimetype="image/png")
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


def get_num_slider_values():
    """
    Calculate the number of slider values based on available datasets or images.

    Returns:
        int: The total number of slider values (datasets or images).
    """
    dicom_files = [file for file in os.listdir(DICOM_FOLDER) if file.endswith(".dcm")]
    num_slider_values = len(dicom_files)
    return num_slider_values


# Additional functions would follow with similar structured comments...
