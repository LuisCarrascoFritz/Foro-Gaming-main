var settings = {
    "url": "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15",
    "method": "GET",
    "timeout": 0,
  };
  
  $.ajax(settings).done(function (response) {
    console.log(response);
  });

  $.ajax(settings).done(function (response) {
    console.log(response); 

    
    var dealsHtml = '';
    response.forEach(function(deal) {
        dealsHtml += `
            <div class="deal">
                <h2>${deal.title}</h3>
                <img id="logo" src="${deal.thumb}" alt="${deal.title}">
                <p>Precio actual: $${deal.salePrice}</p>
                <p>Precio original: $${deal.normalPrice}</p>
                
                
            </div>
            <hr>
        `;
    });

    // Inserta el HTML generado en el div con id "deals"
    $('#deals').html(dealsHtml);
});