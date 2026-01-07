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
    
    // Add entrance animations to detail boxes
    const detailBoxes = document.querySelectorAll('.detail-box');
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
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
