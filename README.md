````markdown
# ✉️ AI Email Generator

An AI-powered web application that generates professional emails using Google's Gemini AI and Streamlit.

## 🚀 Features

- Generate professional emails with AI
- Multiple email types
- Multiple writing tones
- Short, medium, and detailed email lengths
- Custom recipient and purpose
- Additional details support
- Editable generated email
- Download generated email as a text file
- Simple and responsive Streamlit interface

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK

## 📁 Project Structure

```text
ai-email-generator/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
````

## ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project folder:

```bash
cd ai-email-generator
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 API Key Setup

The application requires a Gemini API key.

### Local Development

Create this folder:

```text
.streamlit/
```

Inside it, create:

```text
secrets.toml
```

Add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

**Never upload `secrets.toml` to GitHub.**

The `.gitignore` file already excludes the `.streamlit` folder.

## ▶️ Run the Application

Run:

```bash
streamlit run app.py
```

The application will open in your browser.

## ☁️ Streamlit Cloud Deployment

1. Upload this project to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Select `app.py` as the main file.
5. Add your Gemini API key in the application's Secrets settings.
6. Deploy the application.

For Streamlit Cloud, use:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Do not put the actual API key inside `app.py`.

## 🔒 Security

Never commit:

* Gemini API keys
* `.streamlit/secrets.toml`
* `.env` files
* Passwords
* Private credentials

## 📄 License

This project is for educational and personal use.

```
```
