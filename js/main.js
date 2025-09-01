// Main JavaScript for SPLOVE
document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all components
    initHeader();
    initFeaturedModels();
    initStories();
    initModelCards();
    initSearch();
    initFilters();
    
    // Header functionality
    function initHeader() {
        const searchBtn = document.getElementById('search-btn');
        const loginBtn = document.getElementById('login-btn');
        
        // Search button functionality
        if (searchBtn) {
            searchBtn.addEventListener('click', function() {
                // TODO: Implement search modal
                console.log('Search clicked');
            });
        }
        
        // Login button functionality
        if (loginBtn) {
            loginBtn.addEventListener('click', function() {
                // TODO: Implement login modal
                console.log('Login clicked');
            });
        }
    }
    
    // Featured models carousel functionality
    function initFeaturedModels() {
        const featuredContainer = document.querySelector('.featured-container');
        const prevBtn = document.querySelector('.featured-nav .prev-btn');
        const nextBtn = document.querySelector('.featured-nav .next-btn');
        
        if (featuredContainer && prevBtn && nextBtn) {
            const scrollAmount = 220;
            
            // Next button
            nextBtn.addEventListener('click', function() {
                featuredContainer.scrollBy({
                    left: scrollAmount,
                    behavior: 'smooth'
                });
            });
            
            // Previous button
            prevBtn.addEventListener('click', function() {
                featuredContainer.scrollBy({
                    left: -scrollAmount,
                    behavior: 'smooth'
                });
            });
            
            // Featured cards click functionality
            const featuredCards = document.querySelectorAll('.featured-card');
            featuredCards.forEach(card => {
                card.addEventListener('click', function() {
                    const modelName = this.querySelector('.featured-name').textContent;
                    openModelProfile(modelName);
                });
            });
        }
    }
    
    // Stories carousel functionality
    function initStories() {
        const storiesContainer = document.querySelector('.stories-container');
        const prevBtn = document.querySelector('.prev-btn');
        const nextBtn = document.querySelector('.next-btn');
        
        if (storiesContainer && prevBtn && nextBtn) {
            const scrollAmount = 200;
            
            // Next button
            nextBtn.addEventListener('click', function() {
                storiesContainer.scrollBy({
                    left: scrollAmount,
                    behavior: 'smooth'
                });
            });
            
            // Previous button
            prevBtn.addEventListener('click', function() {
                storiesContainer.scrollBy({
                    left: -scrollAmount,
                    behavior: 'smooth'
                });
            });
            
            // Story item click functionality
            const storyItems = document.querySelectorAll('.story-item');
            storyItems.forEach(item => {
                item.addEventListener('click', function() {
                    // TODO: Implement story view modal
                    console.log('Story clicked:', this.querySelector('img').alt);
                });
            });
        }
    }
    
    // Model cards functionality
    function initModelCards() {
        const modelCards = document.querySelectorAll('.model-card');
        const featuredCards = document.querySelectorAll('.featured-card');
        
        // Featured cards click
        featuredCards.forEach(card => {
            card.addEventListener('click', function() {
                const modelName = this.querySelector('.featured-name').textContent;
                openModelProfile(modelName);
            });
        });
        
        // Model cards click
        modelCards.forEach(card => {
            card.addEventListener('click', function() {
                const modelName = this.querySelector('.model-name').textContent;
                openModelProfile(modelName);
            });
        });
    }
    
    // Open model profile (placeholder)
    function openModelProfile(modelName) {
        // TODO: Implement model profile page/modal
        console.log('Opening profile for:', modelName);
        
        // For now, create a simple alert
        // In the future, this could open a modal or navigate to a profile page
        alert(`Perfil de ${modelName} - Em desenvolvimento`);
    }
    
    // Search functionality
    function initSearch() {
        // TODO: Implement search functionality
        // This could include:
        // - Search modal
        // - Live search results
        // - Search filters
        console.log('Search functionality initialized');
    }
    
    // Filter functionality
    function initFilters() {
        // TODO: Implement filter functionality
        // This could include:
        // - Filter modal
        // - Category filters
        // - Location filters
        // - Price filters
        console.log('Filter functionality initialized');
    }
    
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
    
    // Lazy loading for images
    function initLazyLoading() {
        const images = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        images.forEach(img => imageObserver.observe(img));
    }
    
    // Initialize lazy loading
    initLazyLoading();
    
    // Add loading states
    function addLoadingStates() {
        const cards = document.querySelectorAll('.model-card, .featured-card');
        
        cards.forEach(card => {
            card.addEventListener('click', function() {
                this.style.opacity = '0.7';
                this.style.pointerEvents = 'none';
                
                // Reset after a short delay
                setTimeout(() => {
                    this.style.opacity = '1';
                    this.style.pointerEvents = 'auto';
                }, 300);
            });
        });
    }
    
    // Initialize loading states
    addLoadingStates();
    
    // Add keyboard navigation
    function initKeyboardNavigation() {
        document.addEventListener('keydown', function(e) {
            // ESC key to close modals (when implemented)
            if (e.key === 'Escape') {
                // TODO: Close any open modals
                console.log('ESC pressed - close modals');
            }
            
            // Enter key on focused elements
            if (e.key === 'Enter') {
                const focusedElement = document.activeElement;
                if (focusedElement && focusedElement.classList.contains('model-card')) {
                    focusedElement.click();
                }
            }
        });
    }
    
    // Initialize keyboard navigation
    initKeyboardNavigation();
    
    // Add touch gestures for mobile
    function initTouchGestures() {
        let startX = 0;
        let startY = 0;
        
        document.addEventListener('touchstart', function(e) {
            startX = e.touches[0].clientX;
            startY = e.touches[0].clientY;
        });
        
        document.addEventListener('touchend', function(e) {
            if (!startX || !startY) return;
            
            const endX = e.changedTouches[0].clientX;
            const endY = e.changedTouches[0].clientY;
            
            const diffX = startX - endX;
            const diffY = startY - endY;
            
            // Swipe left/right for stories
            if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 50) {
                const storiesContainer = document.querySelector('.stories-container');
                if (storiesContainer) {
                    const scrollAmount = diffX > 0 ? 200 : -200;
                    storiesContainer.scrollBy({
                        left: scrollAmount,
                        behavior: 'smooth'
                    });
                }
            }
            
            startX = 0;
            startY = 0;
        });
    }
    
    // Initialize touch gestures
    initTouchGestures();
    
    // Performance optimization: Debounce scroll events
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
    
    // Add scroll effects
    const handleScroll = debounce(function() {
        const scrolled = window.pageYOffset;
        const header = document.querySelector('.header');
        
        if (scrolled > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    }, 10);
    
    window.addEventListener('scroll', handleScroll);
    
    // Console log for debugging
    console.log('SPLOVE website initialized successfully');
});

// Utility functions
const SPLOVE = {
    // Show notification
    showNotification: function(message, type = 'info') {
        // TODO: Implement notification system
        console.log(`${type.toUpperCase()}: ${message}`);
    },
    
    // Format currency
    formatCurrency: function(amount) {
        return new Intl.NumberFormat('pt-BR', {
            style: 'currency',
            currency: 'BRL'
        }).format(amount);
    },
    
    // Validate email
    validateEmail: function(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    },
    
    // Get URL parameters
    getUrlParameter: function(name) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(name);
    }
};
