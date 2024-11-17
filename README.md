# Handwriting to Text Conversion Using Deep Learning
This project aims to convert handwritten English characters, including cursive writing and special symbols, into digital text using deep learning techniques. The system employs Convolutional Neural Networks (CNNs) trained on the IAM dataset for handwriting recognition. It processes handwritten images, removes background noise, detects text regions, and extracts the recognized text.

## **Features**

* **Handwriting recognition:** Converts handwritten text (including cursive) from images into digital text.
* **Preprocessing:** Removes background noise and enhances image quality for better recognition.
* **Text Detection:** Identifies text regions in images before extraction.
* **Special characters support:** Recognizes special symbols and characters.
* **User-friendly interface:** Allows users to upload handwritten images for processing.

## **Project Structure**

The project consists of the following components:

1. **Model Training:** The CNN model is trained on the IAM dataset to recognize various handwriting styles.
2. **Image Preprocessing:** Utilizes OpenCV for preprocessing and horizontal-vertical segmentation of input images.
3. **Text Detection & Recognition:** The processed images are passed through the model to detect and extract text.
4. **Output:** The recognized text is displayed to the user.

## **Prerequisites**

Before running the project, ensure you have the following dependencies installed:

* Python 3.x
* TensorFlow (for the model)
* Flask (for the web app)
* OpenCV (for image processing)
* NLTK (for tokenization)
* Autocorrect (for spelling correction)

## **Dataset**

The project uses the **IAM dataset**, which contains a collection of handwritten words and sentences. 

You can download the dataset from the IAM Handwriting Database.

## **Setup**

**1. Clone the repository**

Start by cloning this repository to your local machine:

      git clone https://github.com/HarshaliGhumate/HandwrittenToText.git
      
      cd handwriting-to-text-conversion

**2. Set Up the Upload Folder**

Create the static/uploads/ folder for image uploads:

      mkdir -p static/uploads
      
**3. Install Dependencies**

Install the required libraries:

      pip install -r requirements.txt

**4. Set Up the Model**

Make sure your pre-trained model (HandwrittenWordsModel-Try3.h5) is in an accessible directory:

    from keras.models import load_model
    
    model = load_model('static/models/HandwrittenWordsModel-Try3.h5')
    
**5. Run the Flask App**

Start the Flask app with:

    python app.py
    
Access the app in your browser at http://127.0.0.1:5000/.

## **Using the Application**

1. **Upload Image:** Go to the homepage and upload a handwritten image (e.g., PNG, JPG).
2. **Text Recognition:** The app will process the image and recognize the text.
3. **Spelling Correction:** It will also correct any spelling errors using the Autocorrect library.
4. **View Text:** The recognized text will be displayed on a new page.

## **Acknowledgements**

* **IAM Handwriting Dataset:** Used for training the model.
* **Flask:** Web framework for serving the app.
* **TensorFlow/Keras:** For the deep learning model.
* **OpenCV:** For image processing.
* **Autocorrect:** For spelling correction.

















