# Facial Moisturizer Pilling Prediction Model

A web-based interface for predicting product pilling based on physical properties of facial moisturizers.

## 🚀 Quick Start

### Installation

1. Install the required package:
```bash
pip install streamlit
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Navigate to the project directory:
```bash
cd "c:\Users\narayanan.k\Python\PillingModel"
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. The app will automatically open in your default web browser at `http://localhost:8501`

## 📊 How to Use

1. **Enter Product Name**: Identify your product
2. **Input Physical Properties**: Enter all 10 measurement values:
   - Modulus
   - Modulus Slope
   - Avg Time Weighted Force Area
   - Area Prior to Transition
   - Avg Break Time Delta
   - Max Break Time Delta
   - Peak 100
   - Plastic Viscosity1 at 10s-1
   - Stress Ratio Curve 1:3 at 10s-1
3. **Calculate**: Click the "Calculate Pilling Score" button
4. **Review Results**: See predictions from three different models and an average score

## 📈 Interpreting Results

- **Higher scores** = More pilling predicted
- **Lower scores** = Less pilling predicted
- The tool provides three model predictions and an averaged score
- Negative model values are automatically set to 0
- Color-coded interpretation helps assess risk level

## 🌐 Sharing the App

### Option 1: Share Locally (Same Network)
When running the app, you'll see a Network URL (e.g., `http://192.168.1.X:8501`). Share this URL with colleagues on the same network.

### Option 2: Deploy Online (Streamlit Cloud - Free)
1. Create a GitHub account (if you don't have one)
2. Upload these files to a GitHub repository:
   - `app.py`
   - `requirements.txt`
   - `README.md`
3. Go to [share.streamlit.io](https://share.streamlit.io)
4. Connect your GitHub repository
5. Share the public URL with anyone!

### Option 3: Deploy on Company Server
Contact your IT department to deploy this as a web service on your company's infrastructure.

## 📝 Notes

- All input fields accept decimal values
- Default values are provided as examples
- The model automatically handles negative predictions
- Results are displayed as percentages

## 🔧 Technical Details

The model uses three independent regression equations that incorporate various physical properties to predict pilling. Each model focuses on different property combinations, and the final score is an average of all three predictions (excluding any negative values from the average calculation).
