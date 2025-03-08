# Job Chat

## Overview
Job Chat is an AI-powered job search assistant built using Streamlit and Google Gemini Pro. This application helps users find job descriptions and related links for professions they search for. It also maintains a search history for easy access.

## Features
- **AI-Powered Job Search:** Uses Google Gemini Pro API to provide profession-related insights.
- **Job Search Links:** Directs users to job listings on LinkedIn, Naukri, and Indeed.
- **Search History:** Keeps track of recent job searches for quick reference.
- **Custom Themes:** Light and Dark mode themes for better UI experience.

## Technologies Used
- **Python**
- **Streamlit**
- **Google Generative AI (Gemini Pro API)**
- **dotenv** (for API key management)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/job-chat.git
   cd job-chat
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the project root directory.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Running the Application
Run the Streamlit app using the following command:
```sh
streamlit run app.py
```

## File Structure
```
job-chat/
│── app.py              # Main Streamlit app
│── requirements.txt    # Dependencies
│── .env                # Environment variables
│── joblist.txt         # List of professions
│── README.md           # Documentation
```

## Usage
1. Open the application in your browser.
2. Enter a profession in the search bar.
3. Click **Search** to get:
   - A brief AI-generated description.
   - Links to job postings on LinkedIn, Naukri, and Indeed.
   - A history of previous searches.
4. Toggle between Light and Dark mode using the sidebar.

## Troubleshooting
- **Missing API Key:** Ensure you have added `GOOGLE_API_KEY` to your `.env` file.
- **File Not Found Error:** Ensure `joblist.txt` is available in the project directory.
- **Dependencies Issue:** Run `pip install -r requirements.txt` to install missing packages.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests on GitHub.

## License
This project is licensed under the MIT License.

## Author
Your Name - [Your GitHub](https://github.com/ayushcodes404)


