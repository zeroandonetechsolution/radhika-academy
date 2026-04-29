document.addEventListener('DOMContentLoaded', () => {
    // Register ScrollTrigger
    gsap.registerPlugin(ScrollTrigger);

    // Initial load animations
    gsap.to(".hero-content.gsap-reveal, .page-header.gsap-reveal", {
        y: 0,
        opacity: 1,
        duration: 1.2,
        ease: "power3.out",
        delay: 0.2
    });

    // Universal scroll animations for all other .gsap-reveal elements
    gsap.utils.toArray('.gsap-reveal:not(.hero-content):not(.page-header)').forEach((element) => {
        gsap.to(element, {
            scrollTrigger: {
                trigger: element,
                start: "top 85%",
                toggleActions: "play none none reverse"
            },
            y: 0,
            opacity: 1,
            duration: 0.8,
            ease: "power3.out"
        });
    });

    // Navbar scroll effect
    const nav = document.querySelector('nav');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.style.padding = '10px 50px';
            nav.style.background = 'rgba(255, 255, 255, 0.9)';
            nav.style.boxShadow = '0 5px 20px rgba(0,0,0,0.05)';
        } else {
            nav.style.padding = '20px 50px';
            nav.style.background = 'var(--glass-bg)';
            nav.style.boxShadow = 'none';
        }
    });

    // Elegant Background Particle Animation
    const canvas = document.getElementById('bg-canvas');
    if (canvas) {
        const ctx = canvas.getContext('2d');
        let width, height, particles;

        function initCanvas() {
            width = canvas.width = window.innerWidth;
            height = canvas.height = window.innerHeight;
            particles = [];
            const particleCount = window.innerWidth < 768 ? 30 : 80;
            
            for (let i = 0; i < particleCount; i++) {
                particles.push({
                    x: Math.random() * width,
                    y: Math.random() * height,
                    radius: Math.random() * 3 + 1,
                    dx: (Math.random() - 0.5) * 0.8,
                    dy: (Math.random() - 0.5) * 0.8,
                    opacity: Math.random() * 0.5 + 0.1,
                    color: Math.random() > 0.5 ? '212, 175, 55' : '255, 107, 129' // Gold or Soft Pink
                });
            }
        }

        function drawParticles() {
            ctx.clearRect(0, 0, width, height);
            particles.forEach(p => {
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(${p.color}, ${p.opacity})`;
                ctx.fill();

                p.x += p.dx;
                p.y += p.dy;

                if (p.x < 0) p.x = width;
                if (p.x > width) p.x = 0;
                if (p.y < 0) p.y = height;
                if (p.y > height) p.y = 0;
            });
            requestAnimationFrame(drawParticles);
        }

        initCanvas();
        drawParticles();
        window.addEventListener('resize', initCanvas);
    }
});
