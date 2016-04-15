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
    }
    setElData(){
        for(let el of elements){
            el = $(el);

            elData.push({
                shift: 0,
                diff: 0,
                offset: el.offset(),
                speed: el.data("speed")
            });
        }
    }
    _handleScroll(e){
        this._scrollY = $(document).scrollTop();

        elements.each((index, el) => {
            let data = elData[index];

            data.diff = this.getScrollDiff(data.offset.top);
            data.shift = this.getScrollShift(data.diff, data.speed);

            this.applyShift(el, data.shift);
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
}

export default Scrollify;