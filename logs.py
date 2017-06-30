#!/usr/bin/env python3
"""Python3 Logs Analysis Application."""

import psycopg2

DBNAME = "news"


def top_articles():
    """Return the 3 most popular articles of all time by total views."""
    print("=============================================================")
    print("The three most popular articles of all time by total views:")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT articles.title, log.views
              FROM (SELECT path, count(*) AS views FROM log
              WHERE status LIKE '%200%' GROUP BY path) AS log
              INNER JOIN articles
              ON log.path ILIKE '%' || articles.slug
              ORDER BY views DESC LIMIT 3;''')
    articles = c.fetchall()
    for article in articles:
        print (article[0] + ' ==> ' + str(article[1]))
    db.close()


def pop_authors():
    """Return the 3 most popular authors of all time by total views."""
    print("=============================================================")
    print("The three most popular authors of all time by total views:")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT authors.name, count(*) AS views
              FROM articles INNER JOIN authors
              ON authors.id = articles.author INNER JOIN
              log ON log.path ILIKE '%' || articles.slug
              GROUP BY authors.name ORDER BY views DESC LIMIT 3;''')
    authors = c.fetchall()
    for author in authors:
        print (author[0] + ' ==> ' + str(author[1]))
    db.close()


def high_errors():
    """Return the days where more than '1%' of requests lead to errors."""
    print("=============================================================")
    print("Days where more than '1%' of requests lead to errors.")
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute('''SELECT to_char(date, 'FMMonth FMDD, YYYY'), err/total as ratio
              FROM (select time::date AS date,
              count(*) AS total,
              sum((status != '200 OK')::int)::float AS err
              FROM log
              GROUP BY date) AS errors
              WHERE err/total > .01;''')
    errors = c.fetchall()
    db.close()

    for error in errors:
        print (error[0])
        print (str(round((error[1]*100), 2)) + '% errors')


top_articles()

pop_authors()

high_errors()
