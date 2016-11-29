$(function () {
    // console.log("123123");
    setInterval(function () {
        var el = $('.container[data-src]'), url = el.data('src');
        $.getJSON(url).done(function (data) {
            for(var i in data) {
                // console.log(i, el.find('.member-balance_' + i), data[i]);
                $('.member-balance_' + i).text(data[i]);
            }
        })
    }, 5000);
});
