import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

st.title("Food Recommendation System")

######### Load Cleaned Data ##########

cleaned_data = pd.read_csv("D:/Swiggy/cleaned_data.csv")

###### Label Encode categorical columns #######

categorical_cols = ["city", "cuisine"]

label_encoders = {}
encoded_data = cleaned_data.copy()

for col in categorical_cols:
    le = LabelEncoder()
    encoded_data[col] = le.fit_transform(encoded_data[col].astype(str))
    label_encoders[col] = le


########## Scale numeric columns ##########
numeric_cols = ["rating", "rating_count", "cost"]

scaler = StandardScaler()
encoded_data[numeric_cols] = scaler.fit_transform(cleaned_data[numeric_cols])

########## KMeans Clustering #########

kmeans = KMeans(n_clusters=10, random_state=42)
encoded_data["cluster"] = kmeans.fit_predict(encoded_data[categorical_cols + numeric_cols])

# Add cluster back to cleaned_data
cleaned_data["cluster"] = encoded_data["cluster"]

######### Streamlit UI – Select Restaurant ########
restaurant_list = cleaned_data["name"].tolist()
selected_restaurant = st.selectbox("Select a Restaurant:", restaurant_list)

if st.button("Get Recommendations"):

    # Find selected restaurant
    selected_row = cleaned_data[cleaned_data["name"] == selected_restaurant].iloc[0]
    selected_cluster = selected_row["cluster"]

    # Restaurants in same cluster
    similar_restaurants = cleaned_data[
        (cleaned_data["cluster"] == selected_cluster) &
        (cleaned_data["name"] != selected_restaurant)
    ]

    st.subheader(" Recommended Restaurants")

    if similar_restaurants.empty:
        st.warning("No similar restaurants found in this cluster.")
    else:
        for _, row in similar_restaurants.head(10).iterrows():
            st.markdown(
                f"""
                <div style="background:#eef2f3; padding:10px; border-radius:10px; margin-bottom:10px;">
                    <h3>{row['name']}</h3>
                    <b>City:</b> {row['city']}<br>
                    <b>Rating:</b> {row['rating']} ({row['rating_count']} ratings)<br>
                    <b>Cost:</b> ₹{row['cost']}<br>
                    <b>Cuisine:</b> {row['cuisine']}
                </div>
                """,
                unsafe_allow_html=True
            )
