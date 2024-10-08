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
    let product_count = $('#product-count').val();
    if (!product_count){
         product_count = 1;
    }

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
            }else {
                if (result.isConfirmed && res.status === 'not_completed') {
                    window.location.href = '/panel/profile-update/';
                };

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

  // product wish list functions

function addProducToWishlist(product_Id){
    const product_count = $('#product-count').val();
    $.get('/favorite/add-to-wishlist?product_id=' + product_Id).then(res => {
                Swal.fire({
              position: "top-end",
              icon: res.icon,
              title: res.title,
              text: res.text,
              showConfirmButton: false,
              timer: 1500
            }).then((result)=>{
            if ( result.isConfirmed && res.status === 'not_authenticated'){
                window.location.href = '/account/login';
            };
        })
    });
    };
function remove_favorite(favorite_Id){
    console.log("success");
     $.get('/panel/remove-wishlist?favorite_id=' + favorite_Id).then(res => {

         if (res.status === 'success'){
                $('#order_favorite_content').html(res.body);

         }
     })
};

// sweat alert of payment

function payment(order_Id){

    $.get('/order/payment?order_Id=' + order_Id).then(res => {
        Swal.fire({
            title: res.title,
            text: res.text,
            icon: res.icon,
            showCancelButton: res.show_cancel_button,
            cancelButtonText: "لغو",
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: res.confirm_button_text,
        // }).then((result)=>{
        //     if ( result.isConfirmed && res.status === 'not_authenticated'){
        //         window.location.href = '/account/login';
        //     }else {
        //         if (result.isConfirmed && res.status === 'not_completed') {
        //             window.location.href = '/panel/profile-update/';
        //         };
        //
        //     };
        })
    });
    };
