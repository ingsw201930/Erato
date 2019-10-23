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