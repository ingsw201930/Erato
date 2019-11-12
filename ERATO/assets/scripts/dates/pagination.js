function get_date_list_more_dates(index, baseurl){
    console.log("Getting list in index "+index)
    $.ajax({url: baseurl+"/s/get_date_list_more_dates/"+index,
    success: function(result){
        container=document.getElementById("date_list_more_dates")
        container.innerHTML = result;

      $('.ui.rating').rating({
          initialRating: 0,
          maxRating: 5,
          onRate: function (rating) {
          rate(baseurl, rating);
          }
      });


    }});
}

function next_more_dates(baseurl){
    current_index = parseInt(document.getElementById("current_index_more_dates").textContent, 10)-1;
    get_date_list_more_dates(current_index+1, baseurl);
    current_index+=1;
    document.getElementById("current_index_more_dates").innerHTML=current_index+1;
}

function back_more_dates(baseurl){
    current_index = parseInt(document.getElementById("current_index_more_dates").textContent,10)-1;
    if(current_index>0){
      get_date_list_more_dates(current_index-1, baseurl);
        current_index-=1;
        document.getElementById("current_index_more_dates").innerHTML=current_index+1;
    }
}
