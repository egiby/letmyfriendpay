(function($) {

	$('#complexify #password').complexify({minimumChars:6, strengthScaleFactor:0.7}, function (valid, complexity) {
		var progressBar = $('#complexify #complexity-bar');

		progressBar.toggleClass('progress-success', valid);
		progressBar.toggleClass('progress-danger', !valid);
		progressBar.attr("value", complexity);

		$('#complexify #complexity').text(Math.round(complexity) + '%');
	});

})(jQuery);