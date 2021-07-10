let mainSlider = {
    container: document.getElementById('mainSlider-container'),
    containerName: 'slider',
    list: document.getElementById('mainSlider-list'),
    items: document.getElementsByClassName('slider__slide'),
    shortList: document.getElementById('mainSlider-shortList'),
    shortListItems: document.getElementsByClassName('slider__short-list-item'),
    leftButton: document.getElementById('mainSlider-buttonLeft'),
    rightButton: document.getElementById('mainSlider-buttonRight')
}

let servicesSlider = {
    container: document.getElementById('servicesSlider-container'),
    containerName: 'services',
    list: document.getElementById('servicesSlider-list'),
    items: document.getElementsByClassName('services__slider-item'),
    shortList: document.getElementById('servicesSlider-shortList'),
    shortListItems: document.getElementsByClassName('services__short-list-item'),
    leftButton: document.getElementById('servicesSlider-buttonLeft'),
    rightButton: document.getElementById('servicesSlider-buttonRight')
}

let doctorsSlider = {
    container: document.getElementById('doctorsSlider-container'),
    containerName: 'doctors',
    list: document.getElementById('doctorsSlider-list'),
    items: document.getElementsByClassName('doctors__slider-item'),
    shortList: document.getElementById('doctorsSlider-shortList'),
    shortListItems: document.getElementsByClassName('doctors__short-list-item'),
}

let reviewsSlider = {
    container: document.getElementById('reviewsSlider-container'),
    containerName: 'reviews',
    list: document.getElementById('reviewsSlider-list'),
    items: document.getElementsByClassName('reviews__slider-item'),
    shortList: document.getElementById('reviewsSlider-shortList'),
    shortListItems: document.getElementsByClassName('reviews__short-list-item'),
}

createSlider(mainSlider);
createSlider(servicesSlider);
createSlider(doctorsSlider);
createSlider(reviewsSlider);
