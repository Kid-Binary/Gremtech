"use strict";

import "jquery";
import "jquery-validation";
import "jquery-mask-plugin";

import Loader from "./lib/loader";
import FeedbackController from "./controllers/feedbackController";

new Loader();

$(() => {

    new FeedbackController();
    $("form").validate({ignore: ""});
});