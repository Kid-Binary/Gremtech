"use strict";

import Cookies from "../lib/cookies";

let form = $("#feedback-form");
let loaderHolder = $("#loader-holder");
let responseHolder = $("#response-holder");
let token = Cookies.get("csrftoken");

let isDone = true;

class FeedbackController{

    constructor(){
        this._events();
    }
    _events(){
        form.on("submit", (e) => { this._handleForm(e) });
    }
    _handleForm(e){
        e.preventDefault();

        if(!form.valid() && !isDone) return;

        isDone = false;

        loaderHolder.addClass("active");
        responseHolder.removeClass().empty();

        $.ajax({
            url: form.attr("action"),
            type: "POST",
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": token
            },
            data: form.serializeArray()
        })
        .done((response) => {
            response = JSON.parse(response);

            responseHolder.addClass("success").html(`<p>${response.message}</p>`);
            form[0].reset();
        })
        .fail((response) => {
            response = JSON.parse(response.responseText);

            let html = "";
            for(let key in response.errors){
                html += `<li><p>${key}: <span>${response.errors[key]}</span></p></li>`;
            }

            responseHolder.addClass("error").html(`
                <p>${response.message}</p>
                <ul>${html}<ul>
            `);
        })
        .always(() => {
            
            loaderHolder.removeClass("active");
            window.scrollTo(0, 0);

            window.setTimeout(function(){
                responseHolder.removeClass().empty();
                isDone = true;
            }, 5000);
        });
        
    }
}

export default FeedbackController;