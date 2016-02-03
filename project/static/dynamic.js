function evaluateChange(select, url, selectDescription, resultSelectId) {
    var selectedId = select.value;
    
    $.ajax({
        type: 'GET',
        url: url +'/' + selectedId + '/'
    }).done(function(data) {
        var option_list = [
            ["", "--- Select "+ selectDescription +" ---"]
        ].concat(Object.keys(data).map(function(key) {
            return [key, data[key]]
        }));

        $(resultSelectId).html($.map(option_list, function(option) {
            return $("<option></option>").attr("value", option[0]).text(option[1]);
        }));
    });
}

$("#region_select").change(function() {
	evaluateChange(this, '/dist', 'District', '#district_select');
});

$("#district_select").change(function() {
	evaluateChange(this, '/subd', 'Subdistrict', '#subdist_select');
});

$("#subdist_select").change(function() {
	evaluateChange(this, '/vill', 'Village', '#village_select');
});