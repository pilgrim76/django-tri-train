function refresh() {
   $.ajax({
     url: "",
     dataType: "text",
     success: function(html) {
       $('#fu').replaceWith($.parseHTML(html));
       setTimeout(refresh,2000);
     }
   });
}
refresh();

