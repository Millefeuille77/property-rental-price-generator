import numbers
import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('num_scaler.pkl', 'rb'))
encoder = pickle.load(open('cat_encoder.pkl', 'rb'))

st.header('Prediksi Harga Rumah')

bedroom = st.number_input ('Masukkan jumlah kamar tidur')
bathroom = st.number_input('Masukkan jumlah kamar mandi')
sqft_living = st.number_input('Masukkan luas ruang tamu')
sqft_lot = st.number_input('Masukkan luas tanah (sqft)')
floors = st.number_input('Masukkan jumlah lantai rumah')
sqft_above = st.number_input('Masukkan luas atas(sqft)')
sqft_basement = st.number_input('Masukkan luas basement(sqft)')
yr_built = st.number_input('Masukkan tahun rumah dibangun')
yr_renovated = st.number_input('Masukkan tahun rumah direnovasi')
lat = st.number_input('Masukkan lintang /latitude lokasi rumah')
long = st.number_input('Masukkan bujur/longitude lokasi rumah')
year = st.number_input('Masukkan tahun rumah yang ingin dilihat')

waterfront = st.selectbox('Apakah ada waterfront?', ['ada', 'tidak ada'])
view = st.selectbox('Pemandangan rumah', ['tidak ada', 'gunung', 'kota', 'danau'])
condition = st.selectbox('Kondisi Rumah', ['rusak parah', 'rusak sedang', 'rusak ringan', 'biasa', 'sangat bagus' ])
grade = st.selectbox('Grade', ['g1','g2','g3','g4','g5','g6','g7','g8','g9','g10','g11','g12','g13'])

if st.button('Submit'):
    num_cols = ['bedrooms','bathrooms','sqft_living','sqft_lot','floors','sqft_above','sqft_basement','yr_built','yr_renovated','lat','long','year']
    cat_cols = ['waterfront','view','condition','grade']
    
    num_df = pd.DataFrame([[bedroom, bathroom, sqft_living, sqft_lot, floors, sqft_above, sqft_basement, yr_built, yr_renovated, lat, long, year]], columns = num_cols)
    cat_df = pd.DataFrame([[waterfront, view, condition, grade]], columns = cat_cols)

    scaler_dat = pd.DataFrame(scaler.transform(num_df))
    encoded_dat = pd.DataFrame(encoder.transform(cat_df))
    X = pd.concat([scaler_dat, encoded_dat], axis=1)

    pred = model.predict(X)

    st.text(f'Harga Rumah: EUR {pred[0]}')