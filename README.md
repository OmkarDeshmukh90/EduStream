# EduStream
This repository contains code for a College Recommendation System built using Python and Streamlit. The system helps students find colleges based on their marks and preferred branch of study.

## Overview

The EduStream System consists of the following components:

1. **Authentication**: Users need to verify their email address to access the system. Upon successful verification, they can log in and use the recommender.
   
2. **EduStream**: Authenticated users can input their marks and preferred branch of study. The system then recommends colleges based on these criteria.

## Dependencies

Make sure you have the following dependencies installed:

- Python 3
- Streamlit
- Pandas
- smtplib (for email functionality)

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/OmkarDeshmukh90/EduStream.git
```

2. Navigate to the project directory:

```bash
cd EduStream
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run College_recommender.py
```

5. Access the application through your web browser at `http://localhost:8501`.

## Features

- **Email Verification**: Users need to verify their email address before accessing the system, ensuring security and authenticity.
  
- **Personalization**: Users can input their marks and preferred branch of study, and the system recommends colleges tailored to their preferences.

- **Dynamic Recommendations**: The system dynamically filters colleges based on the user's input, providing relevant recommendations in real-time.

## Data

The college data used for recommendations is stored in an Excel file (`college_database.xlsx`). Ensure that the file is properly formatted and contains the necessary information.

