# Document Attribute Extractor

This project is a Streamlit web application that allows users to extract key-value pairs from document images using the Qwen Model through the OpenRouter API. It is capable of processing `.jpg`, `.jpeg`, and `.png` images to extract structured data in JSON format.

---

## Features
- **File Upload**: Supports `.jpg`, `.jpeg`, and `.png` file uploads.
- **Image Display**: Displays the uploaded image in the app for preview.
- **Document Parsing**: Extracts key-value pairs from the document using the Qwen-2-VL-72B-Instruct model.
- **JSON Output**: Provides a well-structured JSON output of the extracted data.
- **Error Handling**: Handles unsupported file formats and API errors gracefully.

---

## Tech Stack
- **Streamlit**: For creating the user interface.
- **OpenRouter API**: To interact with the Qwen-2-VL-72B-Instruct model.
- **Pillow**: For image processing and conversion to base64.
- **Python**: The core programming language used for the app.

---

## APIs Used
- **OpenRouter API**: The app uses the OpenRouter API for document attribute extraction. The Qwen-2-VL-72B-Instruct model processes the uploaded image and extracts key-value pairs.

---

## Installation
### Prerequisites
- Python 3.8 or later
- Pip (Python package manager)

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
