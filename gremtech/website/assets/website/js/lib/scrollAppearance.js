"use strict";

const topShift = 80;
let elements = $(".scroll-appearance");

class ScrollAppearance{

    constructor(){
        this._scrollY = 0;
        this._events();
    }
    _events(){
        $(document).on("scroll", (e) => { this._handleScroll(e) });
    }
    _handleScroll(e){
        this._scrollY = $(window).scrollTop();

        for(let el of elements){
            el = $(el);
            ((this._scrollY + window.innerHeight) >= el.offset().top + topShift) ? el.addClass("active") : el.removeClass("active");
        }
        return false;
    }
}

export default ScrollAppearance;