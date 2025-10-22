import streamlit as st
import cv2
import numpy as np
from PIL import Image
from deepface import DeepFace
import time

# Page config
st.set_page_config(
    page_title="Aura Detection System 🔥",
    page_icon="🔥",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        padding: 15px 30px;
        border-radius: 10px;
        border: none;
        font-weight: bold;
    }
    .success-box {
        background-color: #2b2b2b;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #4CAF50;
        text-align: center;
    }
    .error-box {
        background-color: #2b2b2b;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #ff4444;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

def analyze_gender(image):
    """Analyze gender using DeepFace"""
    try:
        # Convert PIL to numpy array
        img_array = np.array(image)
        
        # Analyze
        result = DeepFace.analyze(img_array, actions=['gender'], enforce_detection=False)
        
        if isinstance(result, list):
            result = result[0]
        
        gender = result['dominant_gender']
        confidence = result['gender'][gender]
        
        return gender, confidence
    except Exception as e:
        st.error(f"Analysis error: {e}")
        return None, 0

def show_result(gender, meme_image_path):
    """Display results with meme and message"""
    
    # Display meme image
    try:
        meme = Image.open(meme_image_path)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(meme, use_container_width=True)
    except:
        st.warning("⚠️ Meme image not found! Place male_meme.jpg and female_meme.jpg in the same folder.")
    
    # Display message based on gender
    if gender == 'Man':
        st.markdown("""
        <div class="success-box">
            <h1 style="color: #ff6b35;">🔥 NONCHALANT AURA DETECTED 🔥</h1>
            <h2 style="color: white;">NONCHALANT AURA GUY!</h2>
            <p style="color: #aaa; font-size: 18px;">
                You will be blessed with goth mommy and<br>
                South Indian baddies in 2 minutes! 🔥💯
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="error-box">
            <h1 style="color: #ff4444;">😤 AURA SCAN COMPLETE 😤</h1>
            <h2 style="color: white;">Ew chalant short auraless creature! 😤</h2>
            <p style="color: #aaa; font-size: 18px;">
                You will be blessed with 1 kg of apple, salt,<br>
                and a daily 2-hour aura farming class<br>
                by Sensei Varun-chan! 🍎🧂📚
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Balloons effect
    if gender == 'Man':
        st.balloons()

# Main app
def main():
    st.title("🔥 AURA DETECTION SYSTEM 🔥")
    st.markdown("### Discover your true aura level!")
    
    st.markdown("---")
    
    # Instructions
    with st.expander("📖 How to use"):
        st.write("""
        1. Click 'Take Photo' or upload an image
        2. Make sure your face is clearly visible
        3. Wait for the AI to analyze your aura
        4. Receive your blessing!
        """)
    
    # Option 1: Camera Input
    st.markdown("### 📸 Option 1: Take a Photo")
    camera_photo = st.camera_input("Smile for the camera!")
    
    if camera_photo:
        with st.spinner("🔮 Analyzing your aura..."):
            # Open image
            image = Image.open(camera_photo)
            
            # Analyze
            gender, confidence = analyze_gender(image)
            
            if gender and confidence > 50:
                st.success(f"✅ Detection confidence: {confidence:.1f}%")
                
                # Show result
                if gender == 'Man':
                    show_result(gender, "male_meme.jpg")
                else:
                    show_result(gender, "female_meme.jpg")
            else:
                st.error("❌ Could not detect face clearly. Please try again!")
    
    st.markdown("---")
    
    # Option 2: File Upload
    st.markdown("### 📁 Option 2: Upload an Image")
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    
    if uploaded_file:
        with st.spinner("🔮 Analyzing your aura..."):
            # Open image
            image = Image.open(uploaded_file)
            
            # Display uploaded image
            st.image(image, caption="Your Photo", use_container_width=True)
            
            # Analyze
            gender, confidence = analyze_gender(image)
            
            if gender and confidence > 50:
                st.success(f"✅ Detection confidence: {confidence:.1f}%")
                
                # Show result
                if gender == 'Man':
                    show_result(gender, "male_meme.jpg")
                else:
                    show_result(gender, "female_meme.jpg")
            else:
                st.error("❌ Could not detect face clearly. Please try again!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p>Made with 🔥 by Aura Masters</p>
        <p style='font-size: 12px;'>Powered by DeepFace AI</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
