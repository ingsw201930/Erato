function accept(date_id, baseurl){
    $.ajax({url: baseurl+"/accept_date/"+date_id, success: function(result){
        if(result.state=="failed"){
            return;
        }
        $('body').toast({
        class: 'success',
        message: 'You have accepted the date'
        })
        ;
    }});
}

function reject(date_id, baseurl){
    $.ajax({url: baseurl+"/reject_date/"+date_id, success: function(result){
        if(result.state=="failed"){
            return;
        }
        $('body').toast({
        class: 'success',
        message: 'You have rejected the date'
        });
    }});
}


function end_date(date_id, baseurl){
    console.log("Ending date")
    $.ajax({url: baseurl+"/end_date/"+date_id, success: function(result){
        if(result.state=="failed"){
            return;
        }
        $('body').toast({
        class: 'success',
        message: 'You have ended the date'
        });
    }});
}
