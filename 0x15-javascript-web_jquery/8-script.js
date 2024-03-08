// fetches and lists the title for all movies by using this URL
// https://swapi-api.hbtn.io/api/films/?format=json
// All movie titles must be list in the HTML tag UL#list_movies
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $('#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
