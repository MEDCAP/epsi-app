from flask import Flask, request, jsonify
from magnets import hupc_processing, clinical_processing, mr_solutions_processing
import os
from flask_cors import CORS
from werkzeug.utils import secure_filename
import cv2

# Constants
UPLOAD_FOLDER = "/Users/benjaminyoon/Desktop/PIGI folder/Projects/Project4 HP MRI Web Application/hp-mri-web-application-yoonbenjamin/data"
app = Flask(__name__)
CORS(app)


@app.route("/api/get_proton_picture/<int:slider_value>", methods=["POST"])
def get_proton_picture(slider_value: int):
    """
    Retrieve and return an image based on a given slider value by loading the corresponding DICOM file.

    Parameters:
        slider_value (int): The slider value corresponding to the desired image.

    Returns:
        Flask Response: Either the image file or a JSON object indicating an error.

    Author: Benjamin Yoon
    Date: 2024-04-30
    Version: 1.2.2
    """
    data = request.get_json()
    magnet_type = data.get("magnetType", "HUPC")  # Default to HUPC if not specified

    if magnet_type == "HUPC":
        result = hupc_processing.process_proton_picture(slider_value, data)
    elif magnet_type == "Clinical":
        result = clinical_processing.process_proton_picture(slider_value, data)
    elif magnet_type == "MR Solutions":
        result = mr_solutions_processing.process_proton_picture(slider_value, data)
    else:
        return jsonify({"error": "Invalid magnet type"}), 400

    return result


@app.route("/api/get_num_slider_values", methods=["GET"])
def fetch_num_slider_values():
    """
    API endpoint to fetch the number of slider values.

    Returns:
        JSON: Contains the number of slider values.
    """
    magnet_type = request.args.get(
        "magnetType", "HUPC"
    )  # Default to HUPC if not specified
    
    if magnet_type == "HUPC":
        num_values = hupc_processing.get_num_slider_values()
    elif magnet_type == "Clinical":
        num_values = 0
    elif magnet_type == "MR Solutions":
        num_values = mr_solutions_processing.get_num_slider_values()
    else:
        return jsonify({"error": "Invalid magnet type"}), 400
    
    return jsonify({"numSliderValues": num_values})


@app.route("/api/get_hp_mri_data/<int:hp_mri_dataset>", methods=["POST"])
def get_hp_mri_data(hp_mri_dataset):
    """
    Retrieve and return HP MRI data for a specified dataset ID with dynamic thresholding for data visualization.

    Parameters:
        hp_mri_dataset (int): The dataset ID for which to fetch HP MRI data.

    Returns:
        json: JSON containing MRI data or an error message.

    Author: Benjamin Yoon
    Date: 2024-04-30
    Version: 1.2.2
    """
    threshold = request.args.get("threshold", default=0.2, type=float)
    magnet_type = request.args.get(
        "magnetType", "HUPC"
    )  # Default to HUPC if not specified

    if magnet_type == "HUPC":
        result = hupc_processing.process_hp_mri_data(hp_mri_dataset, threshold)
    elif magnet_type == "Clinical":
        result = 0
    elif magnet_type == "MR Solutions":
        result = 0
    else:
        return jsonify({"error": "Invalid magnet type"}), 400

    return result


@app.route("/upload", methods=["POST"])
def file_upload():
    """
    Handle file uploads by saving uploaded files to a predefined upload folder.

    Returns:
        json: A JSON object indicating the status of the file upload (success or error).
    """
    try:
        uploaded_files = request.files.getlist("files")
        for file in uploaded_files:
            if file:
                filename = secure_filename(file.filename)
                save_path = os.path.join(UPLOAD_FOLDER, filename)
                file.save(save_path)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
