# 🏥 RAG Medical Chatbot

A Retrieval-Augmented Generation (RAG) based Medical Chatbot built using **LangChain**, **Flask**, **OpenAI GPT**, **HuggingFace**, and **Pinecone**.  
This project enables intelligent medical question answering by retrieving relevant context from a vector database and generating responses using an LLM.

---

## 📌 Project Overview

This application:

1. Converts medical documents into embeddings  
2. Stores embeddings inside Pinecone vector database  
3. Retrieves relevant context for user queries  
4. Generates accurate responses using GPT  
5. Provides a web interface using Flask  

---

## 🚀 Local Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/rktiwarimt007/rag_medical_chatbot.git
cd rag_medical_chatbot
```

---

## 2️⃣ Create Conda Environment

```bash
conda create -n medicalbot python=3.11 -y
conda activate medicalbot
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create Environment Variables

Create a `.env` file in the root directory:

```ini
PINECONE_API_KEY="your_pinecone_api_key"
OPENAI_API_KEY="your_openai_api_key"
```

---

## 5️⃣ Store Embeddings in Pinecone

Run the following command to generate and upload embeddings:

```bash
python store_index.py
```

---

## 6️⃣ Run the Application

```bash
python app.py
```

Open your browser and navigate to:

``
http://localhost:8080
``

---

## 🛠 Tech Stack

- **Python**
- **LangChain**
- **Flask**
- **OpenAI GPT**
- **HuggingFace**
- **Pinecone**
- **Docker**
- **AWS (EC2 + ECR)**
- **GitHub Actions (CI/CD)**

---

## ☁️ AWS CI/CD Deployment Guide

This project supports automated deployment using **GitHub Actions** and AWS services.

---

## 1️⃣ Login to AWS Console

Sign in to your AWS account.

---

## 2️⃣ Create IAM User for Deployment

### Required Access

- EC2 (Virtual Machine)
- ECR (Elastic Container Registry)

### Required IAM Policies

- `AmazonEC2ContainerRegistryFullAccess`
- `AmazonEC2FullAccess`

---

## 3️⃣ Create ECR Repository

Create a repository to store Docker images.

Example:

``
355222350521.dkr.ecr.ap-southeast-2.amazonaws.com/rag_medical_chatbot
``

Save the repository URI.

---

## 4️⃣ Launch EC2 Instance (Ubuntu)

Create an Ubuntu EC2 instance.

---

## 5️⃣ Install Docker on EC2

### Update System (Optional)

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
```

### Install Docker (Required)

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

---

## 6️⃣ Configure EC2 as GitHub Self-Hosted Runner

1. Go to your GitHub repository  
2. Navigate to: `Settings → Actions → Runners`  
3. Click **New Self-Hosted Runner**  
4. Select Ubuntu  
5. Run the provided commands inside EC2  

---

## 7️⃣ Setup GitHub Secrets

Go to:

``
Settings → Secrets and Variables → Actions
``

Add the following secrets:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_DEFAULT_REGION`
- `ECR_REPO`
- `PINECONE_API_KEY`
- `OPENAI_API_KEY`

---

## 🐳 Deployment Workflow

The CI/CD pipeline performs the following steps automatically:

1. Build Docker image  
2. Push image to AWS ECR  
3. Pull image inside EC2  
4. Run Docker container  

---

## 📂 Project Structure

```text
RAG_MEDICAL_CHATBOT/
│
├── data/
│   └── Medical_book.pdf          # Source medical document
│
├── research/
│   └── trials.ipynb              # Experimentation notebook
│
├── src/
│   ├── __init__.py
│   ├── helper.py                 # Utility functions
│   └── prompt.py                 # Prompt templates
│
├── static/
│   └── style.css                 # CSS styling
│
├── templates/
│   └── chat.html                 # Frontend UI
│
├── app.py                        # Main Flask application
├── store_index.py                # Embedding + Pinecone storage
├── requirements.txt              # Dependencies
├── setup.py                      # Package setup
├── template.sh                   # Shell script
├── .env                          # API keys (not pushed)
├── .gitignore
├── LICENSE
└── README.md
```

---

## ⚠️ Disclaimer

This chatbot is for educational and research purposes only.  
It is not intended to replace professional medical advice.

---

## 👨‍💻 Author

Developed as a RAG-based AI system for medical question answering.
