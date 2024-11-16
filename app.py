import streamlit as st
import requests
import json
import base64
from io import BytesIO
from PIL import Image

# Function to encode the image into base64 format
def encode_image(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    encoded_string = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return encoded_string

# Streamlit App
st.title("Document Attribute Extractor")

# Upload file option
uploaded_file = st.file_uploader("Upload a document (Image or PDF)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    if uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        # Display uploaded image
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)  # Display the image
        base64_img = encode_image(img)
    else:
        st.error("Unsupported file type. Please upload a JPG, PNG, or JPEG file.")
        st.stop()

    # Submit button
    if st.button("Submit"):
        with st.spinner("Extracting data..."):
            # OpenRouter API key
            OPENROUTER_API_KEY = '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'

            # API request to OpenRouter
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}"
                },
                data=json.dumps({
                    "model": "qwen/qwen-2-vl-72b-instruct",  # Qwen model
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": "You are Document Attribute Extractor. Extract all the key-value pairs in the document as JSON."
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/png;base64,{base64_img}"
                                    }
                                }
                            ]
                        }
                    ],
                    "max_tokens": 4837,
                    "temperature": 0.2,
                    "top_p": 0.04
                })
            )

            # Handle response
            if response.status_code == 200:
                raw_output = response.text
                st.subheader("Raw API Response:")
                st.code(raw_output, language="json")  # Display the raw response in the Streamlit app

                try:
                    # Parse JSON response
                    json_output = response.json()
                    if "choices" in json_output and len(json_output["choices"]) > 0:
                        # Extract the content and clean any backticks
                        extracted_content = json_output["choices"][0]["message"]["content"]
                        cleaned_content = extracted_content.strip("```json").strip("```")
                        
                        # Parse the cleaned JSON
                        parsed_json = json.loads(cleaned_content)
                        st.subheader("Extracted JSON:")
                        st.json(parsed_json)
                    else:
                        st.error("No JSON data found in the response.")
                except json.JSONDecodeError as e:
                    st.error(f"JSON Parse Error: {str(e)}")
            else:
                st.error(f"Failed to get a valid response. Status Code: {response.status_code}")

# Footer
st.caption(
    "Powered by OpenRouter API and Qwen Model | Created by [Faiyyaz Hangad](https://www.instagram.com/faiyazhangad/)"
)
