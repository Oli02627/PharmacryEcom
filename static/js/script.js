
/*==increase-cart-quanity========================*/
$('.increase-cart-quanity').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[1]
    $.ajax({
        type: "GET",
        url: "pluscart",
        data: {
            cart_id:id
        },
        success: function (data){
            eml.innerText = data.quantity
            document.getElementById("subtotal-amount").innerText = data.total_amount.toFixed(2);
        }
    })
})


/*==decrese-cart-quanity===============*/
$('.decrease-cart-quanity').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[1]
    $.ajax({
        type: "GET",
        url: "minuscart",
        data: {
            cart_id:id
        },
        success: function (data){
            eml.innerText = data.quantity
            document.getElementById("subtotal-amount").innerText = data.total_amount.toFixed(2);
        }
    })
})


/*==Remove-Cart===============*/
$('.removecart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this
    $.ajax({
        type: "GET",
        url: "removecart",
        data: {
            cart_id:id
        },
        success: function (data){
            document.getElementById("subtotal-amount").innerText = data.total_amount.toFixed(2);
            eml.parentNode.parentNode.remove()
        }
    })
})