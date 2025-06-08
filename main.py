import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Page Configuration
st.set_page_config(page_title="Amazon Sales Analytics", layout="wide")

# Title
st.title("📊 Amazon Sales Analytics Dashboard")
st.markdown("An interactive dashboard showing insights from Amazon product data.")

# Load Dataset
@st.cache_data
def load_data():
    return pd.read_csv('amazon.csv')

df = load_data()
st.subheader("Data Preview")
st.dataframe(df.head())

# Display Data Info
st.subheader("Dataset Information")
buffer = df.info(buf=None)
st.text(str(buffer))

# Summary Statistics
st.subheader("Summary Statistics")
st.dataframe(df.describe())

# Missing Values
st.subheader("Missing Values")
st.dataframe(df.isnull().sum())

# Drop Missing Values
df.dropna(inplace=True)

# Convert Rating to Numeric
if 'rating' in df.columns:
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

# Sales Distribution
if 'discounted_price' in df.columns:
    st.subheader("Distribution of Discounted Prices")
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['discounted_price'], bins=30, kde=True, color='blue', ax=ax1)
    ax1.set_title('Discounted Price Distribution')
    st.pyplot(fig1)

# Top Products
if 'product_name' in df.columns and 'rating' in df.columns:
    st.subheader("Top 10 Most Reviewed Products")
    top_products = df.groupby('product_name')['rating'].count().nlargest(10)
    fig2, ax2 = plt.subplots(figsize=(12, 6))
    sns.barplot(y=top_products.index, x=top_products.values, palette='viridis', ax=ax2)
    ax2.set_title('Top 10 Most Reviewed Products')
    ax2.set_xlabel('Number of Reviews')
    st.pyplot(fig2)

# Review Titles
if 'review_title' in df.columns:
    st.subheader("Top 10 Most Frequent Review Titles")
    title_counts = df['review_title'].value_counts().nlargest(10)
    fig3, ax3 = plt.subplots(figsize=(12, 6))
    sns.barplot(y=title_counts.index, x=title_counts.values, palette='coolwarm', ax=ax3)
    ax3.set_title('Top Review Titles')
    ax3.set_xlabel('Count')
    st.pyplot(fig3)

# Word Cloud
if 'review_content' in df.columns:
    st.subheader("Word Cloud of Review Content")
    review_text = ' '.join(df['review_content'].dropna())
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(review_text)
    fig4, ax4 = plt.subplots(figsize=(10, 5))
    ax4.imshow(wordcloud, interpolation='bilinear')
    ax4.axis('off')
    st.pyplot(fig4)

# Ratings Distribution
if 'rating' in df.columns:
    st.subheader("Ratings Distribution")
    fig5, ax5 = plt.subplots(figsize=(10, 5))
    sns.countplot(x=df['rating'], palette='pastel', ax=ax5)
    ax5.set_title('Ratings Distribution')
    st.pyplot(fig5)

# Discount Percentage Distribution
if 'discount_percentage' in df.columns:
    st.subheader("Discount Percentage Distribution")
    fig6, ax6 = plt.subplots(figsize=(10, 5))
    sns.histplot(df['discount_percentage'], bins=30, kde=True, color='green', ax=ax6)
    ax6.set_title('Discount Percentage Distribution')
    st.pyplot(fig6)

# Correlation Heatmap
st.subheader("Correlation Heatmap of Numeric Features")
fig7, ax7 = plt.subplots(figsize=(12, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5, ax=ax7)
st.pyplot(fig7)

# Category-wise Average Ratings
if 'category' in df.columns and 'rating' in df.columns:
    st.subheader("Top 10 Categories by Average Rating")
    category_ratings = df.groupby('category')['rating'].mean().nlargest(10)
    fig8, ax8 = plt.subplots(figsize=(12, 6))
    sns.barplot(y=category_ratings.index, x=category_ratings.values, palette='plasma', ax=ax8)
    ax8.set_title('Top Categories by Average Rating')
    ax8.set_xlabel('Average Rating')
    st.pyplot(fig8)

# Footer
st.markdown("---")
st.markdown("# 👨‍💻 About the Developer")
st.markdown("## **Kajola Gbenga**")

st.markdown(
    """
📇 Certified Data Analyst | Certified Data Scientist | Certified SQL Programmer | Mobile App Developer

🔗 [LinkedIn](https://www.linkedin.com/in/kajolagbenga)  
📜 [View My Certifications & Licences](https://www.datacamp.com/portfolio/kgbenga234)  
💻 [GitHub](https://github.com/prodigy234)  
🌐 [Portfolio](https://kajolagbenga.netlify.app/)  
📧 k.gbenga234@gmail.com
"""
)


st.markdown("✅ Created using Python and Streamlit")