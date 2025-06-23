🏙️ Sustainable Smart City Assistant
------------------------------------

This AI-powered smart city platform includes:
✔️ Chat Assistant
✔️ Policy Summarizer
✔️ KPI Forecasting
✔️ Citizen Feedback
✔️ Eco Tips Generator
✔️ Anomaly Detection
✔️ Semantic Search (Policy Search)
✔️ KPI Dashboard

Developed using: Streamlit + Hugging Face + FAISS + scikit-learn

------------------------------------
🔧 Requirements
------------------------------------

1. Python 3.8+
2. pip package manager

------------------------------------
📦 Installation
------------------------------------

1. Clone this repo or download the zip:
   git clone https://github.com/prograto/smart-city-assistant.git

2. Navigate to the project folder:
   cd smart-city-assistant

3. Create and activate a virtual environment (recommended):

   Windows:
   python -m venv venv
   venv\Scripts\activate

   macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate

4. Install all dependencies:
   pip install -r requirements.txt

5. (One-time only) Download NLTK tokenizer:
   python
   >>> import nltk
   >>> nltk.download('punkt')
   >>> exit()

------------------------------------
🚀 Running the App Locally
------------------------------------

Run this command inside the project folder:

   streamlit run app.py

Then open the URL displayed in your terminal, usually:
   http://localhost:8501

------------------------------------
📂 Sample Upload Formats
------------------------------------

1. KPI CSV (for Forecasting / Dashboard)
----------------------------------------
KPI,Value
Water Usage,1600
Air Quality Index,75
Energy Usage,4500

2. Policy Document (for Summarizer / Search)
--------------------------------------------
Upload a `.txt` file containing city policy or rules.

------------------------------------
☁️ Deploy on Streamlit Cloud (Free)
------------------------------------

1. Push your project to GitHub
2. Go to: https://streamlit.io/cloud
3. Click **"New App"**
4. Connect your GitHub repo
5. Set main file as: `app.py`
6. Click **Deploy**

🎉 Your Smart City Assistant is now live!(Frontend deployment only) We nee to use Docker for backend Deployment too.
https://smart-city-assistant-prograto.streamlit.app/

------------------------------------
👨‍💻 Created by:
Chandu Smart techtuts(Prograto)
