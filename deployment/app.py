from asyncio.windows_utils import pipe
import numbers
import streamlit as st
import pandas as pd
import pickle

complete = pickle.load(open('pipe.pkl', 'rb'))

st.header('Prediksi Harga Rental Property')

bedrooms = st.number_input ('Masukkan jumlah kamar tidur')
calculated_host_listings_count = st.number_input('Masukkan jumlah kamar mandi')
guests_included = st.number_input('Masukkan luas ruang tamu')
host_listings_count = st.number_input('Masukkan luas tanah (sqft)')
availability_30 = st.number_input('Masukkan jumlah lantai rumah')
review_scores_value = st.number_input('Masukkan luas atas(sqft)')

room_type = st.selectbox('Tipe room', ['Private room', 'Entire home/apt', 'Shared room'])
property_type = st.selectbox('Tipe property', ['House', 'Camper/RV', 'Bed & Breakfast', 'Apartment', 'Townhouse',
 'Condominium', 'Bungalow','Cabin' ,'Other', 'Loft' ,'Villa' ,'Treehouse',
 'Tent', 'Boat' ,'Hut' ,'Chalet' ,'Earth House', 'Tipi'])
cancellation_policy = st.selectbox('Cancellation policy', ['moderate', 'flexible', 'strict', 'super_strict_30' ,'no_refunds'])
bed_type = st.selectbox('Tipe Ranjang', ['Real Bed', 'Futon' ,'Airbed' ,'Pull-out Sofa', 'Couch'])

if st.button('Submit'):
    num_cols = ['bedrooms', 'calculated_host_listings_count', 'guests_included', 'host_listings_count', 'availability_30', 'review_scores_value']
    cat_cols = ['room_type', 'property_type', 'cancellation_policy', 'bed_type']
    
    num_df = pd.DataFrame([[bedrooms, calculated_host_listings_count, guests_included, host_listings_count, availability_30, review_scores_value]], columns = num_cols)
    cat_df = pd.DataFrame([[room_type, property_type, cancellation_policy, bed_type]], columns = cat_cols)

    X = pd.concat([num_df, cat_df], axis=1)

    st.write(X)
    st.text(complete.predict(X))
