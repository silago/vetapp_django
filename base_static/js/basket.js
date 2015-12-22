
window.basket = { 
    basket_url: '/basket/',
    add_item: function(item_id,quantity,obj) {
        var url = this.basket_url+'put/'+item_id+'/'+quantity;
        $.ajax({url:url,dataType:'json',success:function(data) {
            var items = data.data;
            var count = 0;
            for (var i=0; i<items.length; i++) {
                count+=parseInt(items[i].quantity);
            }
            $('#basket_counter').html(count);
            if (obj) {
                $(obj).html('Товар в корзине')
                $(obj).addClass('secondary');
                $(obj).attr('disabled','disabled');

            }
            /* upp basket counter */
        }})
    },
    get_count: function() {
        var url = this.basket_url+'get/';
        $.ajax({url:url,dataType:'json',success:function(data){
            $('#basket_counter').html(data.data);
        }})
    },
}

