var current_index=0

function get_service_list(index){
    $.ajax({
        url: "{{BASEURL}}/s/get_service_list/"+index,
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