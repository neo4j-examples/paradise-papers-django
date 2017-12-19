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
