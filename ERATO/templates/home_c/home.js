var current_index=0

function get_data(){
    data={
        search:document.getElementById("filter_search").value,
        user:document.getElementById("filter_user").value,
    }
    if(document.getElementById("use_weight").checked){
        data.weight_min=document.getElementById("filter_weight_min").value;
        data.weight_max=document.getElementById("filter_weight_max").value;
    }
    if(document.getElementById("use_height").checked){
        data.height_min=document.getElementById("filter_height_min").value;
        data.height_max=document.getElementById("filter_height_max").value;
    }
    if(document.getElementById("use_price").checked){
        data.price_min=document.getElementById("filter_price_min").value;
        data.price_max=document.getElementById("filter_price_max").value;
    }
    return data
}

function get_service_list(index){
    $.ajax({
        url: "{{BASEURL}}/c/get_service_list/"+index,
        data:get_data(),
        success: function(result){
        container=document.getElementById("service_container")
        container.innerHTML = result;
    }});
}

function next(){
    current_index+=1;
    document.getElementById("current_index").innerHTML=current_index+1;
    get_service_list(current_index)
}

function back(){
    if(current_index>0){
        current_index-=1;
        document.getElementById("current_index").innerHTML=current_index+1;
        get_service_list(current_index)
    }
}

function filter(){
    current_index=0
    document.getElementById("current_index").innerHTML=current_index+1;
    get_service_list(current_index)
}
