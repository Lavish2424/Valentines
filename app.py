import streamlit as st

st.set_page_config(
    page_title="Be My Valentine? 💕",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #ffe4e1, #ffc0cb);
    }
</style>
""", unsafe_allow_html=True)

st.title("❤️ Will you be my Valentine? ❤️")

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
            padding: 20px 10px;
            background: linear-gradient(135deg, #ffe4e1, #ffc0cb);
            font-family: 'Poppins', sans-serif;
            text-align: center;
            overflow: hidden;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        h1 {
            font-family: 'Dancing Script', cursive;
            font-size: clamp(2.8rem, 9vw, 4.8rem);
            color: #e11d48;
            margin: 20px 0 30px;
            text-shadow: 0 4px 20px rgba(225, 29, 72, 0.4);
        }
        
        .container {
            position: relative;
            width: min(820px, 92vw);
            height: clamp(380px, 55vh, 460px);
            max-width: 100%;
            margin: 0 auto;
        }
        
        .btn {
            position: absolute;
            padding: 22px 55px;
            font-size: clamp(26px, 5.5vw, 32px);
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            transition: all 0.3s;
            user-select: none;
            touch-action: none;
        }
        
        #yesBtn {
            background: linear-gradient(45deg, #22c55e, #86efac);
            color: white;
            left: 8%;
            top: 48%;
            transform: translateY(-50%);
        }
        
        #yesBtn:hover, #yesBtn:active {
            transform: translateY(-50%) scale(1.15) rotate(8deg);
        }
        
        #noBtn {
            background: linear-gradient(45deg, #ef4444, #f87171);
            color: white;
            right: 8%;
            top: 48%;
            transform: translateY(-50%);
        }
        
        /* Mobile stacking */
        @media (max-width: 640px) {
            .container {
                height: clamp(420px, 62vh, 520px);
            }
            #yesBtn {
                left: 50% !important;
                top: 28% !important;
                transform: translate(-50%, -50%) !important;
                width: 78%;
                max-width: 320px;
            }
            #noBtn {
                left: 50% !important;
                top: 58% !important;
                transform: translate(-50%, -50%) !important;
                width: 78%;
                max-width: 320px;
            }
        }
        
        .heart {
            position: absolute;
            font-size: 2.2rem;
            animation: floatHeart 8s linear infinite;
            opacity: 0.9;
            pointer-events: none;
            z-index: -1;
        }
        
        @keyframes floatHeart {
            0% { transform: translateY(110vh) rotate(0deg); }
            100% { transform: translateY(-120px) rotate(360deg); }
        }
    </style>
</head>
<body>
    <h1>Will you be my Valentine?</h1>
    <div class="container" id="container">
        <button id="yesBtn" class="btn" onclick="yesClicked()">YES 💖</button>
        <button id="noBtn" class="btn" onclick="noClicked()">NO 🏃‍♂️</button>
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const container = document.getElementById('container');

        function moveNoButton() {
            const maxX = container.clientWidth - noBtn.offsetWidth - 30;
            const maxY = container.clientHeight - noBtn.offsetHeight - 40;
            let x = Math.random() * maxX;
            let y = 40 + Math.random() * (maxY - 80);
            
            // Bouncy running escape
            noBtn.style.transition = 'left 0.25s cubic-bezier(0.68, -0.6, 0.32, 1.6), top 0.25s cubic-bezier(0.68, -0.6, 0.32, 1.6)';
            noBtn.style.left = x + 'px';
            noBtn.style.top = y + 'px';
            noBtn.style.right = 'auto';
            
            // Extra running feel
            noBtn.style.transform = `translateY(-50%) rotate(${Math.random() * 14 - 7}deg)`;
            setTimeout(() => {
                noBtn.style.transform = 'translateY(-50%)';
            }, 280);
        }

        // Shared pointer handler for mouse + touch
        function handlePointerMove(clientX, clientY) {
            const rect = noBtn.getBoundingClientRect();
            const btnCenterX = rect.left + rect.width / 2;
            const btnCenterY = rect.top + rect.height / 2;
            const distance = Math.hypot(clientX - btnCenterX, clientY - btnCenterY);
            
            if (distance < 165) {
                moveNoButton();
            }
        }

        // Desktop mouse
        document.addEventListener('mousemove', (e) => {
            handlePointerMove(e.clientX, e.clientY);
        });

        // Mobile touch
        document.addEventListener('touchmove', (e) => {
            if (e.touches.length > 0) {
                const touch = e.touches[0];
                handlePointerMove(touch.clientX, touch.clientY);
            }
        });

        // Hover / tap also triggers escape
        noBtn.addEventListener('mouseenter', moveNoButton);
        noBtn.addEventListener('touchstart', (e) => {
            e.preventDefault();
            moveNoButton();
        });

        // Start with a little movement
        setTimeout(moveNoButton, 800);

        function yesClicked() {
            confetti({
                particleCount: 220,
                spread: 100,
                origin: { y: 0.6 },
                colors: ['#ec4899', '#f472b6', '#e11d48', '#22c55e', '#eab308']
            });
            confetti({ particleCount: 90, angle: 55, spread: 60, origin: { x: 0 } });
            confetti({ particleCount: 90, angle: 125, spread: 60, origin: { x: 1 } });

            document.body.innerHTML = `
                <div style="margin-top: 20vh; text-align: center; padding: 20px;">
                    <h1 style="font-size: clamp(3.5rem, 12vw, 6rem); color: #e11d48;">YES!!! 💕</h1>
                    <p style="font-size: clamp(1.8rem, 6vw, 3rem); margin: 30px 0; color: #881337;">
                        I knew you'd say yes, my love 🥰<br>
                        You're my favorite person in the whole world!
                    </p>
                    <p style="font-size: clamp(4rem, 15vw, 7rem); animation: bounce 1.3s infinite;">❤️🌹💖</p>
                </div>
            `;

            setInterval(() => confetti({ particleCount: 70, spread: 90 }), 320);
        }

        function noClicked() {
            alert("😭 Haha nice try... but no is not an option today! 🏃‍♂️");
            moveNoButton();
        }

        // Floating hearts
        function createHeart() {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.textContent = ['❤️','💖','💗','💓','💘'][Math.floor(Math.random()*5)];
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.animationDuration = (Math.random() * 6 + 9) + 's';
            heart.style.fontSize = (Math.random() * 1.6 + 2) + 'rem';
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 17000);
        }

        setInterval(createHeart, 260);
        for (let i = 0; i < 18; i++) setTimeout(createHeart, i * 160);
    </script>
</body>
</html>
"""

st.components.v1.html(html_code, height=820)

st.caption("❤️ Mobile-friendly + running No button! Open this on your phone and hand it to her.")
