def get_form_errors(form, form_errors_items):
    # Get only the first message from each field errors list
    errors = {
        str(form.fields[field].label): error[0]
        for field, error in form_errors_items
    }

    return errors
