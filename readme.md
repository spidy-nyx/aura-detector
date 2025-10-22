# 🔥 Aura Detection System - Web App

Detect your aura level with AI! This web app analyzes faces and gives personalized "aura readings" with memes.

## 🚀 Quick Deploy to Streamlit Cloud (FREE!)

### Step 1: Prepare Your Files
Create a folder with these files:
```
aura-detector/
├── app.py              (the Streamlit code)
├── requirements.txt    (dependencies)
├── male_meme.jpg       (smug anime face image)
└── female_meme.jpg     (phone guy image)
```

### Step 2: Upload to GitHub
1. Go to [GitHub.com](https://github.com) and sign in (or create account)
2. Click the **"+"** button → **"New repository"**
3. Name it: `aura-detector`
4. Make it **Public**
5. Click **"Create repository"**
6. Upload all 4 files (drag & drop or click "uploading an existing file")
7. Click **"Commit changes"**

### Step 3: Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click **"New app"**
4. Select:
   - Repository: `your-username/aura-detector`
   - Branch: `main`
   - Main file path: `app.py`
5. Click **"Deploy!"**
6. Wait 2-3 minutes ⏳

### Step 4: Share the Link! 🎉
- Copy the URL (like `https://your-app.streamlit.app`)
- Send it to your friends!
- They can use it on phone/computer browser
- No installation needed!

---

## 🖥️ Local Testing (Optional)

Want to test before deploying?

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## 📱 How Friends Use It

1. Open the link on phone/computer
2. Click "Take Photo" or upload image
3. AI analyzes the face
4. Get custom aura reading with meme!

---

## 🔧 Troubleshooting

**Camera not working?**
- Allow camera permissions in browser
- Try the upload option instead

**Memes not showing?**
- Make sure `male_meme.jpg` and `female_meme.jpg` are uploaded to GitHub
- File names must match exactly (case-sensitive)

**Deployment failed?**
- Check all files are in the root folder (not in subfolders)
- Verify `requirements.txt` is properly formatted
- Wait a few minutes and try again

---

## 💡 Features

- ✅ Works on mobile & desktop browsers
- ✅ Camera or file upload
- ✅ Real-time AI detection
- ✅ Custom meme responses
- ✅ Free hosting forever
- ✅ No installation needed
- ✅ Shareable link

---

## 📊 Tech Stack

- **Streamlit** - Web framework
- **DeepFace** - AI gender detection
- **TensorFlow** - ML backend
- **OpenCV** - Image processing

---

## 🎨 Customization

Want to change the messages? Edit `app.py`:
- Line 70-80: Male message
- Line 82-92: Female message

Want different memes? Replace the image files!

---

## ⚠️ Important Notes

- First load takes 1-2 minutes (AI models downloading)
- Free tier has usage limits (but generous!)
- App sleeps after inactivity (wakes up on visit)

---

## 🤝 Credits

Made with 🔥 by the Aura Masters

---

**Need help?** Open an issue on GitHub or contact the creator!
