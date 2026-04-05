"""
import streamlit as st
import tensorflow as tf
import numpy as np

def model_prediction(test_image):

    model = tf.keras.models.load_model('my_model.keras')

    image = tf.keras.preprocessing.image.load_img(
        test_image,
        target_size=(128, 128)
    )

    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.expand_dims(input_arr, axis=0)

    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)

    return result_index

st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page" , ["Home" , "About" , "Disease Recogniition"])

if (app_mode == "Home"):
    st.header("Plant Disease Recogition System")
    image_path = "/Users/atharva/Documents/Projects/CSE/Aghri/bg.png"
    st.image(image_path , use_column_width=True)
    st.markdown()

elif (app_mode == "About"):
    st.header("About")
    st.markdown()

elif (app_mode == "Disease Recogniition"):
    st.header("Disease Recogniition")
    test_image = st.file_uploader("Choose an Image")
    if (st.button("Show Image")):
        st.image(test_image , use_column_width=True)
    
    if (st.button("Predict")):
        st.write("Our Prediction")
        result_index = model_prediction(test_image)
        class_name = ['Apple___Apple_scab',
            'Apple___Black_rot',
            'Apple___Cedar_apple_rust',
            'Apple___healthy',
            'Blueberry___healthy',
            'Cherry_(including_sour)___Powdery_mildew',
            'Cherry_(including_sour)___healthy',
            'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
            'Corn_(maize)___Common_rust_',
            'Corn_(maize)___Northern_Leaf_Blight',
            'Corn_(maize)___healthy',
            'Grape___Black_rot',
            'Grape___Esca_(Black_Measles)',
            'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
            'Grape___healthy',
            'Orange___Haunglongbing_(Citrus_greening)',
            'Peach___Bacterial_spot',
            'Peach___healthy',
            'Pepper,_bell___Bacterial_spot',
            'Pepper,_bell___healthy',
            'Potato___Early_blight',
            'Potato___Late_blight',
            'Potato___healthy',
            'Raspberry___healthy',
            'Soybean___healthy',
            'Squash___Powdery_mildew',
            'Strawberry___Leaf_scorch',
            'Strawberry___healthy',
            'Tomato___Bacterial_spot',
            'Tomato___Early_blight',
            'Tomato___Late_blight',
            'Tomato___Leaf_Mold',
            'Tomato___Septoria_leaf_spot',
            'Tomato___Spider_mites Two-spotted_spider_mite',
            'Tomato___Target_Spot',
            'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
            'Tomato___Tomato_mosaic_virus',
            'Tomato___healthy']
        st.success("Model is Predicting it's a {}".format(class_name[result_index]))

"""

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="PhytoScan · Plant Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: #1a1f16;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #1a1f16;
    border-right: none;
}
[data-testid="stSidebar"] * {
    color: #d4e3c3 !important;
}
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #f0f5ea !important;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: #8fa882 !important;
    font-size: 0.82rem;
    line-height: 1.6;
}
.sidebar-brand {
    font-family: 'DM Serif Display', serif;
    font-size: 1.6rem;
    color: #c8ddb4 !important;
    letter-spacing: -0.5px;
    padding: 0.5rem 0 0.25rem;
    display: block;
}
.sidebar-tagline {
    font-size: 0.75rem;
    color: #5a7050 !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 2rem;
    display: block;
}

/* ── Main content ── */
.main .block-container {
    padding: 2.5rem 3rem 3rem;
    max-width: 900px;
}

/* ── Page headers ── */
.page-header {
    margin-bottom: 2.5rem;
}
.page-header h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 2.6rem;
    font-weight: 400;
    color: #1a1f16;
    line-height: 1.15;
    margin: 0 0 0.4rem;
}
.page-header p {
    font-size: 1rem;
    color: #6b7c62;
    font-weight: 300;
    margin: 0;
    max-width: 520px;
    line-height: 1.65;
}

/* ── Divider ── */
.leaf-divider {
    border: none;
    border-top: 1px solid #dde8d5;
    margin: 2rem 0;
}

/* ── Stat cards ── */
.stat-row {
    display: flex;
    gap: 1.25rem;
    margin: 1.75rem 0;
}
.stat-card {
    flex: 1;
    background: #f4f8f0;
    border: 1px solid #dde8d5;
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
}
.stat-card .label {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 1.8px;
    color: #7d9570;
    margin-bottom: 0.35rem;
}
.stat-card .value {
    font-family: 'DM Serif Display', serif;
    font-size: 1.85rem;
    color: #1a1f16;
    line-height: 1;
}

/* ── Feature list ── */
.feature-item {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 0.85rem 0;
    border-bottom: 1px solid #edf2e8;
}
.feature-icon {
    width: 30px;
    height: 30px;
    background: #e6f0de;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.85rem;
    flex-shrink: 0;
    margin-top: 1px;
}
.feature-text strong {
    display: block;
    font-size: 0.9rem;
    font-weight: 600;
    color: #1a1f16;
    margin-bottom: 0.15rem;
}
.feature-text span {
    font-size: 0.82rem;
    color: #7d9570;
    line-height: 1.5;
}

