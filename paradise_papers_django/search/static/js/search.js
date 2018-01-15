function handleListVisibility (event, template) {
    var button = event.target.parentElement;
    var container = $(template);
    var currentTemplate = $('.show');
    $('.nav-button.active').toggleClass("active");
    $(button).toggleClass("active");
    currentTemplate.hide();
    currentTemplate.toggleClass('show');
    container.show();
    container.toggleClass('show');
}

function changeTabs(current, other) {
	var currentTab = $(current);
	var otherTab = $(other);
	if (currentTab.hasClass("not-active"))  {
		currentTab.removeClass("not-active");
		otherTab.addClass("not-active");
	}

}
var juristictionTab = $('.search-by-jurisdiction');
var CountryTab = $('.search-by-country');
var countryDropdown = $('.country-selected');
var jurisdictionDropdown = $('.jurisdiction-selected');

juristictionTab.click(function(e) {
    if ($(this).hasClass("not-active")) {
	    $(this).removeClass("not-active");
	    CountryTab.addClass("not-active");
	    countryDropdown.addClass("dropdown-no-display");
	    jurisdictionDropdown.removeClass("dropdown-no-display");
	} 
});

CountryTab.click(function(e) {
    if ($(this).hasClass("not-active")) {
	    $(this).removeClass("not-active");
	    juristictionTab.addClass("not-active");
	    countryDropdown.removeClass("dropdown-no-display");
	    jurisdictionDropdown.addClass("dropdown-no-display");
	} 
});
