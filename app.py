import streamlit as st

st.set_page_config(
    page_title="Be My Valentine? 💕",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cute background
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #ffe4e1, #ffc0cb);
    }
</style>
""", unsafe_allow_html=True)

st.title("❤️ Will you be my Valentine? ❤️")

# Optional: Add her photo here (replace the URL or use a local file)
# st.image("https://your-photo-link.jpg", width=300)

st.markdown("### (Hover over the No button... I dare you 😏)")

# The fun interactive part
html_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&family=Dancing+Script:wght@700&display=swap');
        
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #ffe4e1, #ffc0cb);
            font-family: 'Poppins', sans-serif;
            text-align: center;
            overflow: hidden;
            height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        
        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: 4.8rem;
            color: #e11d48;
            margin-bottom: 2rem;
            text-shadow: 0 4px 20px rgba(225, 29, 72, 0.4);
        }
        
        .container {
            position: relative;
            width: 820px;
            height: 420px;
        }
        
        .btn {
            position: absolute;
            padding: 20px 60px;
            font-size: 32px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 10px 25px rgba(0,0,0,0.25);
            transition: all 0.3s;
        }
        
        #yesBtn {
            background: linear-gradient(45deg, #22c55e, #86efac);
            color: white;
            left: 100px;
            top: 160px;
        }
        
        #yesBtn:hover {
            transform: scale(1.2) rotate(8deg);
        }
        
        #noBtn {
            background: linear-gradient(45deg, #ef4444, #f87171);
            color: white;
            right: 100px;
            top: 160px;
        }
        
        .heart {
            position: absolute;
            font-size: 2.2rem;
            animation: floatHeart 7s linear infinite;
            opacity: 0.85;
            pointer-events: none;
        }
        
        @keyframes floatHeart {
            0% { transform: translateY(100vh) rotate(0deg); }
            100% { transform: translateY(-150px) rotate(360deg); }
        }
    </style>
</head>
<body>
    <h1>Will you be my Valentine?</h1>
    <div class="container" id="container">
        <button id="yesBtn" class="btn" onclick="yesClicked()">YES 💖</button>
        <button id="noBtn" class="btn" onclick="noClicked()">NO 😢</button>
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const container = document.getElementById('container');

        function moveNoButton() {
            const maxX = container.clientWidth - noBtn.offsetWidth - 50;
            const maxY = container.clientHeight - noBtn.offsetHeight - 50;
            const x = Math.random() * maxX;
            const y = 60 + Math.random() * (maxY - 60);
            
            noBtn.style.transition = 'left 0.35s ease-out, top 0.35s ease-out';
            noBtn.style.left = x + 'px';
            noBtn.style.top = y + 'px';
            noBtn.style.right = 'auto';
        }

        // Mouse gets close → button runs away
        document.addEventListener('mousemove', (e) => {
            const rect = noBtn.getBoundingClientRect();
            const btnCenterX = rect.left + rect.width / 2;
            const btnCenterY = rect.top + rect.height / 2;
            const distance = Math.hypot(e.clientX - btnCenterX, e.clientY - btnCenterY);
            
            if (distance < 170) {
                moveNoButton();
            }
        });

        // Hover = instant escape
        noBtn.addEventListener('mouseenter', moveNoButton);

        // Initial movement
        setTimeout(moveNoButton, 700);

        function yesClicked() {
            // Big confetti celebration
            confetti({
                particleCount: 200,
                spread: 90,
                origin: { y: 0.55 },
                colors: ['#ec4899', '#f472b6', '#e11d48', '#22c55e']
            });
            
            // Side cannons
            confetti({ particleCount: 80, angle: 60, spread: 50, origin: { x: 0 } });
            confetti({ particleCount: 80, angle: 120, spread: 50, origin: { x: 1 } });

            // Replace screen with love message
            document.body.innerHTML = `
                <div style="margin-top: 18vh; text-align: center;">
                    <h1 style="font-size: 6rem; color: #e11d48;">YES!!! 💕</h1>
                    <p style="font-size: 3rem; margin: 30px 0; color: #881337;">
                        I knew you'd say yes, my love 🥰<br>
                        You're my favorite person in the whole world!
                    </p>
                    <p style="font-size: 7rem; animation: bounce 1.2s infinite;">❤️🌹💖</p>
                </div>
            `;

            // Keep the confetti going
            setInterval(() => {
                confetti({ particleCount: 60, spread: 100 });
            }, 350);
        }

        function noClicked() {
            alert("😭 Nice try... but I'm not accepting no today! 💪");
            moveNoButton();
        }

        // Floating hearts in background
        function createHeart() {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.textContent = ['❤️','💖','💗','💓','💘'][Math.floor(Math.random()*5)];
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDuration = (Math.random() * 5 + 8) + 's';
            heart.style.fontSize = (Math.random() * 1.4 + 1.8) + 'rem';
            document.body.appendChild(heart);
            
            setTimeout(() => heart.remove(), 16000);
        }

        setInterval(createHeart, 280);
        for (let i = 0; i < 15; i++) setTimeout(createHeart, i * 180);
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=720)

st.caption("Made with love ❤️ Run this locally with `streamlit run app.py` and show her on your laptop!")
