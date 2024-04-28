# HP MRI Web Application

## Introduction
The Hyperpolarized (HP) Magnetic Resonance Imaging (MRI) Web Application, developed by Benjamin Yoon and Medcap Computing at PIGI Lab (University of Pennsylvania Perelman School of Medicine), is a sophisticated data visualization tool designed for the analysis and interpretation of EPSI (Echo Planar Spectroscopic Imaging) data. This application offers an intuitive user interface allowing users to interactively adjust image slices, contrast levels, and dataset parameters, and visualize EPSI grids overlaid on proton images.

## Features
### Version 1.0.0
- **Initial Release:** Features interactive sliders for adjusting image slices and contrast and real-time EPSI grid overlay on proton images.

### Version 1.0.1
- **Responsive Design:** Automatically adjusts dimensions based on screen resolution.
- **Enhanced Contrast Control:** Expanded range of contrast settings for improved image visualization.

### Version 1.1.0
- **Interactive Plot Shift Controls:** Introduces buttons and directional arrows to shift the overlay plot relative to the proton image, including a reset button for default positioning.
- **EPSI Axis Management:** Added functionality to manage EPSI axis with grid retention; displays grid and image by default.
- **Export Functionality:** Feature to save the current view as a PNG file.

### Version 1.1.1
- **Operational Enhancements:** Improved application functionality.
- **About Page and Branding Updates:** Introduced an About page, updated the application's logo and title, and included copyright information for Benjamin Yoon, PIGI Lab/Medcap Computing.
- **Data Management:** Enhanced dataset upload capabilities for processing and visualization.

### Version 1.2.0
- **UI Refinement:** Enhanced the user interface to improve aesthetics and usability, focusing on intuitive design and user interaction.
- **Official Title:** Named as Hyperpolarized (HP) Magnetic Resonance (MRI) Web Application.

### Version 1.2.1
- **Voxel Selection Tool:** Introduced functionality to select and highlight individual voxels within the EPSI grid for detailed analysis.
- **Threshold Adjustment:** Implemented a slider to dynamically adjust the minimum peak value of the EPSI data visualization.

## Installation (Local)
You can download the HP MRI Web Application locally by running the following commands in your terminal (one time only). First, we install necessary dependencies for a React application in the frontend and Flask in the backend. 

```bash
git clone https://github.com/benjaminyoon/hpmri-benjaminyoon.git hpmri-local
```
Here create and activate our virtual environment for the backend.
```bash
cd backend
python -m venv .venv
```
Run the first command if you're on MacOS and the second command if you're on Windows
```bash
source .venv/bin/activate
.venv\Scripts\activate
```
Finally run the following command
```bash
pip install -r requirements.txt
```
Now we install the node modules for our frontend
```bash
cd ..
cd frontend
npm install react-app-rewired --save-dev
npm uninstall -g react-app-rewired
npm install
```
## Usage
- Start the application locally by running the following commands (everytime you want to start the application):

```bash
cd backend
source .venv/bin/activate # on MacOS, if on Windows run: .venv\Scripts\activate
python HpMri.py
```
Now open a separate terminal instance (window) and run the following commands
```bash
cd hpmri-local
cd frontend
npm start
```

- Navigate to http://localhost:3000 in your web browser to access the HP MRI App.

## License
This project is licensed under the MIT License - React (software)

## About PIGI Lab
PIGI Lab is a MRI technology research lab in the University of Pennsylvania Perelman School of Medicine dedicated to creating innovative solutions across various fields. Learn more at www.pigilab.com.

## Author
Benjamin Yoon, HP MRI Web Application lead developer, is a B.S.E. student at the University of Pennsylvania. For any questions or suggestions regarding the HP MRI Web App, please contact us:

- Benjamin Yoon - yoonb2002@gmail.com

2024 University of Pennsylvania Perelman School of Medicine, PIGI Lab. All rights reserved.
