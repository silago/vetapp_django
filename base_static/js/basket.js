
window.minus_html = function(obj) {
    $(obj).val($(obj).val()-1);
}

window.plus_html = function(obj) {
    $(obj).val(parseInt($(obj).val())+1);
}

window.basket = { 
    basket_url: '/basket/',
    add_item: function(item_id,quantity) {
        var url = this.basket_url+'put/'+item_id+'/'+quantity;
        $.ajax({url:url,dataType:'json',success:function(data) {
            var items = data.data;
            var count = 0;
            for (var i=0; i<items.length; i++) {
                count+=parseInt(items[i].quantity);
            }
            $('#basket_counter').html(count);
            var obj = $('.add-to-cart-'+item_id);
            if (typeof obj!='undefined') {
                $(obj).html('Товар добавлен')
                $(obj).addClass('secondary');
                $(obj).attr('disabled','disabled');
            }
            /* upp basket counter */
        }})
    },
    del_item: function(item_id) {
        var url = this.basket_url+'delete/'+item_id+'/';
        $.ajax({url:url,dataType:'json',success:function(data) {
            var items = data.data;
            var count = 0;
            for (var i=0; i<items.length; i++) {
                count+=parseInt(items[i].quantity);
            }
            $('#basket_counter').html(count);
        }})
    },
    get_count: function() {
        var url = this.basket_url+'get/';
        $.ajax({url:url,dataType:'json',success:function(data){
            var items = data.data;
            var count = 0;
            for (var i=0; i<items.length; i++) {
                count+=parseInt(items[i].quantity);
            }
            $('#basket_counter').html(count);
        }})
    },
}

