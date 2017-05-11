$('.list-group-item').on('click',function(event){
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url  : 'filtro_articulo/',
        type : 'GET',
        data : { filter_categoria : element.attr("data")},
     })
};
