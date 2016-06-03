/**
 * Created by Alonski on 6/2/2016.
 */

$(function () {
    console.log("start");
    var total_price = 0
    $('#dishes').on('click', 'li', function () {
        var el = $(this);
        console.log(el);
        console.log(el.data('price'));
        total_price += Number(el.data('price'));
        var new_el = $('<li>').text(el.text());
        new_el.append($('<input type="hidden" name="item">').val(el.data('id')));
        $('#frm ul').append(new_el);
        $('#price_total span').text(total_price);
        console.log(total_price);
    });
    console.log("end");

    // requst.POST['item'].getlist()

});