$(document).ready(function(e) {
  var lis = $('.nav > li');
  menu_focus( lis[0], 1 );

  $(".fancybox").fancybox({
    padding: 10,
    helpers: {
      overlay: {
        locked: false
      }
    }
  });

});


	<!-- autocomplete and add/remove for forms -->
$( function() {
  var genreTags = [
     "Reggae",
     "Latin",
     "Brass",
     "Classical",
     "Other",
     "Jazz",
     "Orchestra",
     "Pop",
     "Children's",
     "Folk",
     "World",
     "Country",
     "Hip Hop",
     "Stage & Screen",
     "Rock",
     "Funk",
     "Soul",
     "Blues",
     "Electronic & DJ"
  ];
  var artistTags = [
     "Ryan Adams",
     "Iron Maiden",
     "Metallica",
     "Led Zeppelin",
     "The 1975",
     "Nirvana",
     "Wes Montgomery",
     "AC/DC",
     "The Ramones",
     "Black Flag",
     "Pearl Jam",
     "Norma Jean",
     "He is Legend",
     "alt-j",
     "Anberlin",
     "Black Sabbath",
     "The Civil Wars",
     "The Clash",
     "Pantera",
     "Weezer"
  ];
  function split( val ) {
    return val.split( /,\s*/ );
  }
  function extractLast( term ) {
    return split( term ).pop();
  }

  $( "#genretags" )
    // don't navigate away from the field on tab when selecting an item
    .on( "keydown", function( event ) {
      if ( event.keyCode === $.ui.keyCode.TAB &&
          $( this ).autocomplete( "instance" ).menu.active ) {
        event.preventDefault();
      }
    })
    .autocomplete({
      minLength: 0,
      source: function( request, response ) {
        // delegate back to autocomplete, but extract the last term
        response( $.ui.autocomplete.filter(
          genreTags, extractLast( request.term ) ) );
      },
      focus: function() {
        // prevent value inserted on focus
        return false;
      },
      select: function( event, ui ) {
        var terms = split( this.value );
        // remove the current input
        terms.pop();
        // add the selected item
        terms.push( ui.item.value );
        // add placeholder to get the comma-and-space at the end
        terms.push( "" );
        this.value = terms.join( ", " );
        return false;
      }
    });

    $( "#artisttags" )
      // don't navigate away from the field on tab when selecting an item
      .on( "keydown", function( event ) {
        if ( event.keyCode === $.ui.keyCode.TAB &&
            $( this ).autocomplete( "instance" ).menu.active ) {
          event.preventDefault();
        }
      })
      .autocomplete({
        minLength: 0,
        source: function( request, response ) {
          // delegate back to autocomplete, but extract the last term
          response( $.ui.autocomplete.filter(
            artistTags, extractLast( request.term ) ) );
        },
        focus: function() {
          // prevent value inserted on focus
          return false;
        },
        select: function( event, ui ) {
          var terms = split( this.value );
          // remove the current input
          terms.pop();
          // add the selected item
          terms.push( ui.item.value );
          // add placeholder to get the comma-and-space at the end
          terms.push( "" );
          this.value = terms.join( ", " );
          return false;
        }
      });
} );

jQuery(function() {
    var locations = {
        'Boss': ['DS-1', 'TU-3', 'PS-2'],
        'TC Electronic': ['Ditto Looper'],
        'Electro-Harmonix': ['Small Clone','Small Stone','Hall of Fame'],
        'USA': ['Downers Grove'],
        'Mexico': ['Puebla'],
        'South Africa': ['Midrand'],
        'China': ['Beijing'],
        'Russia': ['St. Petersburg'],
    }

    $('[id^="brand"]').change(function () {
        var country = $(this).val(), lcns = locations[country] || [];

        var html = $.map(lcns, function(lcn){
            return '<option value="' + lcn + '">' + lcn + '</option>'
        }).join('');
        $('.pedalname').closest('select').html(html)
    });
});


// show recommendations table after button click
function showTable() {
    document.getElementById("table-data").style.display="none";
    document.getElementById("table-data").style.display="block";
}


// add more pedal data
$("#addMore").click(function(){
    $(".linedrop:first").clone(true).append('<button id="remove">-</button>').appendTo(".ui-widget");
    $(".linedrop:last").empty();
});

// remove unwanted pedal data
$(document).on("click", "#remove", function(){
   $(this).parent('div').remove();
});
