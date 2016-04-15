"use strict";

function setProgressPercents(){

    $(".progress-holder").each((index, el) => {
        el = $(el);
        el.find(".progress-bar").css({width: el.data("percents") + "%"});
    });

}

export default setProgressPercents;