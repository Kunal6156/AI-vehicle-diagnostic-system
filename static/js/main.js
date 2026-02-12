// Main JavaScript for Alto Car Manual

// Tab switching functionality
function switchTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    const tabButtons = document.querySelectorAll('.tab-btn');
    tabButtons.forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    const selectedTab = document.getElementById(`${tabName}-tab`);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }
    
    // Activate corresponding button
    const clickedButton = event.target;
    clickedButton.classList.add('active');
    
    // Hide results and errors when switching tabs
    hideResults();
    hideError();
}

// Utility functions
function showLoading() {
    document.getElementById('loading').style.display = 'block';
    hideResults();
    hideError();
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

function showResults() {
    document.getElementById('results').style.display = 'block';
    // Scroll to results
    document.getElementById('results').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideResults() {
    document.getElementById('results').style.display = 'none';
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    // Scroll to error
    errorDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideError() {
    document.getElementById('error').style.display = 'none';
}

// Display analysis results
function displayResults(data) {
    // Display analysis text
    const analysisDiv = document.getElementById('analysis-text');
    analysisDiv.textContent = data.analysis || 'No analysis available';
    
    // Display videos
    const videosContainer = document.getElementById('videos-container');
    videosContainer.innerHTML = '';
    
    if (data.videos && data.videos.length > 0) {
        data.videos.forEach(video => {
            const videoCard = createVideoCard(video);
            videosContainer.appendChild(videoCard);
        });
    } else {
        videosContainer.innerHTML = '<p style="color: #666;">No related videos found. Try a different query.</p>';
    }
    
    showResults();
}

// Create video card element
function createVideoCard(video) {
    const card = document.createElement('div');
    card.className = 'video-card';
    
    card.innerHTML = `
        <img src="${video.thumbnail}" alt="${video.title}" class="video-thumbnail">
        <div class="video-info">
            <div class="video-title">${video.title}</div>
            <div class="video-channel">${video.channel}</div>
            <a href="${video.url}" target="_blank" class="video-link">Watch on YouTube →</a>
        </div>
    `;
    
    return card;
}

// Format error message
function formatError(error) {
    if (typeof error === 'string') {
        return error;
    }
    
    if (error.error) {
        return error.error;
    }
    
    return 'An unexpected error occurred. Please try again.';
}

// Initialize page
document.addEventListener('DOMContentLoaded', function() {
    console.log('Alto Car Digital Manual loaded');
    
    // Check if API is configured
    fetch('/health')
        .then(response => response.json())
        .then(data => {
            if (!data.services.gemini || !data.services.youtube) {
                console.warn('API keys not fully configured');
            }
        })
        .catch(error => {
            console.error('Health check failed:', error);
        });
});

// Smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});
