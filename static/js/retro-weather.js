// Retro Weather Channel JavaScript

// Update current time display
function updateCurrentTime() {
    const now = new Date();
    const options = { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric', 
        hour: '2-digit', 
        minute: '2-digit',
        second: '2-digit'
    };
    const timeString = now.toLocaleDateString('en-US', options);
    const timeElement = document.getElementById('currentTime');
    if (timeElement) {
        timeElement.textContent = timeString.toUpperCase();
    }
    
    // Update time in weather data section
    const updateTimeElement = document.getElementById('updateTime');
    if (updateTimeElement) {
        const shortOptions = {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true
        };
        updateTimeElement.textContent = now.toLocaleTimeString('en-US', shortOptions).toUpperCase();
    }
}

// Initialize time updates
updateCurrentTime();
setInterval(updateCurrentTime, 1000);

// Scrolling alerts ticker enhancement
// The CSS animation handles the scrolling, but we can add dynamic content here
function initializeAlertsTicker() {
    const ticker = document.getElementById('alertsTicker');
    if (!ticker) return;
    
    // Optional: Add dynamic weather alerts if available
    // This could be enhanced to fetch real alerts from an API
    
    // Pause animation on hover for readability
    ticker.addEventListener('mouseenter', function() {
        this.style.animationPlayState = 'paused';
    });
    
    ticker.addEventListener('mouseleave', function() {
        this.style.animationPlayState = 'running';
    });
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initializeAlertsTicker();
    
    // Add smooth scrolling for better UX
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Add entrance animations to detail boxes
    const detailBoxes = document.querySelectorAll('.detail-box');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(20px)';
                
                setTimeout(() => {
                    entry.target.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    detailBoxes.forEach(box => {
        observer.observe(box);
    });
});

// Add retro TV static effect on page load (subtle)
function addRetroEffect() {
    const body = document.body;
    body.style.opacity = '0';
    
    setTimeout(() => {
        body.style.transition = 'opacity 0.5s ease-in';
        body.style.opacity = '1';
    }, 100);
}

// Initialize retro effect
addRetroEffect();
