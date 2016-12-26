$(function () {
    setInterval(function () {
        var el = $('.container[data-src]'), url = el.data('src');
        $.getJSON(url).done(function (data) {
            for(var i in data) {
                $('.member-balance_' + i).text(data[i]);
            }
        })
    }, 5000);
});
