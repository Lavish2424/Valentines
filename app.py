import streamlit as st

st.set_page_config(page_title="Be My Valentine?", page_icon="❤️", layout="centered")

st.markdown("""
<style>
    .stApp { background: linear-gradient(135deg, #fff0f5, #ffe4e9); }
    .title { font-family: 'Dancing Script', cursive; font-size: clamp(2.8rem, 9vw, 5rem); color: #e11d48; text-align: center; margin: 30px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">Will you be my Valentine?</h1>', unsafe_allow_html=True)

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
        
        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: clamp(2.8rem, 9vw, 5rem);
            color: #e11d48;
            margin: 20px 0 40px;
            text-shadow: 0 4px 15px rgba(225, 29, 72, 0.3);
        }
        
        .container {
            position: relative;
            width: min(800px, 92vw);
            height: 420px;
            max-width: 100%;
        }
        
        .btn {
            position: absolute;
            padding: 22px 65px;
            font-size: clamp(26px, 6vw, 34px);
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 12px 30px rgba(0,0,0,0.25);
            transition: all 0.4s cubic-bezier(0.68, -0.55, 0.27, 1.55);
            user-select: none;
        }
        
        #yesBtn {
            background: linear-gradient(45deg, #22c55e, #86efac);
            color: white;
            left: 12%;
            top: 45%;
        }
        
        #yesBtn:hover, #yesBtn:active {
            transform: scale(1.18) rotate(6deg);
        }
        
        #noBtn {
            background: linear-gradient(45deg, #ef4444, #f87171);
            color: white;
            right: 12%;
            top: 45%;
        }
        
        @media (max-width: 640px) {
            .container { height: 480px; }
            #yesBtn, #noBtn {
                left: 50% !important;
                transform: translateX(-50%);
                width: 82%;
                max-width: 340px;
            }
            #yesBtn { top: 28%; }
            #noBtn { top: 58%; }
        }
        
        .heart {
            position: absolute;
            font-size: 2.4rem;
            animation: float 9s linear infinite;
            opacity: 0.85;
            pointer-events: none;
            z-index: -1;
        }
        
        @keyframes float {
            0% { transform: translateY(110vh) rotate(0deg); }
            100% { transform: translateY(-140px) rotate(380deg); }
        }
    </style>
</head>
<body>
    <h1>Will you be my Valentine?</h1>
    <div class="container">
        <button id="yesBtn" class="btn" onclick="yesClicked()">YES 💖</button>
        <button id="noBtn" class="btn" onclick="noClicked()">NO 💔</button>
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        let scale = 1.0;

        function shrinkNo() {
            if (scale <= 0.35) return;
            scale = Math.max(0.32, scale - 0.085);
            noBtn.style.transform = `scale(${scale})`;
            
            // Gentle wobble when shrinking
            noBtn.style.transition = 'transform 0.35s';
            setTimeout(() => {
                noBtn.style.transition = 'all 0.4s cubic-bezier(0.68, -0.55, 0.27, 1.55)';
            }, 400);
        }

        function handlePointer(clientX, clientY) {
            const rect = noBtn.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            const distance = Math.hypot(clientX - centerX, clientY - centerY);
            
            if (distance < 155 && scale > 0.35) {
                shrinkNo();
            }
        }

        // Mouse + Touch support
        document.addEventListener('mousemove', e => handlePointer(e.clientX, e.clientY));
        document.addEventListener('touchmove', e => {
            if (e.touches.length) handlePointer(e.touches[0].clientX, e.touches[0].clientY);
        });

        noBtn.addEventListener('mouseenter', shrinkNo);
        noBtn.addEventListener('touchstart', e => {
            e.preventDefault();
            shrinkNo();
        });

        function yesClicked() {
            confetti({ particleCount: 240, spread: 100, origin: { y: 0.6 }, colors: ['#ec4899','#f472b6','#e11d48','#22c55e'] });
            confetti({ particleCount: 100, angle: 60, origin: { x: 0 } });
            confetti({ particleCount: 100, angle: 120, origin: { x: 1 } });

            document.body.innerHTML = `
                <div style="margin-top: 22vh; padding: 20px; text-align: center;">
                    <h1 style="font-size: clamp(3.8rem, 13vw, 6.5rem); color: #e11d48;">YES!!! 💕</h1>
                    <p style="font-size: clamp(1.9rem, 6.5vw, 3.2rem); color: #881337; margin: 25px 0;">
                        I knew you'd say yes, my love 🥰<br>
                        You just made me the happiest person alive!
                    </p>
                    <p style="font-size: clamp(5rem, 18vw, 8rem); animation: bounce 1.4s infinite;">❤️🌹💖</p>
                </div>
            `;
            
            setInterval(() => confetti({ particleCount: 80, spread: 110 }), 380);
        }

        function noClicked() {
            alert("💔 Ouch... but this button is getting smaller for a reason 😉");
            shrinkNo();
            shrinkNo(); // extra shrink on click
        }

        // Floating hearts
        function createHeart() {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.textContent = '❤️';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDuration = (Math.random() * 7 + 8) + 's';
            heart.style.fontSize = (Math.random() * 1.8 + 2.2) + 'rem';
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 18000);
        }
        
        setInterval(createHeart, 240);
        for (let i = 0; i < 20; i++) setTimeout(createHeart, i * 140);
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=820)

st.caption("❤️ New shrinking No button version — fully mobile friendly!")
