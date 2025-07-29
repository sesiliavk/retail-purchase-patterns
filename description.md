# Judul Project
Analisis Karakteristik Pelanggan dan Preferensi Produk untuk Strategi Promosi yang Efektif

## Repository Outline
1. P2M3_Sesilia_Virdha_ddl.txt : untuk menyimpan link dataset dan syntax sql
2. P2M3_Sesilia_Virdha_data_raw.csv : File ini berisi dataset original
3. P2M3_Sesilia_Virdha_data_clean.csv : File ini berisi data yang telah dilakukan Data Cleaning
4. P2M3_Sesilia_Virdha_DAG.py : File yang berisi DAG untuk dijalankan dengan menggunakan Apache Airflow
5. P2M3_Sesilia_Virdha_conceptual.txt : File ini berisi jawaban conceptual problem
6. P2M3_Sesilia_Virdha_GX.ipynb : File ini berisi Expectations yang digunakan untuk melakukan validasi data.
7. Folder Images : Folder ini berisi daftar screenshot EDA

## Problem Background
 Di era globalisasi ini, konsumen kini memiliki berbagai pilihan dalam menentukan produk, metode pembayaran, hingga metode pengiriman. Persaingan retail menjadi semakin ketat karena konsumen cenderung lebih selektif dan loyal terhadap brand yang mampu memahami kebutuhan konsumen secara personal. Sehingga untuk mengoptimalkan penjualan dan penawaran produk, dibutuhkannya data yang menggambarkan pola pembelian dan preferensi pelanggan untuk dianalisis guna merencanakan strategi promosi yang tepat sesuai karakteristik konsumen

## Project Output
Visualisasi dan dashboard di kibana

## Data
Dataset ini bersumber dari Kaggle dengan jumlah kolom 18, 3900 baris, dan terdapat missing value
| Field Name          | Description                                                                                           |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Customer ID         | A unique identifier assigned to each individual customer, facilitating tracking and analysis of their shopping behavior over time. |
| Age                 | The age of the customer, providing demographic information for segmentation and targeted marketing strategies. |
| Gender              | The gender identification of the customer, a key demographic variable influencing product preferences and purchasing patterns. |
| Item Purchased      | The specific product or item selected by the customer during the transaction.                        |
| Category            | The broad classification or group to which the purchased item belongs (e.g., clothing, electronics, groceries). |
| Purchase Amount (USD)| The monetary value of the transaction, denoted in United States Dollars (USD), indicates the cost of the purchased item(s). |
| Location            | The geographical location where the purchase was made, offering insights into regional preferences and market trends. |
| Size                | The size specification (if applicable) of the purchased item, relevant for apparel, footwear, and certain consumer goods. |
| Color               | The color variant or choice associated with the purchased item, influencing customer preferences and product availability. |
| Season              | The seasonal relevance of the purchased item (e.g., spring, summer, fall, winter), impacting inventory management and marketing strategies. |
| Review Rating       | A numerical or qualitative assessment provided by the customer regarding their satisfaction with the purchased item. |
| Subscription Status | Indicates whether the customer has opted for a subscription service, offering insights into their level of loyalty and potential for recurring revenue. |
| Shipping Type       | Specifies the method used to deliver the purchased item (e.g., standard shipping, express delivery), influencing delivery times and costs. |
| Discount Applied    | Indicates if any promotional discounts were applied to the purchase, shedding light on price sensitivity and promotion effectiveness. |
| Promo Code Used     | Notes whether a promotional code or coupon was utilized during the transaction, aiding in the evaluation of marketing campaign success. |
| Previous Purchases  | Provides information on the number or frequency of prior purchases made by the customer, contributing to customer segmentation and retention strategies. |
| Payment Method      | Specifies the mode of payment employed by the customer (e.g., credit card, cash), offering insights into preferred payment options. |
| Frequency of Purchases | Indicates how often the customer engages in purchasing activities, a critical metric for assessing customer loyalty and lifetime value. |


## Method
Menggunakan Docker untuk menjalankan Elasticsearch, Kibana, airflow, dan postgreSQL.

## Stacks
Bahasa Pemrograman : Python

Tools : VSCode, Docker

Library : Pandas, Great Expectations, Apache Airflow, Elastic Search, sqlalchemy

## Reference
Dataset : https://www.kaggle.com/datasets/zeesolver/consumer-behavior-and-shopping-habits-dataset/data

---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)