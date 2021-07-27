def url_gen(job, filters):
    '''
    Get a job title and job filters to generate the query url for scrapping

    Args:
        job (str): The job title you want to search for it.
        filters (dict): Lists of each filter values.

    Return:
        url (str): The url of the search query.
    '''
    # The base text of the url
    url = 'https://wuzzuf.net/search/jobs/?a=navbl'

    # Iterate through filters the through its values to edit the search query url
    for key, value in filters.items():
        if not value:
            continue
        if type(value) == list:
            value.sort()
            for i, value in enumerate(value):
                if key == 'career_level':
                    url += '&filters%5B{}%5D%5B{}%5D={}'.format(key,i,value.title().replace(' ','%20'))
                if key == 'job_types':
                    url += '&filters%5B{}%5D%5B{}%5D={}'.format(key,i,value.lower().replace(' ','_'))
            continue
        if type(value) == str:
            url += '&filters%5B{}%5D%5B0%5D=within_{}'.format(key,value.lower().replace(' ','_'))


    
    # Add the job title to the search query url
    url += '&q={}&start=0'.format(job.strip().lower().replace(' ','%20'))

    return url
