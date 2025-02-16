# **Deployment Documentation for Doggo Down Under**

This document outlines the step-by-step process for deploying the **Doggo Down Under** e-commerce website to **Heroku**, including the database and AWS S3 bucket configuration.

---

## **Table of Contents**
1. [Project Prerequisites](#project-prerequisites)  
2. [Local Development Setup](#local-development-setup)  
3. [Setting Up Heroku](#setting-up-heroku)  
4. [Configuring the Database (PostgreSQL)](#configuring-the-database-postgresql)  
5. [Deploying to Heroku](#deploying-to-heroku)  
6. [Static & Media File Storage (AWS S3)](#static--media-file-storage-aws-s3)  
7. [Environment Variables](#environment-variables)  
8. [Final Deployment Steps](#final-deployment-steps)  
9. [Post-Deployment Testing](#post-deployment-testing)  

---

## **1. Project Prerequisites**
Before deploying, ensure you have the following installed on your local machine:
- Python 3.10.11  
- Django  
- PostgreSQL (for local testing)  
- Git  
- Heroku CLI  
- Stripe account for payment processing  
- AWS S3 Bucket for static & media file storage  

---

## **2. Local Development Setup**
### **Clone the Repository**
```sh
git clone <repository-url>
cd doggo-down-under
```

### **Create a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
```

### **Install Dependencies**
```sh
pip install -r requirements.txt
```

### **Set Up a Local `.env` File**
Create a `.env` file in the root directory and add:
```sh
SECRET_KEY="your-secret-key"
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL="your-postgres-url"
STRIPE_PUBLIC_KEY="your-stripe-public-key"
STRIPE_SECRET_KEY="your-stripe-secret-key"
AWS_ACCESS_KEY_ID="your-aws-access-key"
AWS_SECRET_ACCESS_KEY="your-aws-secret-key"
AWS_STORAGE_BUCKET_NAME="your-bucket-name"
```

### **Apply Migrations & Run Server**
```sh
python manage.py migrate
python manage.py runserver
```
Check `http://127.0.0.1:8000/` to ensure it works.

---

## **3. Setting Up Heroku**
### **Create a Heroku App**
Log in to Heroku and create an app:
```sh
heroku login
heroku create doggo-down-under
```

### **Add Buildpacks**
Set the required buildpacks:
```sh
heroku buildpacks:add heroku/python
heroku buildpacks:add https://github.com/heroku/heroku-buildpack-python
```

---

## **4. Configuring the Database (PostgreSQL)**
### **Install PostgreSQL Locally**
```sh
pip install psycopg2-binary
```

### **Add Heroku Postgres**
```sh
heroku addons:create heroku-postgresql:hobby-dev
```

### **Get Database URL**
```sh
heroku config
```
Copy the `DATABASE_URL` and update `.env`:
```sh
DATABASE_URL="your-heroku-postgres-url"
```

### **Apply Migrations**
```sh
heroku run python manage.py migrate
```

---

## **5. Deploying to Heroku**
### **Initialize Git & Add Remote**
```sh
git init
heroku git:remote -a doggo-down-under
```

### **Push Code to Heroku**
```sh
git add .
git commit -m "Initial Deployment"
git push heroku main
```

### **Create a Superuser**
```sh
heroku run python manage.py createsuperuser
```

---

## **6. Static & Media File Storage (AWS S3)**
### **1. Create an AWS S3 Bucket**
1. Go to [AWS S3](https://s3.console.aws.amazon.com/s3/)  
2. Click **Create Bucket**  
3. Name it (e.g., `doggo-down-under-media`)  
4. Uncheck **Block all public access**  
5. Enable **Bucket Versioning**  
6. Click **Create Bucket**  

### **2. Create AWS IAM User**
1. Go to **AWS IAM Console**  
2. Create a **new user** with **programmatic access**  
3. Attach **AmazonS3FullAccess** policy  
4. Copy **Access Key ID** & **Secret Access Key**  

### **3. Install Required Packages**
```sh
pip install boto3 django-storages
```

### **4. Configure `settings.py`**
Add this to **`INSTALLED_APPS`**:
```python
INSTALLED_APPS += ['storages']
```

Define the AWS storage settings:
```python
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'us-east-1'  # Change based on your bucket's region
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
```

### **5. Set AWS Credentials in Heroku**
```sh
heroku config:set AWS_ACCESS_KEY_ID="your-aws-access-key"
heroku config:set AWS_SECRET_ACCESS_KEY="your-aws-secret-key"
heroku config:set AWS_STORAGE_BUCKET_NAME="your-bucket-name"
```

### **6. Collect Static Files**
```sh
python manage.py collectstatic
```

---

## **7. Environment Variables**
Set environment variables in Heroku:
```sh
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set STRIPE_PUBLIC_KEY="your-stripe-public-key"
heroku config:set STRIPE_SECRET_KEY="your-stripe-secret-key"
heroku config:set AWS_ACCESS_KEY_ID="your-aws-access-key"
heroku config:set AWS_SECRET_ACCESS_KEY="your-aws-secret-key"
heroku config:set AWS_STORAGE_BUCKET_NAME="your-bucket-name"
```

---

## **8. Final Deployment Steps**
### **Enable Automatic Deploys (Optional)**
1. Connect your Heroku app to GitHub in the Heroku dashboard.
2. Enable **Automatic Deploys** for the `main` branch.

### **Verify Deployment**
Open the app in a browser:
```sh
heroku open
```

Congratulations! The website is now deployed succesfully :)