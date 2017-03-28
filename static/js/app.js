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

jQuery(function($) {
    var locations = {
        'Boss': ['DS-1', 'TU-3', 'PS-2'],
        'Spain': ['Barcelona'],
        'Hungary': ['Pecs'],
        'USA': ['Downers Grove'],
        'Mexico': ['Puebla'],
        'South Africa': ['Midrand'],
        'China': ['Beijing'],
        'Russia': ['St. Petersburg'],
    }

    var $locations = $('#pedalname');
    $('#brand').change(function () {
        var country = $(this).val(), lcns = locations[country] || [];

        var html = $.map(lcns, function(lcn){
            return '<option value="' + lcn + '">' + lcn + '</option>'
        }).join('');
        $locations.html(html)
    });
});


$(function() {
  $("#addMore").click(function(e) {
    e.preventDefault();
    $('#linedrop').clone().appendTo("#ui-widget");
  });
});

var options = $python_list;
var brand_list = $python_list;
var product_list = $python_list;
var cat_list = $python_list;
var instrument_list = $python_list;
var url_list = $python_list;


	var props = {
		filters_row_index: 1,
		sort: true,
		sort_config: {
			sort_types:['String','String','US','US','US','US','US','US','US']
		},
		remember_grid_values: true,
		alternate_rows: true,
		rows_counter: true,
		rows_counter_text: "Displayed rows: ",
		btn_reset: true,
		btn_reset_text: "Clear",
		btn_text: " > ",
		loader: true,
		loader_text: "Filtering data...",
		loader_html: '<img src="loader.gif" alt="" ' +
				'style="vertical-align:middle;" /> Loading...',
		on_show_loader: hideIESelects, //IE only: selects are hidden when loader visible
		on_hide_loader: showIESelects, //IE only: selects are displayed when loader closed
		col_0: "select",
		col_1: "select",
		col_2: "select",
		col_9: "none",
		display_all_text: "< Show all >",
		col_width: ["15%","10%","10%","10%","13%","10%","12%","10%","10%"]
	}
	var tf = setFilterGrid("demo",props);
