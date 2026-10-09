
# AMR Risk Level Prediction

A web-based application that displays Antimicrobial Resistance (AMR) risk levels for different districts.

## About the Project

The AMR Risk Level Prediction project provides a simple web interface to view district-wise antimicrobial resistance risk information. It uses Python and Flask for the backend and HTML and CSS for the frontend.

## Features

- District-wise AMR risk level information
- Interactive web interface
- Flask-based backend
- JSON data integration
- Simple and user-friendly design

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JSON

## Project Structure

```text
himachal/
├── app.py
├── data/
│   └── amr_data.json
├── static/
│   └── style.css
├── templates/
│   ├── district.html
│   └── index.html
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/hkumar80558-droid/AMR-Risk-Level.git
```

### 2. Open the project folder

```bash
cd AMR-Risk-Level
```

### 3. Install dependencies

Install Flask:

```bash
pip install flask
```

If your project has a `requirements.txt` file, install all dependencies using:

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the local URL shown in your terminal in a web browser.

## Future Improvements

- Add more district-wise AMR data
- Improve visualizations and reporting
- Deploy the application online

## Author

Developed as an Antimicrobial Resistance (AMR) Risk Level web application.