let mainSlider = {
    container: document.getElementById('mainSlider-container'),
    list: document.getElementById('mainSlider-list'),
    items: document.getElementsByClassName('slider__slide'),
    leftButton: document.getElementById('mainSlider-buttonLeft'),
    rightButton: document.getElementById('mainSlider-buttonRight')
}

createSlider(mainSlider);