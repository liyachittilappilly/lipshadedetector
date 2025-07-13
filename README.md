
# 💄 Lipstick Shade Detector



## 🌸 Project Overview

Welcome to the **Lipstick Shade Detector** — an AI-powered web application that detects the lipstick shade you're wearing using your webcam. Whether you're going for a subtle nude or a bold cherry red, this project identifies your lip color and names the closest known shade using a curated palette of beautiful lipstick tones. All wrapped in a dreamy pastel aesthetic ✨

---

## 📸 What It Does

- Activates your **webcam** to capture real-time facial data.
- Uses **MediaPipe FaceMesh** to pinpoint your **upper & lower lip regions**.
- Calculates the **average color** of both lip regions.
- Matches it to the closest known shade in a custom lipstick dictionary using **Lab color space conversion** for accurate matching.
- Displays results with soft UI and subtle blur effects on an aesthetic web page 💕

---


## 🧠 Tech Stack

| Category        | Tech Used                     |
|----------------|-------------------------------|
| 🧠 Machine Vision | Python, OpenCV, MediaPipe       |
| 💄 Color Matching | `skimage.color`, `webcolors` |
| 🎨 Design & UI     | HTML, CSS (Glassmorphism style) |
| 🌐 Framework     | Flask (Python Web Framework) |
| 📷 Input Device   | Webcam (via OpenCV)           |

---

## 🪞 Features

- 🎯 Real-time lipstick detection
- 💖 Elegant front-end styling
- 💅 Matches lipstick shade using perceptual color distance
- 🌐 Flask-powered lightweight web server
- 👁️‍🗨️ Uses both upper and lower lips for precise prediction

---

## 📂 Project Structure

```bash
lipstick-detector/
├── app.py                 # Flask app runner
├── detect_lipstick.py     # Main detection logic
├── static/
│   └── style.css          # All the pink & pretty
│   └── chromebook wallpaper.jpg  # Background aesthetic
├── templates/
│   └── index.html         # Front-end HTML
└── README.md              # You're here!
````

---

## 💌 How to Run

> 📝 Make sure you have Python 3 installed along with pip.

1. **Clone this repo**

```bash
git clone https://github.com/yourusername/lipstick-detector.git
cd lipstick-detector
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
python app.py
```

4. **Open in browser**
   Visit `http://127.0.0.1:5000/` to start detecting 💋

---

## 🎀 Shades in the Palette

A sample of the beautiful lipstick colors used:

* 💕 Rose Pink
* 💋 Cherry Red
* 🌸 Dusty Rose
* 🍑 Peach
* 🍷 Wine
* 🖤 Deep Red
* ✨ Mauve
* 🔥 Brick
  ...and many more!

---

## 💻 Future Enhancements

* 📱 Mobile version with responsive layout
* 💾 Save detected shade history
* 🎯 Allow user to upload photo instead of webcam
* 💬 Recommend similar shades from popular brands

---

## 👑 Made By

💖 **Liya S Chittilappilly**
🧠 Computer Science Engineering @ Vidya Academy
🎓 ML Enthusiast 


---

## ⭐ Show Your Support

* 🌟 Star this repo
* 💌 Share it with friends

---