/* ── Upload zone ── */
[data-testid="stFileUploader"] {
    border: 1.5px dashed #b5cfa5 !important;
    border-radius: 12px !important;
    background: #f9fbf7 !important;
    padding: 1.5rem !important;
    transition: border-color 0.2s;
}
[data-testid="stFileUploader"]:hover {
    border-color: #7aaa64 !important;
}

/* ── Buttons ── */
.stButton > button {
    border-radius: 8px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.875rem !important;
    letter-spacing: 0.3px !important;
    padding: 0.55rem 1.5rem !important;
    transition: all 0.18s ease !important;
}
.stButton > button[kind="primary"],
.stButton > button:first-child {
    background: #2d4a26 !important;
    border: none !important;
    color: #e8f0e3 !important;
}
.stButton > button:hover {
    background: #3d6234 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(45,74,38,0.25) !important;
}

/* ── Result card ── */
.result-card {
    background: linear-gradient(135deg, #f0f8e8 0%, #e8f4de 100%);
    border: 1px solid #c3dbb0;
    border-left: 4px solid #5a9e42;
    border-radius: 10px;
    padding: 1.5rem 1.75rem;
    margin-top: 1.5rem;
}
.result-card .result-label {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #5a7a4e;
    margin-bottom: 0.4rem;
}
.result-card .result-name {
    font-family: 'DM Serif Display', serif;
    font-size: 1.6rem;
    color: #1e3a18;
    margin-bottom: 0.3rem;
}
.result-card .result-sub {
    font-size: 0.83rem;
    color: #6b8a5e;
}

/* ── About page ── */
.about-section {
    background: #f9fbf7;
    border: 1px solid #dde8d5;
    border-radius: 10px;
    padding: 1.5rem 1.75rem;
    margin-bottom: 1.25rem;
}
.about-section h3 {
    font-family: 'DM Serif Display', serif;
    font-size: 1.15rem;
    font-weight: 400;
    color: #1a1f16;
    margin: 0 0 0.6rem;
}
.about-section p, .about-section li {
    font-size: 0.875rem;
    color: #5a7050;
    line-height: 1.7;
    margin: 0;
}

/* ── Selectbox ── */
[data-testid="stSelectbox"] > div > div {
    background: #1e2719 !important;
    border: 1px solid #3a4e32 !important;
    border-radius: 8px !important;
    color: #c8ddb4 !important;
}

/* ── Image display ── */
[data-testid="stImage"] img {
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)


# ── Helpers ────────────────────────────────────────────────────────────────────
CLASS_NAMES = [
    'Apple — Apple Scab', 'Apple — Black Rot', 'Apple — Cedar Apple Rust',
    'Apple — Healthy', 'Blueberry — Healthy',
    'Cherry — Powdery Mildew', 'Cherry — Healthy',
    'Corn — Cercospora / Grey Leaf Spot', 'Corn — Common Rust',
    'Corn — Northern Leaf Blight', 'Corn — Healthy',
    'Grape — Black Rot', 'Grape — Esca (Black Measles)',
    'Grape — Leaf Blight (Isariopsis)', 'Grape — Healthy',
    'Orange — Huanglongbing (Citrus Greening)',
    'Peach — Bacterial Spot', 'Peach — Healthy',
    'Pepper (Bell) — Bacterial Spot', 'Pepper (Bell) — Healthy',
    'Potato — Early Blight', 'Potato — Late Blight', 'Potato — Healthy',
    'Raspberry — Healthy', 'Soybean — Healthy',
    'Squash — Powdery Mildew',
    'Strawberry — Leaf Scorch', 'Strawberry — Healthy',
    'Tomato — Bacterial Spot', 'Tomato — Early Blight',
    'Tomato — Late Blight', 'Tomato — Leaf Mold',
    'Tomato — Septoria Leaf Spot',
    'Tomato — Spider Mites (Two-spotted)',
    'Tomato — Target Spot',
    'Tomato — Yellow Leaf Curl Virus',
    'Tomato — Mosaic Virus', 'Tomato — Healthy',
]

@st.cache_resource(show_spinner=False)
def load_model():
    return tf.keras.models.load_model('my_model.keras')

def predict(image_file):
    model = load_model()
    image = Image.open(image_file).resize((128, 128))
    arr = np.expand_dims(np.array(image), axis=0)
    preds = model.predict(arr)
    return np.argmax(preds), float(np.max(preds))


# ── Sidebar ─────────────────────────────────────────────────────────────────── 
with st.sidebar:
    st.markdown('<span class="sidebar-brand">PhytoScan</span>', unsafe_allow_html=True)
    st.markdown('<span class="sidebar-tagline">Plant Health Intelligence</span>', unsafe_allow_html=True)

    page = st.selectbox(
        "Navigate",
        ["Home", "About" , "Diagnose"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    st.markdown("""
    Upload a clear photo of a plant leaf to receive an instant disease diagnosis powered by deep learning.
    """)


# ── Home ───────────────────────────────────────────────────────────────────────
if page == "Home":
    st.markdown("""
    <div class="page-header">
        <h1>Plant Disease<br><em>Detection System</em></h1>
        <p>Identify crop diseases instantly from a single leaf photograph — across 14 plant species and 38 condition classes.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stat-row">
        <div class="stat-card">
            <div class="label">Plant Species</div>
            <div class="value">14</div>
        </div>
        <div class="stat-card">
            <div class="label">Disease Classes</div>
            <div class="value">38</div>
        </div>
        <div class="stat-card">
            <div class="label">Input Resolution</div>
            <div class="value">128px</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="leaf-divider">', unsafe_allow_html=True)
    st.markdown("#### How it works")

    features = [
        ("🌿", "Upload a Leaf Photo", "Take or select a clear, well-lit photo of the affected plant leaf."),
        ("🔬", "AI Analysis", "A convolutional neural network analyses visual patterns in the image."),
        ("📋", "Receive a Diagnosis", "Get the predicted condition name with confidence in seconds."),
    ]
    for icon, title, desc in features:
        st.markdown(f"""
        <div class="feature-item">
            <div class="feature-icon">{icon}</div>
            <div class="feature-text">
                <strong>{title}</strong>
                <span>{desc}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ── Diagnose ───────────────────────────────────────────────────────────────────
elif page == "Diagnose":
    st.markdown("""
    <div class="page-header">
        <h1>Leaf Diagnosis</h1>
        <p>Upload a leaf image below. For best results use a sharp, well-lit photograph with the leaf filling most of the frame.</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded = st.file_uploader(
        "Drop an image here, or click to browse",
        type=["jpg", "jpeg", "png", "webp"],
        label_visibility="collapsed",
    )

    if uploaded:
        col1, col2 = st.columns([1, 1], gap="large")

        with col1:
            st.markdown("**Uploaded image**")
            st.image(uploaded, use_column_width=True)

        with col2:
            st.markdown("**Run diagnosis**")
            st.markdown(
                "<p style='font-size:0.85rem;color:#7d9570;margin-bottom:1rem;'>"
                "The model will classify the leaf condition from the image you uploaded.</p>",
                unsafe_allow_html=True,
            )

            if st.button("Analyse Leaf", type="primary", use_container_width=True):
                with st.spinner("Analysing…"):
                    idx, confidence = predict(uploaded)
                    label = CLASS_NAMES[idx]
                    plant, condition = label.split(" — ", 1)

                st.markdown(f"""
                <div class="result-card">
                    <div class="result-label">Diagnosis Result</div>
                    <div class="result-name">{condition}</div>
                    <div class="result-sub">🌱 {plant} &nbsp;·&nbsp; {confidence*100:.1f}% confidence</div>
                </div>
                """, unsafe_allow_html=True)

                if "healthy" in condition.lower():
                    st.success("No disease detected — this leaf appears healthy.")
                else:
                    st.warning("Disease indicators detected. Consider consulting an agronomist for treatment advice.")
    else:
        st.info("No image uploaded yet. Select a leaf photo to get started.")


# ── About ──────────────────────────────────────────────────────────────────────
elif page == "About":
    st.markdown("""
    <div class="page-header">
        <h1>About PhytoScan</h1>
        <p>Technical details on the dataset, model architecture, and supported conditions.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="about-section">
        <h3>Dataset</h3>
        <p>
            The model was trained on the <strong>PlantVillage Dataset</strong> — a benchmark collection of
            over 87,000 leaf photographs spanning healthy and diseased specimens across 14 crop species.
            Images are captured under controlled laboratory conditions and cover 38 distinct condition classes.
        </p>
    </div>

    <div class="about-section">
        <h3>Model Architecture</h3>
        <p>
            A convolutional neural network trained end-to-end on 128 × 128 RGB leaf images.
            The model was trained using categorical cross-entropy loss and evaluated on a held-out
            test split, achieving high top-1 accuracy across all 38 classes.
        </p>
    </div>

    <div class="about-section">
        <h3>Supported Crops</h3>
        <p>Apple · Blueberry · Cherry · Corn (Maize) · Grape · Orange · Peach ·
        Pepper (Bell) · Potato · Raspberry · Soybean · Squash · Strawberry · Tomato</p>
    </div>

    <div class="about-section">
        <h3>Disclaimer</h3>
        <p>
            PhytoScan is an assistive tool intended for educational and research use.
            Diagnoses should be validated by a qualified agronomist before any treatment decisions are made.
        </p>
    </div>
    """, unsafe_allow_html=True)