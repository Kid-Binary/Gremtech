"use strict";

import getVendor from "./getVendor";

let elements = $(".scrollify");
let elData = [];
let transform = getVendor("transform");

class Scrollify{

    constructor(){
        this._scrollY = 0;
        
        this.setElData();
        this._events();
    }
    _events(){
        $(document).on("scroll", (e) => { this._handleScroll(e) });
        $(window).on("resize", (e) => { this._handleResize(e) });
    }
    setElData(){
        for(let el of elements){
            el = $(el);

            elData.push({
                offset: el.offset(),
                speed: el.data("speed")
            });
        }
    }
    _handleScroll(e){
        this._scrollY = $(document).scrollTop();

        elements.each((index, el) => {
            let data = elData[index];
            let scrollDiff = this.getScrollDiff(data.offset.top);
            let scrollShift = 0;

            if(scrollDiff >= 0){
                scrollShift = this.getScrollShift(scrollDiff, data.speed);
                this.applyShift(el, scrollShift);
            }
            
        }); 

        return false;
    }
    getScrollDiff(offsetTop){
        return (this._scrollY + window.innerHeight) - offsetTop;
    }
    getScrollShift(diff, speed){
        return (diff / speed) * -1;
    }
    applyShift(el, shift){
        $(el).css({transform: "translate3d(0, "+ shift +"px, 0)"});
    }
    _handleResize(e){
        this._scrollY = 0;
        this.setElData();

        return false;
    }
}

export default Scrollify;