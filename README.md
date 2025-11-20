**Problem Statement:**
The objective is to build a recommendation system based on restaurant data provided in a CSV file. The system should recommend restaurants to users based on input features such as city, rating, cost, and cuisine preferences. The application will utilize clustering or similarity measures to generate recommendations and display results in an easy-to-use Streamlit interface.

By the end of this project, you will:

1)Perform data cleaning and preprocessing.

2)Encode categorical features using One-Hot Encoding.

3)Apply clustering or similarity-based methods for recommendations.

4)Build a Streamlit application to showcase recommendations.



**Business Use Cases:**
1)Personalized Recommendations: Help users discover restaurants based on their preferences.
2)Improved Customer Experience: Provide tailored suggestions to enhance decision-making.
3)Market Insights: Understand customer preferences and behaviors for targeted marketing.
4)Operational Efficiency: Enable businesses to optimize their offerings based on popular preferences.


**Approach:**
1. Data Understanding and Cleaning
Duplicate Removal: Identify and drop duplicate rows.
Handling Missing Values: Impute or drop rows with missing values.
Save the cleaned data to a new CSV file (cleaned_data.csv).

2. Data Preprocessing
Encoding: Apply One-Hot Encoding to categorical features ( city, cuisine).
Save the encoder as a Pickle file (encoder.pkl).
Ensure all features are numerical after encoding.
Create a preprocessed dataset (encoded_data.csv).
Ensure the indices of cleaned_data.csv and encoded_data.csv match.

3. Recommendation Methodology
Clustering or Similarity Measures:
Use K-Means Clustering or Cosine Similarity to identify similar restaurants based on input features.
Use the encoded dataset for computations.
Result Mapping:
Map the recommendation results (indices) back to the non-encoded dataset (cleaned_data.csv).

5. Streamlit Application
Build an interactive application with the following components:
User Input: Accept user preferences (e.g., city, cuisine, rating,price,etc).
Recommendation Engine: Process the input, query the encoded data, and generate recommendations.
Output: Display recommended restaurants using cleaned_data.csv.
