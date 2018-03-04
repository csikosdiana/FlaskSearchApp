# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from forms import ContactSearchForm

from data_processing import display_job_history_as_a_string, get_results


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    search = ContactSearchForm(request.form)
    if request.method == 'POST':
        if request.form['submit'] == 'Search':
            selected, search_term = search.data['select'], search.data['search']
            final_results = get_results(selected, search_term)
            return render_template(
                'results.html',
                form=search,
                final_results=final_results,
                selected=selected,
                search_term=search_term,
                display_job_history=display_job_history_as_a_string
            )

    return render_template(
        'index.html',
        form=search
    )


if __name__ == '__main__':
    app.run()
