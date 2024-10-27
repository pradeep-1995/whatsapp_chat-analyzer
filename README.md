---

# WhatsApp Chat Analyzer

https://pradeep-1995-whatsapp-chat-analyzer-app-mzvcas.streamlit.app/
## Overview

The **WhatsApp Chat Analyzer** is a Python-based web application built using Streamlit that provides insights and analytics from WhatsApp chat exports. It enables users to visualize and analyze various aspects of their chats, including message statistics, user activity, word frequency, emoji usage, and more.

## Features

- **Upload WhatsApp Chat Export:** Users can upload their chat export files in `.txt` format.
- **Chat Statistics:** Displays overall chat statistics including total messages, words, links shared, and media sent.
- **Timeline Visualizations:** Monthly and daily timelines to show message activity over time.
- **User Activity Analysis:** Insights into the most active users and their messaging patterns.
- **Word Cloud Visualization:** Generate and display a word cloud of the most frequently used words.
- **Emoji Analysis:** Visual representation of the emojis used in the chat.
- **Interactive Dashboard:** User-friendly interface to explore different analyses.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/whatsapp-chat-analyzer.git
   cd whatsapp-chat-analyzer
   ```

2. **Set Up a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**

   Make sure you have `pip` installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain the necessary packages, such as:

   ```
   streamlit
   pandas
   matplotlib
   seaborn
   wordcloud
   emoji
   urlextract
   ```

## Usage

1. **Run the Application:**

   To start the Streamlit application, use the following command:

   ```bash
   streamlit run app.py
   ```

   Replace `app.py` with the name of your main Python script if it's different.

2. **Upload a WhatsApp Chat File:**

   - Open the application in your browser (usually at `http://localhost:8501`).
   - Use the sidebar to upload a `.txt` file of your WhatsApp chat export.

3. **Select a User for Analysis:**

   - From the dropdown menu, choose the user you want to analyze or select 'Overall' for group statistics.

4. **View the Results:**

   - Click on the "Show Analysis" button to display the chat analysis, which includes statistics, visualizations, and more.

## Components

### Main Components

- **`preprocessor.py`:** Handles preprocessing of chat data, including timestamp conversion and extracting messages.
- **`helper.py`:** Contains functions to compute statistics, generate visualizations, and create word clouds.
- **`app.py`:** The main Streamlit application that brings together all components and displays the dashboard.

## Contributing

Contributions are welcome! If you would like to contribute to the WhatsApp Chat Analyzer, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and commit them: `git commit -m 'Add your feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/)
- [WordCloud](https://github.com/amueller/word_cloud)
- [Pandas](https://pandas.pydata.org/)

---
