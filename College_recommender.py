import streamlit as st
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random

# Function to generate a random 4-digit code
def generate_verification_code():
    return str(random.randint(1000, 9999))

# Function to send an email with the verification code
def send_verification_email(to_email, code):
    # Email configuration
    sender_email = 'omraje5990@gmail.com'  # Update with your email address
    sender_password = 'pigz pkim eklp srgs'  # Update with your email app password
    smtp_server = 'smtp.gmail.com'  # Update with your SMTP server address
    smtp_port = 587  # Update with your SMTP server port (587 is typical for TLS)

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = "Verification Code"

    # Add message body with the verification code
    body = f"Your verification code is: {code}"
    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
        return True
    except Exception as e:
        st.error(f"An error occurred while sending the verification code: {str(e)}")
        return False

# Function to verify the entered code
def verify_code(entered_code, verification_code):
    if entered_code == verification_code:
        return True
    else:
        return False

# Function to load data
def load_data(file_path):
    # Load data from Excel file
    data = pd.read_excel(file_path)
    return data

# Function to recommend colleges
def recommend_colleges(data, user_marks, user_branch):
    # Filter colleges based on user's marks and branch preference
    recommended_colleges = data[(data['cutoff'] < user_marks) & (data['branch'] == user_branch)]
    return recommended_colleges

def main():
    st.title("College Recommender")

    # Initialize session state variables
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'user_name' not in st.session_state:
        st.session_state.user_name = ""

    # If user is not authenticated, show authentication form
    if not st.session_state.authenticated:
        st.write("Please verify your email address to access the college recommender.")

        # User input for email address
        recipient_email = st.text_input("Enter Your Email Address")

        # Send verification code button
        if st.button("Send Verification Code"):
            if recipient_email:
                # Generate a random 4-digit verification code
                verification_code = generate_verification_code()

                # Send the verification code via email
                if send_verification_email(recipient_email, verification_code):
                    st.success("Verification code sent successfully! Please check your email.")
                    st.session_state.verification_code = verification_code
                    st.session_state.recipient_email = recipient_email
                else:
                    st.error("Failed to send verification code. Please try again.")
            else:
                st.error("Please enter your email address.")

        # If verification code has been sent, show input field for verification code
        if 'verification_code' in st.session_state:
            entered_code = st.text_input("Enter the Verification Code")
            if st.button("Verify Code"):
                if verify_code(entered_code, st.session_state.verification_code):
                    st.success("Verification successful! You are now logged in.")
                    st.session_state.authenticated = True

                    # Prompt user to enter their name
                    st.session_state.user_name = st.text_input("Enter Your Name")

                else:
                    st.error("Verification failed. Please enter the correct verification code.")
    
    # If user is authenticated, show college recommender
    else:
        # Display user's name in upper left corner
        st.sidebar.title(f"Logged in as: {st.session_state.user_name}")

        # Load data
        file_path = "college_database.xlsx" # Update with your file path
        colleges_data = load_data(file_path)

        # Sidebar inputs
        st.sidebar.header("Enter Your Details")
        user_marks = st.sidebar.number_input("Enter Your Marks")  
        branch_options = colleges_data['branch'].unique().tolist()
        user_branch = st.sidebar.selectbox("Select Your Preferred Branch", branch_options)

        # Recommend colleges based on user's marks and branch preference
        recommended_colleges = recommend_colleges(colleges_data, user_marks, user_branch)

        # Display recommended colleges
        st.subheader("Recommended Colleges")
        if recommended_colleges.empty:
            st.write("No colleges found with cutoff marks less than your entered marks or in your preferred branch.")
        else:
            st.write(recommended_colleges)

if __name__ == "__main__":
    main()
