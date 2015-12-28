

    $(function() {
       basket.get_count();
    })



window.searchOnEnter = function(e,obj) {
    if (e.keyCode == 13 ) {
        var url = '/search/';
        var val = $(obj).val();
        document.location = url+val+'/';
    }
    
}
