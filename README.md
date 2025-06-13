# 📊 Amazon Sales Analytics Dashboard

This project is a **Streamlit web application** that provides comprehensive data analytics and visualization of an Amazon product sales dataset. Built with Python and several powerful data libraries, the dashboard allows users to interactively explore insights related to pricing, ratings, reviews, product performance, and more.


---

This Amazon Sales Analytics Dashboard which I extensively built can be accessed live on streamlit [Here](https://amazonanalytics.streamlit.app/)

---

## 📬 Author

**Gbenga Kajola**

[LinkedIn](https://www.linkedin.com/in/kajolagbenga)

[Certified_Data_Scientist](https://www.datacamp.com/certificate/DSA0012312825030)

[Certified_Data_Analyst](https://www.datacamp.com/certificate/DAA0018583322187)

[Certified_SQL_Database_Programmer](https://www.datacamp.com/certificate/SQA0019722049554)


---

## 📁 File Structure

```
📦 Amazon Sales Analytics/
├── amazon.csv       # Main dataset
├── main.py                   # Streamlit dashboard app
├── sales.ipynb       # Jupyter Notebook
├── requirements.txt                   # Installation of Dependencies
├── README.md                      # This readme file
```

---

## 🚀 Features

- Upload and process a real-world Amazon sales dataset.
- Interactive charts using **Seaborn** and **Matplotlib**.
- Review-based insights with **WordCloud** generation.
- Correlation heatmap of numeric features.
- Dynamic insights on:
  - Discounted prices
  - Discount percentage
  - Product popularity
  - Category performance
  - Ratings distribution
  - Review content and titles
- Clean layout using **Streamlit** with section headers and markdown.

---

## 📁 Dataset

- File: `amazon.csv`
- Format: CSV (Comma-Separated Values)
- Must include columns like:
  - `product_name`
  - `discounted_price`
  - `review_content`
  - `review_title`
  - `rating`
  - `category`
  - `discount_percentage`

Ensure the CSV file is clean and formatted correctly. The app also handles missing values by dropping them.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Streamlit**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **WordCloud**

---

## ⚙️ Installation & Setup

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

``` git clone https://github.com/prodigy234/Amazon-Sales-Analytics.git ```

``` cd Amazon-Sales-Analytics ```


### 2. Place Your Dataset
Ensure your amazon.csv file is in the same directory as main.py.


### 3. Create Virtual Environment (Recommended)
``` python -m venv venv ```
``` source venv/bin/activate```  # On Windows: ``` venv\Scripts\activate ```


### 4. Install Dependencies
``` pip install -r requirements.txt```


### 5. Run the Streamlit App
``` streamlit run main.py ```


## 🏁 License

MIT License – feel free to use and customize this for your business or learning projects.
