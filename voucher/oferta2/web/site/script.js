

document.addEventListener('DOMContentLoaded', () => {
    const slider = document.querySelector('.slider');
    const container = document.querySelector('.slider_container');
    const slides = document.querySelectorAll('.slider_content');
    const buttons = document.querySelectorAll('.slider_button');
    let currentIndex = 0;
    
    buttons[currentIndex].classList.add('active');

    let intervalID = setInterval(() => {
        goToSlide(currentIndex + 1 >= slides.length ? 0 : currentIndex + 1)
    }, 5 * 1000)


    buttons.forEach((button, index) => {
        button.addEventListener('click', () => {
            goToSlide(index);
            clearInterval(intervalID)
            intervalID = setInterval(() => {
                goToSlide(currentIndex + 1 >= slides.length ? 0 : currentIndex + 1)
            }, 5 * 1000)
        });
    });

    function goToSlide(index) {
        if (index < 0 || index >= slides.length) return;
        
        const slideWidth = slider.offsetWidth;
        container.style.transform = `translateX(-${index * slideWidth}px)`;
        
        buttons[currentIndex].classList.remove('active');
        currentIndex = index;
        buttons[currentIndex].classList.add('active');
    }

    
    window.addEventListener('resize', () => {
        container.style.transform = `translateX(-${currentIndex * slider.offsetWidth}px)`;
    });

    
});