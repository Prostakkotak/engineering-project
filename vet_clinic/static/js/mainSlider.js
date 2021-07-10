function createSlider(obj) {
    if (obj.items.length != 1) {

        for (let i = 0; i < obj.items.length; i++) {

            let shortListItem = document.createElement('li')
            shortListItem.classList.add(obj.containerName + '__short-list-item')
            shortListItem.setAttribute('data-slide-number', i)

            obj.shortList.appendChild(shortListItem);
        }

        obj.shortListItems[0].classList.add('current');

        if (!obj.leftButton) obj.leftButton = '';
        if (!obj.rightButton) obj.rightButton = '';

        var itemWidth = obj.items[0].offsetWidth

        var betweenElemsDistance = Math.abs(obj.items[0].offsetLeft + obj.items[0].offsetWidth - obj.items[1].offsetLeft);

        var maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance);
        var currentScrollWidth = 0;

        document.addEventListener('click', function(e) {
            let target = e.target;

            while (target != this) {
                if (target == obj.rightButton) {
                    if (currentScrollWidth > maxScrollWidth) {
                        let currentItem = currentItemCalc();

                        currentScrollWidth =
                            currentScrollWidth - itemWidth - betweenElemsDistance;
                        obj.list.style.marginLeft = currentScrollWidth + "px";

                        obj.shortListItems[currentItem].classList.remove('current')
                        obj.shortListItems[currentItem + 1].classList.add('current')
                    } else {
                        currentScrollWidth = 0;
                        obj.list.style.marginLeft = currentScrollWidth + 'px';

                        obj.shortListItems[obj.shortListItems.length - 1].classList.remove('current')
                        obj.shortListItems[0].classList.add('current')
                    }
                } else if (target == obj.leftButton) {
                    if (currentScrollWidth < 0) {
                        let currentItem = currentItemCalc();

                        currentScrollWidth =
                            currentScrollWidth + itemWidth + betweenElemsDistance;
                        obj.list.style.marginLeft = currentScrollWidth + 'px';

                        obj.shortListItems[currentItem].classList.remove('current')
                        obj.shortListItems[currentItem - 1].classList.add('current')
                    } else {
                        currentScrollWidth = maxScrollWidth;
                        obj.list.style.marginLeft = currentScrollWidth + 'px';

                        obj.shortListItems[0].classList.remove('current')
                        obj.shortListItems[obj.shortListItems.length - 1].classList.add('current')
                    }
                } else if (target.classList.contains(obj.containerName + '__short-list-item')) {

                    let currentItem = currentItemCalc();
                    obj.shortListItems[currentItem].classList.remove('current')

                    if (+target.getAttribute('data-slide-number') != 0) {
                        currentScrollWidth =
                            (-itemWidth * target.getAttribute('data-slide-number')) - betweenElemsDistance;
                    } else {
                        currentScrollWidth = 0;
                    }

                    obj.shortListItems[+target.getAttribute('data-slide-number')].classList.add('current')
                    obj.list.style.marginLeft = currentScrollWidth + 'px';
                }

                target = target.parentNode;
            }
        })

        addEventListener("resize", function () {
            let currentItem = currentItemCalc();

            if (currentItem > 0) {
                // Если это не самый первый слайд, то идет перерасчет ширины прокрутки для новой ширины окна браузера
                currentScrollWidth = -((obj.items[0].offsetWidth + betweenElemsDistance) * currentItem);
            } else {
                currentScrollWidth = 0;
            }

            obj.list.style.marginLeft = currentScrollWidth + "px"; // Перемещение на новую точку после перерасчета
            maxScrollWidth = -((obj.items.length - 1) * obj.items[0].offsetWidth + betweenElemsDistance);
            itemWidth = obj.items[0].offsetWidth; // Запоминаем новую текущую ширину одного слайда
        });
    }

    function currentItemCalc() { // Находит индекс текущего элемента
        return Math.floor(-currentScrollWidth / itemWidth);
    }

    
}