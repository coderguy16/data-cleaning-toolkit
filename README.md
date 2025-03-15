# 🌍 GDP Data Transformation Toolkit | Clean & Analyze Time Series Data

**Convert messy, wide-format GDP spreadsheets into analysis-ready datasets.**  
*Perfect for researchers, economists, and data teams needing clean time series data.*

## Source

The data in this repo was obtained from [The World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.CD).

---

## 🛠️ Features
- **Reshape Data**: Transform wide-format years (1960, 1961...) into a tidy `year` column.  
- **Enrich Metadata**: Merge country codes with regions and income groups.  
- **Handle Missing Data**: Clean `NaN`/empty values for seamless analysis.  
- **Export-Ready**: Save to CSV/Excel for use in tools like Power BI or Tableau.

---

## 📥 Input → 📤 Output  
| **Input Columns** | **Output Columns** |  
|--------------------|---------------------|  
| `Country Name`     | `Country Name`      |  
| `Country Code`     | `Country Code`      |  
| `1960`, `1961`...  | `year` (datetime)   |  
| `Indicator Name`   | `gdp` (numeric)     |  
| ...                | `Region`            |  
|                    | `IncomeGroup`       |  

---

## 🚀 Quick Start  
### Install & Run  
```bash  
git clone https://github.com/coderguy16/data-cleaning-toolkit.git 
cd data-cleaning-toolkit 
# Set up environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt  
python src/main.py  
