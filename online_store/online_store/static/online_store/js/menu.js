'use strict';
let menu_links = document.querySelector('.menu').querySelectorAll('li');
menu_links.forEach(link => {

    // изменить на этапе развертывания

    let link_slug = link.querySelector('a');
    if ('http://127.0.0.1:8000' + link_slug.getAttribute('href') === window.location.href) {
        link_slug.classList.add('active');
    }
});