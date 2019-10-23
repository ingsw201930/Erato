var current_index=0

function accept(date_id){
    $.ajax({url: "{{BASEURL}}/accept_date/"+date_id, success: function(result){
        if(result.state=="failed"){
            return;
        }
        htmlString="<div class=\"ui green massive message\">Accepted successfully!</div>"
        var div = document.createElement('div');
        div.innerHTML = htmlString.trim();
        container=document.getElementById("message-"+date_id)
        container.appendChild(div);
    }});
}

function reject(date_id){
    $.ajax({url: "{{BASEURL}}/reject_date/"+date_id, success: function(result){
        if(result.state=="failed"){
            return;
        }
        htmlString="<div class=\"ui red massive message\">Rejected successfully!</div>"
        var div = document.createElement('div');
        div.innerHTML = htmlString.trim();
        container=document.getElementById("message-"+date_id)
        container.appendChild(div);
    }});
}

function get_date_list(index){
    $.ajax({url: "{{BASEURL}}/s/get_date_list/"+index, 
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