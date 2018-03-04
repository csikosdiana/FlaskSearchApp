# -*- coding: utf-8 -*-
import json
from operator import itemgetter


json_data = open('exercise-data June 2017.json')
contacts = json.load(json_data)


def get_select_map():

    job_history = {}
    company = {}
    email = {}
    city = {}
    name = {}
    country = {}

    select_map = {
        'Job history': job_history,
        'Company': company,
        'Email': email,
        'City': city,
        'Name': name,
        'Country': country
    }

    for i, contact in enumerate(contacts):

        # Fill the job_history dictionary
        for job in contact['job_history']:
            job = job.lower()
            if job not in job_history:
                job_history[job] = [i]
            else:
                job_history[job].append(i)

        # Fill the company dictionary
        company_lower = contact['company'].lower()
        if company_lower not in company:
            company[company_lower] = [i]
        else:
            company[company_lower].append(i)

        # Fill the email dictionary
        email_lower = contact['email'].lower()
        if email_lower not in email:
            email[email_lower] = [i]
        else:
            email[email_lower].append(i)

        # Fill the city dictionary
        city_lower = contact['city'].lower()
        if city_lower not in city:
            city[city_lower] = [i]
        else:
            city[city_lower].append(i)

        # Fill the name dictionary
        name_lower = contact['name'].lower()
        if name_lower not in name:
            name[name_lower] = [i]
        else:
            name[name_lower].append(i)

        # Fill the country dictionary
        country_lower = contact['country'].lower()
        if country_lower not in country:
            country[country_lower] = [i]
        else:
            country[country_lower].append(i)

    return select_map


def get_results(selected, search_term):
    """
    Given a selected and a search term it will return a tuple which contains
    the search results. If the search_term is empty it will give back all contacts.
    If the search_term doesn't exists as a key in the selected results, i will also
    return all contacts.
    """
    if not search_term:
        return contacts

    select_map = get_select_map()
    selected_results = select_map[selected]
    search_term = search_term.lower()
    try:
        final_results = itemgetter(*selected_results[search_term])(contacts)
    except KeyError:
        return None

    if not isinstance(final_results, tuple):
        final_results = (final_results,)
    return final_results


def display_job_history_as_a_string(job_history_list):
    return ', '.join(job_history_list)
