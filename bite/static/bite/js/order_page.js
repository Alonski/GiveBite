/**
 * Created by Alonski on 6/2/2016.
 */

$(function () {
    // console.log("start");
    var total_price = 0
    // $('#dishes').on('click', 'li', function () {
    //     var el = $(this);
    //     console.log(el);
    //     console.log(el.data('price'));
    //     total_price += Number(el.data('price'));
    //     var new_el = $('<li>').text(el.text());
    //     new_el.append($('<input type="hidden" name="item">').val(el.data('id')));
    //     $('#frm ul').append(new_el);
    //     $('#price_total span').text(total_price);
    //     console.log(total_price);
    // });

    $('#orderTable').on('click', 'tbody tr', function () {
        var orderTable = $(this);
        // console.log(orderTable.closest('tr').find('td:eq(1)').text());
        total_price -= Number(orderTable.closest('tr').find('td:eq(1)').text().substring(1));
        $('#price_total span').text(total_price);
        orderTable.closest('tr').remove();
    });

    $('#menuTable').on('click', 'tr', function () {
        /*
         When a tr is clicked (Add Dish To Order)
         Copies the tr to the Order Table.
         */
        var menuTable = $(this);
        // console.log(el);
        // console.log(el.data('price'));
        // var new_el = '<tr>';
        var dish_name = menuTable.closest('tr').find('td:eq(0)').text();
        var dish_price = menuTable.closest('tr').find('td:eq(1)').text().substring(1);
        var dish_description = menuTable.closest('tr').find('td:eq(2)').text();
        total_price += Number(dish_price);
        var new_tr = $('<tr></tr>');
        new_tr.append($('<td></td>').text(dish_name));
        new_tr.append($('<td></td>').text('$' + dish_price));
        new_tr.append($('<td></td>').text(dish_description));
        // var new_el = $('<td>').text(el.text());
        // new_el += '</td>';
        new_tr.append($('<input type="hidden" name="item">').val(menuTable.data('id')));
        $('#orderTable tbody').append(new_tr);
        $('#price_total span').text(total_price);
        // console.log(total_price);
    });
    // console.log("end");

    // requst.POST['item'].getlist()

});