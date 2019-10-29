
var current_index=0

function get_date_list(index){
    $.ajax({url: "{{BASEURL}}/c/get_date_list/"+index, 
    success: function(result){
        container=document.getElementById("date_list")
        container.innerHTML = result;
    }});
}

function next(){
    current_index+=1;
    document.getElementById("current_index").innerHTML=current_index+1;
    get_date_list(current_index)
}

function back(){
    if(current_index>0){
        current_index-=1;
        document.getElementById("current_index").innerHTML=current_index+1;
        get_date_list(current_index)
    }
}