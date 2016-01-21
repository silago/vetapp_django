

    $(function() {
       basket.get_count();
       $('.sub_in').closest('div').parent().addClass('in');
    })



window.searchOnEnter = function(e,obj) {
    if (e.keyCode == 13 ) {
        var url = '/search/';
        var val = $(obj).val();
        document.location = url+val+'/';
    }
    
}
