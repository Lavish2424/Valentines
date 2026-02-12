import streamlit as st

st.set_page_config(page_title="Be My Valentine?", page_icon="❤️", layout="centered")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #fff0f5, #ffe4e9); }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 style="font-family: Dancing Script, cursive; font-size: clamp(2.8rem, 9vw, 5rem); color: #e11d48; text-align: center; margin: 30px 0;">Will you be my Valentine?</h1>', unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&family=Dancing+Script:wght@700&display=swap');
        
        body {
            margin: 0;
            padding: 15px;
            background: linear-gradient(135deg, #fff0f5, #ffe4e9);
            font-family: 'Poppins', sans-serif;
            text-align: center;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .container {
            position: relative;
            width: min(820px, 92vw);
            height: clamp(400px, 58vh, 520px);
            max-width: 100%;
            margin: 20px auto;
        }
        
        .btn {
            position: absolute;
            padding: 22px 60px;
            font-size: clamp(26px, 6vw, 34px);
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 12px 35px rgba(0,0,0,0.3);
            transition: left 0.4s cubic-bezier(0.68, -0.6, 0.32, 1.6), 
                        top 0.4s cubic-bezier(0.68, -0.6, 0.32, 1.6),
                        transform 0.35s;
            user-select: none;
        }
        
        #yesBtn {
            background: linear-gradient(45deg, #22c55e, #86efac);
            color: white;
            left: 12%;
            top: 42%;
        }
        
        #yesBtn:hover, #yesBtn:active {
            transform: scale(1.2) rotate(8deg);
        }
        
        #noBtn {
            background: linear-gradient(45deg, #ef4444, #f87171);
            color: white;
            right: 12%;
            top: 42%;
        }
        
        .heart {
            position: absolute;
            font-size: 2.3rem;
            animation: floatHeart 8.5s linear infinite;
            opacity: 0.9;
            pointer-events: none;
            z-index: -1;
        }
        
        @keyframes floatHeart {
            0% { transform: translateY(110vh) rotate(0deg); }
            100% { transform: translateY(-150px) rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container" id="container">
        <button id="yesBtn" class="btn" onclick="yesClicked()">YES 💖</button>
        <button id="noBtn" class="btn" onclick="noClicked()">NO 💔</button>
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const container = document.getElementById('container');
        let scale = 1.0;

        function randomPosition() {
            const maxX = container.clientWidth - noBtn.offsetWidth - 40;
            const maxY = container.clientHeight - noBtn.offsetHeight - 60;
            const x = 30 + Math.random() * maxX;
            const y = 40 + Math.random() * maxY;
            
            noBtn.style.left = x + 'px';
            noBtn.style.top = y + 'px';
            noBtn.style.right = 'auto';
            noBtn.style.transform = `scale(${scale})`;
        }

        function shrinkAndMove(extra = 0) {
            if (scale <= 0.28) return;
            scale = Math.max(0.25, scale - 0.07 - extra);
            noBtn.style.transition = 'transform 0.3s, left 0.45s cubic-bezier(0.68, -0.55, 0.27, 1.55), top 0.45s cubic-bezier(0.68, -0.55, 0.27, 1.55)';
            noBtn.style.transform = `scale(${scale})`;
            randomPosition();
        }

        // Constant auto-shrink + move (the main new feature)
        setInterval(() => {
            shrinkAndMove(0.02);   // gentle constant shrinking + movement
        }, 1850);

        // Proximity chase (mouse + touch)
        function handlePointer(clientX, clientY) {
            const rect = noBtn.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            const distance = Math.hypot(clientX - centerX, clientY - centerY);
            
            if (distance < 160) {
                shrinkAndMove(0.09);   // bigger shrink when you get close
            }
        }

        document.addEventListener('mousemove', e => handlePointer(e.clientX, e.clientY));
        document.addEventListener('touchmove', e => {
            if (e.touches.length) handlePointer(e.touches[0].clientX, e.touches[0].clientY);
        });

        noBtn.addEventListener('mouseenter', () => shrinkAndMove(0.08));
        noBtn.addEventListener('touchstart', e => {
            e.preventDefault();
            shrinkAndMove(0.1);
        });

        // Initial position
        setTimeout(() => {
            scale = 1.0;
            randomPosition();
        }, 600);

        function yesClicked() {
            confetti({ particleCount: 230, spread: 100, origin: { y: 0.58 }, colors: ['#ec4899', '#f472b6', '#e11d48', '#22c55e', '#eab308'] });
            confetti({ particleCount: 110, angle: 60, spread: 55, origin: { x: 0 } });
            confetti({ particleCount: 110, angle: 120, spread: 55, origin: { x: 1 } });

            document.body.innerHTML = `
                <div style="margin-top: 22vh; padding: 20px; text-align: center;">
                    <h1 style="font-size: clamp(3.8rem, 13vw, 6.5rem); color: #e11d48;">YES!!! 💕</h1>
                    <p style="font-size: clamp(1.9rem, 6.5vw, 3.2rem); color: #881337; margin: 30px 0;">
                        I knew you'd say yes, my love 🥰<br>
                        You just made my whole year!
                    </p>
                    <p style="font-size: clamp(5rem, 18vw, 8rem); animation: bounce 1.4s infinite;">❤️🌹💖</p>
                </div>
            `;
            setInterval(() => confetti({ particleCount: 75, spread: 100 }), 340);
        }

        function noClicked() {
            alert("💔 Too late... it's running away! 🏃‍♂️");
            shrinkAndMove(0.12);
        }

        // Floating hearts
        function createHeart() {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.textContent = ['❤️','💖','💗','💓'][Math.floor(Math.random()*4)];
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDuration = (Math.random() * 6 + 9) + 's';
            heart.style.fontSize = (Math.random() * 1.7 + 2.1) + 'rem';
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 17500);
        }
        
        setInterval(createHeart, 260);
        for (let i = 0; i < 22; i++) setTimeout(createHeart, i * 130);
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=860)

st.caption("❤️ No button now constantly shrinks + randomly moves! Fully mobile friendly.")
