// Analysis functionality for Alto Car Manual

let selectedImageFile = null;
let selectedVideoFile = null;

// Image handling
function handleImageSelect(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    // Validate file type
    const validTypes = ['image/png', 'image/jpeg', 'image/jpg', 'image/gif'];
    if (!validTypes.includes(file.type)) {
        showError('Please select a valid image file (PNG, JPG, JPEG, or GIF)');
        return;
    }
    
    // Validate file size (16MB)
    if (file.size > 16 * 1024 * 1024) {
        showError('File size must be less than 16MB');
        return;
    }
    
    selectedImageFile = file;
    
    // Show preview
    const reader = new FileReader();
    reader.onload = function(e) {
        document.getElementById('preview-img').src = e.target.result;
        document.getElementById('image-preview').style.display = 'block';
        document.getElementById('image-upload-area').style.display = 'none';
        document.getElementById('analyze-image-btn').style.display = 'block';
    };
    reader.readAsDataURL(file);
    
    hideError();
}

function clearImage() {
    selectedImageFile = null;
    document.getElementById('image-input').value = '';
    document.getElementById('preview-img').src = '';
    document.getElementById('image-preview').style.display = 'none';
    document.getElementById('image-upload-area').style.display = 'block';
    document.getElementById('analyze-image-btn').style.display = 'none';
    hideResults();
    hideError();
}

function analyzeImage() {
    if (!selectedImageFile) {
        showError('Please select an image first');
        return;
    }
    
    showLoading();
    
    const formData = new FormData();
    formData.append('file', selectedImageFile);
    formData.append('type', 'image');
    
    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        hideLoading();
        
        if (data.success) {
            displayResults(data);
        } else {
            showError(formatError(data));
        }
    })
    .catch(error => {
        hideLoading();
        showError('Network error. Please check your connection and try again.');
        console.error('Error:', error);
    });
}

// Video handling
function handleVideoSelect(event) {
    const file = event.target.files[0];
    if (!file) return;
    
    // Validate file type
    const validTypes = ['video/mp4', 'video/avi', 'video/quicktime', 'video/x-msvideo'];
    if (!validTypes.includes(file.type)) {
        showError('Please select a valid video file (MP4, AVI, or MOV)');
        return;
    }
    
    // Validate file size (16MB)
    if (file.size > 16 * 1024 * 1024) {
        showError('File size must be less than 16MB');
        return;
    }
    
    selectedVideoFile = file;
    
    // Show preview
    const reader = new FileReader();
    reader.onload = function(e) {
        const videoElement = document.getElementById('preview-video');
        videoElement.src = e.target.result;
        document.getElementById('video-preview').style.display = 'block';
        document.getElementById('video-upload-area').style.display = 'none';
        document.getElementById('analyze-video-btn').style.display = 'block';
    };
    reader.readAsDataURL(file);
    
    hideError();
}

function clearVideo() {
    selectedVideoFile = null;
    document.getElementById('video-input').value = '';
    document.getElementById('preview-video').src = '';
    document.getElementById('video-preview').style.display = 'none';
    document.getElementById('video-upload-area').style.display = 'block';
    document.getElementById('analyze-video-btn').style.display = 'none';
    hideResults();
    hideError();
}

function analyzeVideo() {
    if (!selectedVideoFile) {
        showError('Please select a video first');
        return;
    }
    
    showLoading();
    
    const formData = new FormData();
    formData.append('file', selectedVideoFile);
    formData.append('type', 'video');
    
    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        hideLoading();
        
        if (data.success) {
            displayResults(data);
        } else {
            showError(formatError(data));
        }
    })
    .catch(error => {
        hideLoading();
        showError('Network error. Please check your connection and try again.');
        console.error('Error:', error);
    });
}

// Text query handling
function analyzeText() {
    const query = document.getElementById('text-query').value.trim();
    
    if (!query) {
        showError('Please enter a question or describe your problem');
        return;
    }
    
    if (query.length < 10) {
        showError('Please provide more details (at least 10 characters)');
        return;
    }
    
    showLoading();
    
    const formData = new FormData();
    formData.append('query', query);
    formData.append('type', 'text');
    
    fetch('/analyze', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        hideLoading();
        
        if (data.success) {
            displayResults(data);
        } else {
            showError(formatError(data));
        }
    })
    .catch(error => {
        hideLoading();
        showError('Network error. Please check your connection and try again.');
        console.error('Error:', error);
    });
}

// Drag and drop support for image upload
const imageUploadArea = document.getElementById('image-upload-area');
if (imageUploadArea) {
    imageUploadArea.addEventListener('dragover', function(e) {
        e.preventDefault();
        this.style.borderColor = '#3498db';
        this.style.background = '#e3f2fd';
    });
    
    imageUploadArea.addEventListener('dragleave', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
        this.style.background = '#fafafa';
    });
    
    imageUploadArea.addEventListener('drop', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
        this.style.background = '#fafafa';
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            const imageInput = document.getElementById('image-input');
            imageInput.files = files;
            handleImageSelect({ target: imageInput });
        }
    });
}

// Drag and drop support for video upload
const videoUploadArea = document.getElementById('video-upload-area');
if (videoUploadArea) {
    videoUploadArea.addEventListener('dragover', function(e) {
        e.preventDefault();
        this.style.borderColor = '#3498db';
        this.style.background = '#e3f2fd';
    });
    
    videoUploadArea.addEventListener('dragleave', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
        this.style.background = '#fafafa';
    });
    
    videoUploadArea.addEventListener('drop', function(e) {
        e.preventDefault();
        this.style.borderColor = '#ddd';
        this.style.background = '#fafafa';
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            const videoInput = document.getElementById('video-input');
            videoInput.files = files;
            handleVideoSelect({ target: videoInput });
        }
    });
}

// Enter key support for text query
const textQueryInput = document.getElementById('text-query');
if (textQueryInput) {
    textQueryInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            analyzeText();
        }
    });
}
