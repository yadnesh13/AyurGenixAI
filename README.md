# AyurGenixAI 🌿 - An Ayurvedic Medication Advisor 💊

<img src="./ayurveda.jpg" alt="Ayurveda" width="700"/>

**Welcome to AyurGenixAI!**

AyurGenixAI is an innovative solution designed to bridge the gap between traditional Ayurvedic medicine and modern healthcare. Utilizing advanced AI technologies, including natural language processing (NLP) and machine learning (ML), AyurGenixAI provides personalized Ayurvedic medication recommendations based on classical texts and user inputs. This integration of ancient wisdom with contemporary medical practices aims to enhance holistic health and wellness.

## Table of Contents
- [Problem Description](#problem-description)
- [Solution Provided](#solution-provided)
- [Features](#features)
- [Components](#components)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Problem Description

1. Finding reliable and personalized Ayurvedic medication advice is challenging in today's fast-paced world. 
2. Many people seek natural remedies but struggle to get accurate and tailored recommendations for their specific symptoms and conditions.

## Solution Provided

1. AyurGenixAI uses advanced NLP and ML technologies to provide personalized Ayurvedic medication recommendations. 
2. Users can input symptoms into a user-friendly interface to receive precise advice on Ayurvedic remedies, promoting overall health and wellness.

## Features
- **User Input Analysis:** Captures and processes user symptoms and conditions.
- **Personalized Recommendations:** Suggests Ayurvedic medications tailored to individual needs.
- **Extensive Database:** Utilizes a comprehensive database of Ayurvedic treatments and their uses.
- **Interactive Interface:** Easy-to-use interface for a seamless user experience.
- **Secure and Confidential:** Ensures user data privacy and security.
- **Educational Resources:** Detailed information about Ayurvedic herbs, their uses, and benefits.

## Components
- **Data Processing:** Scripts for preprocessing data and preparing it for model training.
- **Model Training:** Scripts for training NLP and ML models to analyze symptoms and recommend medications.
- **Recommendation Engine:** Core logic for generating personalized Ayurvedic medication recommendations.

## Project Structure
```
AyurGenixAI/
├── data/
│   ├── herbs.csv
│   ├── symptoms.csv
│   ├── ayurvedic_formulations.csv
│   ├── ayurvedic_texts/
│   │   ├── text1.txt
│   │   ├── text2.txt
│   │   └── ...
│   └── ayurvedic_formulations.csv
│
├── models/
│   ├── symptom_analysis_model.h5
│   ├── medication_recommendation_model.h5
│   └── formulation_engine.py
│
├── preprocessing/
│   ├── text_processing.py
│   ├── nlp_analysis.py
│   └── combined_preprocessed_text.txt
│
├── src/
│   ├── data_processing.py
│   ├── model_training.py
│   ├── recommendation_engine.py
│   └── formulation_engine.py
│
├── recommendation/
│   ├── recommendation_results.csv
│
├── app.py
├── requirements.txt
├── environment.yml
└── README.md

```

## Setup and Installation

### Prerequisites
- Anaconda/Miniconda
- Python 3.x

### Installation
1. **Clone the repository**
   ```sh
   git clone https://github.com/kittu-122/AyurGenixAI.git
   cd AyurGenixAI
   ```

2. **Create a new conda environment and install dependencies**
   ```sh
   conda env create -f environment.yml
   conda activate ayurveda_env
   ```

3. **Install NLTK data**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   ```

## Usage

### Step 1: Preprocess Text Data
Run the `text_processing.py` script to preprocess the Ayurvedic text files.

```sh
python preprocessing/text_processing.py
```

### Step 2: Analyze Text Data
Run the `nlp_analysis.py` script to perform NLP analysis and extract relevant information from the preprocessed text.

```sh
python preprocessing/nlp_analysis.py
```

### Step 3: Generate Recommendations
Run the `formulation_engine.py` script to generate Ayurvedic drug and formulation recommendations based on input symptoms or pharmacological properties.

```sh
python recommendation/formulation_engine.py
```

## CSV File Columns
- `Herb Name`
- `Parts Used in Treatment`
- `Disease`
- `Symptoms/Condition`
- `Therapeutic Uses`
- `Formulation`
- `Dosage`
- `Administration Guidelines`
- `Pharmacological Property`
- `Side Effects`
- `Prakriti`
- `Dosha`

## Documentation Links

### 1. NLP Model - BERT
- [BERT GitHub](https://github.com/google-research/bert)  
  **Use**: Provides the implementation of the BERT model, a foundational transformer model for natural language understanding, enabling effective text analysis and feature extraction in Ayurvedic contexts.
  
- [BERT Fine-Tuning Guide](https://huggingface.co/transformers/training.html)  
  **Use**: Offers guidelines for fine-tuning BERT on custom datasets, allowing for improved performance on specific Ayurvedic tasks.

### 2. Contextual Model - Ollama 3
- [Ollama Documentation](https://ollama.com)  
  **Use**: Provides resources for integrating Ollama’s AI models into applications, enhancing contextual understanding and user interaction in the AyurGenixAI project.

### 3. AI-Powered Analysis - Gemini API
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)  
  **Use**: Enables the use of advanced AI analysis tools for generating insights, improving the quality of Ayurvedic recommendations and user engagement.

### 4. Backend Development
Flask
- [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/)  
  **Use**: A micro web framework for Python, used to build lightweight APIs for the AyurGenixAI backend.

- [Flask API Quickstart Guide](https://flask.palletsprojects.com/en/2.3.x/quickstart/#apis)  
  **Use**: Provides a step-by-step guide to creating APIs with Flask, facilitating rapid development of backend services.

Django
- [Django Documentation](https://docs.djangoproject.com/en/stable/)  
  **Use**: A high-level Python web framework that promotes rapid development and clean, pragmatic design, suitable for building robust web applications.

- [Django Rest Framework](https://www.django-rest-framework.org/)  
  **Use**: An extension of Django that simplifies the creation of RESTful APIs, essential for serving data to the frontend of the AyurGenixAI application.

### 5. Frontend Development - React
- [React Documentation](https://reactjs.org/docs/getting-started.html)  
  **Use**: A JavaScript library for building user interfaces, allowing for the creation of interactive and dynamic web applications for AyurGenixAI.

- [Axios in React](https://axios-http.com/docs/intro)  
  **Use**: A promise-based HTTP client for the browser and Node.js, facilitating easy data fetching and interaction with the backend APIs.

### 6. Database - MongoDB
- [MongoDB Documentation](https://www.mongodb.com/docs/)  
  **Use**: A NoSQL database that allows for flexible data storage, ideal for handling diverse Ayurvedic data structures.

- [MongoDB Atlas Setup](https://www.mongodb.com/cloud/atlas)  
  **Use**: Provides a cloud database solution for easy setup, management, and scaling of the database for the AyurGenixAI project.

### 7. Model Training Frameworks
  TensorFlow
- [TensorFlow Documentation](https://www.tensorflow.org/)  
  **Use**: A powerful open-source framework for building and training machine learning models, suitable for developing AI components in AyurGenixAI.

### 8. Hugging Face - Pretrained Models and Fine-Tuning
- [Hugging Face](https://huggingface.co/)  
  **Use**: A platform for accessing a wide range of pretrained models and tools for fine-tuning, particularly useful for NLP tasks in the AyurGenixAI application.

### 9. Deployment Platforms
  Frontend
- [Deploying Frontend with Netlify](https://docs.netlify.com/)  
  **Use**: A platform for deploying static websites and frontend applications, providing continuous deployment and hosting for the React application.

- [Deploying Frontend with Vercel](https://vercel.com/docs)  
  **Use**: An optimized platform for deploying frontend applications, enhancing performance and user experience for the AyurGenixAI project.

Backend
- [Deploying Flask on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)  
  **Use**: A guide for deploying Flask applications to Heroku, simplifying the process of making the backend accessible online.

- [AWS Elastic Beanstalk for Django Deployment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)  
  **Use**: Provides resources for deploying Django applications on AWS, allowing for scalable and reliable hosting of the backend services.
  
## Accessing the Website

## Contributing
Contributions to the project are welcome! Feel free to submit pull requests, report issues, or suggest enhancements to improve AyurGenixAI.

**Thank you for choosing this project. Hoping that this project proves useful and delivers a seamless experience for your needs!**







