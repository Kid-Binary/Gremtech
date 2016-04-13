def get_form_errors(form_errors_items):
    # Get only the first message from each field errors list
    errors = {
        field: error[0]
        for field, error in form_errors_items
    }

    return errors
