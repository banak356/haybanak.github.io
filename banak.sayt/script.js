// Պարզ անիմացիա վերևից դեպի ներքև երևալու համար
document.addEventListener('DOMContentLoaded', () => {
    const elements = document.querySelectorAll('.fade-in');
    elements.forEach((el) => {
        el.style.opacity = 0;
        el.style.transition = 'opacity 2s';
        el.style.opacity = 1;
    });
});
