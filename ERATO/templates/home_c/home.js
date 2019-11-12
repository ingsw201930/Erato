var current_index=0

function get_data(){
    var weight_min,weight_max
    if(document.getElementById("use_weight").checked){
        weight_min=document.getElementById("filter_weight_min").value;
        weight_max=document.getElementById("filter_weight_max").value;
    }else{
        weight_min=undefined;
        weight_max=undefined;
    }
    data={
        search:document.getElementById("filter_search").value,
        user:document.getElementById("filter_user").value,
        weight_min:weight_min,
        weight_max:weight_max
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
