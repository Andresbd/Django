=====
Andan
=====

Este es un proyecto del semestre i

Quick start
-----------

1. Add "andan" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'andan',
    ]

2. Include the andan URLconf in your project urls.py like this::

    url(r'^andan/', include('andan.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
