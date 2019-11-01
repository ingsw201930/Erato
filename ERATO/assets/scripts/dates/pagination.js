var current_index=0

function next(){
    current_index+=1;
    document.getElementById("current_index").innerHTML=current_index+1;
    get_date_list(current_index)
    $('.rating').rating();
}

function back(){
    if(current_index>0){
        current_index-=1;
        document.getElementById("current_index").innerHTML=current_index+1;
        get_date_list(current_index)
        $('.rating').rating();
    }
}

function get_date_list(index, baseurl){
    $.ajax({url: baseurl+"/s/get_date_list/"+index,
    success: function(result){
        container=document.getElementById("date_list_non_rated")
        container.innerHTML = result;
    }});
    $('.rating').rating();
}
