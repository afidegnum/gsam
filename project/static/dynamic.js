/**
 * Created by afidegnum on 1/30/16.
 */

$("#region_select").change(function() {
    var make_id = $(this).find(":selected").val();
    var request = $.ajax({
        type: 'GET',
        url: '/dist/' + region_id,
    });
    request.done(function(data){
        var option_list = [["", "--- Select One ---"]].concat(data);

        $("district_select").empty();
        for (var i = 0; i < option_list.length; i++) {
            $("#district_select").append(
                $("<option></option>").attr(
                    "value", option_list[i][0]).text(option_list[i][1])
            );
        }
    });
});

$("#district_select").change(function() {
    var make_id = $(this).find(":selected").val();
    var request = $.ajax({
        type: 'GET',
        url: '/subd/' + dist_id,
    });
    request.done(function(data){
        var option_list = [["", "--- Select One ---"]].concat(data);

        $("subdist_select").empty();
        for (var i = 0; i < option_list.length; i++) {
            $("#subdist_select").append(
                $("<option></option>").attr(
                    "value", option_list[i][0]).text(option_list[i][1])
            );
        }
    });
});

$("#subdist_select").change(function() {
    var make_id = $(this).find(":selected").val();
    var request = $.ajax({
        type: 'GET',
        url: '/vill/' + village_id,
    });
    request.done(function(data){
        var option_list = [["", "--- Select One ---"]].concat(data);

        $("village_select").empty();
        for (var i = 0; i < option_list.length; i++) {
            $("#village_select").append(
                $("<option></option>").attr(
                    "value", option_list[i][0]).text(option_list[i][1])
            );
        }
    });
});