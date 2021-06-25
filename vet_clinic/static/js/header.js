let trigram = document.getElementById('trigram'),
    header = document.getElementById('header'),
    bodyShadow = document.createElement('div');

let wrapper = document.getElementsByClassName('wrapper')[0];

bodyShadow.classList.add('body-shadow');
bodyShadow.id = 'body-shadow';

wrapper.appendChild(bodyShadow);

bodyShadow = document.getElementById('body-shadow');

trigram.addEventListener('click', () => {
    trigram.classList.toggle('open');
    document.getElementsByClassName('header')[0].classList.toggle('open');
    bodyShadow.classList.toggle('active');
});

addEventListener('resize', () => {
    if (document.body.offsetWidth >= 1100) {
        if (bodyShadow.classList.contains('active')) {
            bodyShadow.classList.remove('active');
        }
    } else {
        if (trigram.classList.contains('open')) {
            bodyShadow.classList.add('active');
        }
    }
});