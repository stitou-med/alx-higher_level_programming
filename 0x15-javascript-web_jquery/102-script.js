// script that fetches and prints how to say “Hello” depending on the language
// API service: https://www.fourtonfish.com/hellosalut/hello/
// language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
// translation must be fetched when the user clicks on INPUT#btn_translate
// The translation of “Hello” must be displayed in the HTML tag DIV#hello
$('document').ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/?';
  $('#btn_translate').click(function () {
    $.get(url + $.param({ lang: $('#language_code').val() }), function (data) {
      $('#hello').html(data.hello);
    });
  });
});
