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

function rate(date_id, rate, baseurl){
  $.ajax({url: baseurl+"/rate/"+date_id+"/"+rate, success: function(result){
      if(result.state=="failed"){
          return;
      }
  }});
  alert("rated");
}

function reject(date_id, baseurl){
    $.ajax({url: baseurl+"/reject_date/"+date_id, success: function(result){
        if(result.state=="failed"){
            return;
        }
        $('body').toast({
        class: 'success',
        message: 'You have rejected the date'
        })
        ;
    }});
}
