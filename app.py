import streamlit as st
import pandas as pd

# Pre-defined set of fixtures (you can add more here)
fixtures = [
    ('Manchester United', 'Liverpool'),
    ('Arsenal', 'Chelsea'),
    ('Manchester City', 'Tottenham'),
    ('Leeds', 'Bournemouth')
]

# A global dataframe to store predictions
df = pd.DataFrame(columns=['Name', 'Home Team', 'Home Prediction', 'Away Team', 'Away Prediction'])

st.title("Predix 2024 Week 6")

with st.form("prediction_form"):
    name = st.text_input("Your Name")
    
    st.write("Enter your predictions for the following fixtures:")
    
    # List to store each fixture's predictions
    predictions = []
    
    for home_team, away_team in fixtures:
        col1, col2, col3, col4 = st.columns([3, 1, 3, 1])
        
        # Display teams in two columns with score inputs
        with col1:
            st.write(home_team)
        with col2:
            home_score = st.number_input(f"Score", min_value=0, max_value=10, step=1, key=f"{home_team}_score")
        with col3:
            st.write(away_team)
        with col4:
            away_score = st.number_input(f"Score", min_value=0, max_value=10, step=1, key=f"{away_team}_score")
        
        # Collect the input for this fixture
        predictions.append({
            'Name': name,
            'Home Team': home_team,
            'Home Prediction': home_score,
            'Away Team': away_team,
            'Away Prediction': away_score
        })
    
    submit = st.form_submit_button("Submit Prediction")
    
    if submit:
        # Convert list of predictions into a dataframe
        pred_df = pd.DataFrame(predictions)
        
        # Concatenate the new predictions with the existing dataframe
        df = pd.concat([df, pred_df], ignore_index=True)
        
        st.write("Your predictions have been submitted!")
        st.dataframe(df)  # Display updated dataframe
