ymaps.ready(init);

function init() {
    var myMap = new ymaps.Map("map", {
            center: [59.838336, 30.117805], // тут надо определить координаты юзера или если нет доступа к геопозиции то что будет, если ничего не делать?
            zoom: 10
        }, {
            searchControlProvider: 'yandex#search' // по меткам не ищет( 
        }),

        
 // для установки и получения координат точки
myGeoObject = new ymaps.GeoObject({
    geometry: {
        type: "Point",
        coordinates: [59.851504, 30.070433] // какие по умолчанию?
    },
    properties: {
        iconContent: 'передвинь меня', 
        hintContent: 'нажми чтобы увидеть координаты'
    }
}, {
    preset: 'islands#blackStretchyIcon',
    draggable: true
});

    // для установки и получения координат точки
myGeoObject.events.add('dragend', function(e) {
    // Получение ссылки на объект, который был передвинут.
    var thisPlacemark = e.get('target');
    // Определение координат метки
    var coords = thisPlacemark.geometry.getCoordinates();
    // и вывод их при щелчке на метке
    thisPlacemark.properties.set('balloonContent', coords);
 });

myPlace = new ymaps.Placemark([
    59.811908, 30.074203
    ],{
        balloonContent: 'Зеленая метка'
    }, {
        preset: 'islands#redGlyphIcon',            
        iconGlyph: 'tree-deciduous',
        iconGlyphColor: 'green',
        iconColor: 'green'
    });

myPlace2 = new ymaps.Placemark([
    59.811025, 30.083684
],{
    balloonContent: '<strong>Красная метка</strong>'  
}, {
    preset: 'islands#redGlyphIcon',            
        iconGlyph: 'eye-open',
        iconGlyphColor: 'red',
        iconColor: 'red'
});

myMap.geoObjects
    .add(myGeoObject)
    .add(myPlace)
    .add(myPlace2)
}

