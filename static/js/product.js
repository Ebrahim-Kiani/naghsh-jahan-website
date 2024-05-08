function showLargeImage(imagesrc, imageid){


    var elements = document.querySelectorAll('li[data-target="#carousel-example-1"]');
    for (var i = 0; i < elements.length; i++) {
        if (elements[i].classList.contains("active")) {
            elements[i].classList.remove("active");
        }
    }
    $('#' + imageid).addClass('active');

    var imgElement = document.getElementById('product-main-image-slide').querySelector('img');
    imgElement.src = imagesrc;

}
function addProducToOrder(product_Id){
    const product_count = $('#product-count').val();
    $.get('/order/add-to-order?product_id=' + product_Id+ '&count=' + product_count).then(response =>{
        console.log(response);
        });
}