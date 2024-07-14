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
    $.get('/order/add-to-order?product_id=' + product_Id+ '&count=' + product_count).then(res => {
        Swal.fire({
            title: res.title,
            text: res.text,
            icon: res.icon,
            showCancelButton: res.show_cancel_button,
            cancelButtonText: "لغو",
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: res.confirm_button_text,
        }).then((result)=>{
            if ( result.isConfirmed && res.status === 'not_authenticated'){
                window.location.href = '/account/login';
            };
        })
    });
    };
function remove_detail(detail_Id){
     $.get('/panel/remove-order-detail?detail_id=' + detail_Id).then(res => {
         if (res.status === 'success'){
                $('#order_detail_content').html(res.body);

         }
     })
};

  function handleQuantityChange(input, detail_Id) {
    // Get the updated value
    var updatedQuantity = input.value;

    // Perform your desired action with the updated quantity
    console.log('Updated quantity:', updatedQuantity);

         $.get('/panel/change-order-detail?detail_id=' + detail_Id+'&detail_number='+updatedQuantity).then(res => {
         if (res.status === 'success'){
               $('#order_detail_content').html(res.body);

         }
     })
  }
