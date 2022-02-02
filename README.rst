==================
Outpost Django XML
==================

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|

.. |docs| image:: https://readthedocs.org/projects/outpost/badge/?style=flat
    :target: https://readthedocs.org/projects/outpost.django.xml
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/medunigraz/outpost.django.xml.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/medunigraz/outpost.django.xml

.. |requires| image:: https://requires.io/github/medunigraz/outpost.django.xml/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/medunigraz/outpost.django.xml/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/medunigraz/outpost.django.xml/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/medunigraz/outpost.django.xml

.. end-badges

Provide up-to-date event and lecturer data from CAMPUSonline for digital XML door signs.

* Free software: BSD license

Documentation
=============

https://outpost.django.xml.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
