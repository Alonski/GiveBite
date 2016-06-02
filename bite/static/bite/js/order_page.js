/**
 * Created by Alonski on 6/2/2016.
 */

$(function () {
    console.log("start");

    $('#dishes').on('click', 'li', function () {
        var el = $(this);
        console.log(el);
        var new_el = $('<li>').text(el.text());
        new_el.append($('<input type="hidden" name="item">').val(el.data('id')));
        $('#frm ul').append(new_el);
    });

    console.log("end");

    // requst.POST['item'].getlist()

});