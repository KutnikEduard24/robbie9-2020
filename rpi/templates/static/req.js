  $('#btnStart').onclick(function(){
       $.ajax({
           type:"PUT",
           url:'http://localhost:5000/run'
       });
    });