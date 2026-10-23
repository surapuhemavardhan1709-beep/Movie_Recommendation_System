# Movie Recommendation System

## Project Overview

The Movie Recommendation System is a Machine Learning project that recommends movies based on the movie selected by the user.

The system analyzes movie information such as genres, keywords, cast, crew, and overview to find movies with similar characteristics.

The project also uses the TMDB API to display movie information and posters in the Streamlit application.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Natural Language Processing (NLP)
- NLTK
- TMDB API
- Jupyter Notebook

## Dataset

The project uses movie information from two CSV files:

- `movies.csv`
- `credits.csv`

The datasets contain information about movies, including:

- Movie title
- Genres
- Keywords
- Overview
- Cast
- Crew
- Director

## Project Workflow

```text
Movie Dataset
      ↓
Load movies.csv and credits.csv
      ↓
Merge the Datasets
      ↓
Select Required Features
      ↓
Handle Missing Values
      ↓
Combine Movie Information
      ↓
Text Preprocessing
      ↓
Stemming
      ↓
Bag of Words
      ↓
Cosine Similarity
      ↓
Movie Recommendation
      ↓
Streamlit Web Application
      ↓
TMDB Movie Posters
```

## Data Preprocessing

The project combines important movie information into a single `tags` column.

The tags are created using:

- Movie overview
- Genres
- Keywords
- Cast
- Director

The text is then converted to lowercase and processed using stemming so that similar words can be matched more effectively.

## Recommendation System

The project uses **Bag of Words** to convert movie text information into numerical vectors.

The resulting vectors are compared using **Cosine Similarity**.

The similarity matrix is then used to find movies that are most similar to the movie selected by the user.

## Model Details

The Bag of Words representation contains:

```text
4803 movies
5000 features
```

The cosine similarity matrix contains:

```text
4803 × 4803
```

Each movie can therefore be compared with the other movies in the dataset.

## Features

- Search/select a movie.
- Recommend similar movies.
- Uses movie metadata for recommendations.
- Displays movie posters using the TMDB API.
- Interactive Streamlit interface.
- Content-based movie recommendation.

## Streamlit Application

The project includes a Streamlit web application that allows the user to select a movie and receive recommended movies.

The application uses the TMDB API to retrieve movie poster information.

## Project Structure

```text
Movie_Recommendation_System/
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── README.md
│
└── data/
    ├── movies.csv
    └── credits.csv
```

## Installation

Install the required Python libraries:

```bash
pip install pandas numpy scikit-learn nltk streamlit requests
```

## TMDB API Setup

The Streamlit application uses the TMDB API to retrieve movie poster information.

Create a `.env` file and store the API key securely.

```text
TMDB_API_KEY=your_api_key_here
```

Do not upload your actual API key to GitHub.

## How to Run

Open the terminal inside the project folder and run:

```bash
streamlit run app.py
```

The application will open in your web browser.

## Example

The user selects a movie from the application.

The system analyzes the movie's characteristics and recommends similar movies.

```text
Selected Movie
      ↓
Movie Features
      ↓
Similarity Calculation
      ↓
Top Similar Movies
      ↓
Movie Posters
```

## Applications

This recommendation system can be used in:

- Movie streaming platforms
- Entertainment applications
- Personalized content recommendation
- Movie discovery systems
- Recommendation engine demonstrations

## Skills Demonstrated

This project demonstrates practical knowledge of:

- Python programming
- Data preprocessing
- Pandas and NumPy
- Natural Language Processing
- Text preprocessing
- Stemming
- Feature extraction
- Bag of Words
- Cosine Similarity
- Machine Learning
- Streamlit
- API integration

## Project Purpose

The purpose of this project is to build a content-based movie recommendation system and gain practical experience in Machine Learning, Natural Language Processing, recommendation systems, web application development, and API integration.

## Author

**Hema Vardhan Surapu**
