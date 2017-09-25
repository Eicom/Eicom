// MAPA
var api = 'AIzaSyAEEXndwXj8Wh09p-Rj6jyUEwMrOaBfHlU';
function initMap() {
    var latLng = {
        // lat: 20.4316085,
        lat: 32.4351823,
        lng: -114.7590884
        // lng: -101.7245765
    };
    var map = new google.maps.Map(document.getElementById('mapa'), {
        'center': latLng,
        'zoom': 14,
        'mapTypeId': google.maps.MapTypeId.ROADMAP
    });

    var contenido = '<h2>EICOM San Luis R.C.</h2>' +
                    '<p>Estamos para atenderte, ven y visítanos!</p>';

    var informacion = new google.maps.InfoWindow({
        content: contenido
    });
    var marker = new google.maps.Marker({
        position:latLng,
        map: map,
        title:'gtowebcamp'
    });
    marker.addListener('click', function(){
        informacion.open(map, marker);
    });
}

// CAROUSEL
$(document).ready(function(){
    $('.carousel[data-type="multi"] .item').each(function(){
        var next = $(this).next();
        if (!next.length) {
            next = $(this).siblings(':first');
        }
        next.children(':first-child').clone().appendTo($(this));

        for (var i=0;i<3;i++) {
            next=next.next();
            if (!next.length) {
                next = $(this).siblings(':first');
            }
            next.children(':first-child').clone().appendTo($(this));
        }
    });
});

// ELIMINAR PRODUCTO
$(document).on('click', '.confirm-delete', function(){
    return confirm('Estás seguro que deseas borrar el producto: {{ instance.clave }}?');
});