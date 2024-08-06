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

### CSV File Columns
- `Disease`
- `Formulation`
- `Pharmacological Property`
- `Dosage`
- `Administration Guidelines`

## Accessing the Website
After running the Streamlit application, you can access the AyurGenixAI interface through the local server URL displayed in your terminal.

## Contributing
Contributions to the project are welcome! Feel free to submit pull requests, report issues, or suggest enhancements to improve AyurGenixAI.

**Thank you for choosing this project. Hoping that this project proves useful and delivers a seamless experience for your needs!**







