"use strict";

class Loader{

    constructor(){
        this._events();
    }
    _events(){
        $(window).on("load", (e) => { this._handleLoad(e) });
    }
    _handleLoad(e){

        window.setTimeout(function(){
            $("body").addClass("__loaded");
        }, 2000);

        window.setTimeout(function(){
            window.scrollTo(0, 0);
        }, 100);

        return false;
    }
}

export default Loader;