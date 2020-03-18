
from imdb.models import *
from .utils import execute_sql_query

def get_two_bar_plot_data_director_hits():
    import json

    data = execute_sql_query(
        """
        SELECT m.name,
            m.collections,
            m.director_id,
            AVG(collections)
        FROM imdb_movie AS m
        WHERE 
            m.collections IN (SELECT MAX(collections) FROM imdb_movie GROUP BY director_id)
            
        GROUP BY director_id
        ORDER BY director_id DESC;
        """
    )
    lables,data1,data2,data3 = [],[],[],[]
    for item in data:
        lables.append((Director.objects.get(id = item[2]).name).split()[-1])
        # lables.append(Director.objects.get(id = item[2]).name)
        data1.append(item[3])
        data2.append(item[1])
        data3.append(item[0])

    multi_bar_plot_data = {
        "labels": lables,
        "datasets": [
            {
                "label": "Avg Of Movies Collection",
                "data": data1,
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "borderWidth": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)",
                "fontFamily": "Poppins"
            },
            {
                "label": "High Rated Movie Collection",
                "data": data2,
                "borderColor": "rgba(0,0,0,0.09)",
                "borderWidth": "0",
                "backgroundColor": "hsla(252, 100%, 46%, 0.5)",
                "fontFamily": "Poppins"
            }
        ]
    }

    return {
        'multi_bar_plot_data_one': json.dumps(multi_bar_plot_data),
        'multi_bar_plot_data_one_title': 'Director Max Collection'
    }


def get_area_plot_data_movie_year():
    import json


    data = execute_sql_query(
        """
            SELECT m.name,
                strftime('%Y',m.date_of_release) AS year,
                AVG(m.collections)
            FROM imdb_movie as m
            GROUP BY year;
        """
    )
    lables, data1, data2 = [],[],[]
    for item in data:
        lables.append(item[0])
        data1.append(item[1])
        data2.append(item[2])

    area_plot_data = {
        "labels": data1,
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "data": data2,
            "label": "Colections",
            "backgroundColor": 'rgba(0,103,255,.15)',
            "borderColor": 'rgba(0,103,255,0.5)',
            "borderWidth": 3.5,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(0,103,255,0.5)',
        }, ]
    }
    return {
        'area_plot_data_one': json.dumps(area_plot_data),
        'area_plot_data_one_title': 'Movie Industry'
    }



def get_pie_chart_data_gender():
    import json


    from imdb.models import Movie
    fmale = Actor.objects.filter(gender = 'F').count()
    male = Actor.objects.filter(gender = 'M').count()
    pie_chart_data = {
        "datasets": [{
            "data": [fmale,male],
            "backgroundColor": [
                "rgba(123, 123, 255,0.9)",
                "rgba(0, 123, 255,0.3)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": ['Female', 'Male']
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'Male vs Female'
    }


def get_doughnut_chart_data_genre():
    import json
    from imdb.models import Movie

    labels = Genre.objects.all()
    data,genre = [],[]
    for item in labels:
        data.append(Movie.objects.filter(genre = item).count())
    for label in labels:
        genre.append(label.name)
    doughnut_graph_data = {
        "datasets": [{
            "data": data,
            "backgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": genre
        
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': 'Genre'
    }


def get_multi_line_plot_data_gender():
    import json

    years_list = execute_sql_query(
        """
            SELECT 
                strftime('%Y',date_of_release) AS year
            FROM imdb_movie
            GROUP BY year;
        """
    )

    data = execute_sql_query(
        """
            SELECT COUNT(DISTINCT(a.id)) as count,
                a.gender,
                strftime('%Y',m.date_of_release) AS year
            FROM imdb_movie AS m
            INNER JOIN imdb_cast AS c
                ON m.id = c.movie_id
            INNER JOIN imdb_actor AS a
                ON a.id = c.actor_id
            GROUP BY year,a.gender;
        """
    )
    print(years_list)
    print(data)
    print('\n')
    years = []
    for year in years_list:
        years.append(year[0])
    
    # for item in data:
    #     years.append(item[2])

    male_count, female_count = [],[]

    for year in years:
        male_count.append([year,0])
        female_count.append([year,0])
    
    print()
    print(male_count)
    print(female_count)
    print()

    for year in years:
        for item in data:
            if item[2] ==  year and item[1]=='M':
                for elem in male_count:
                    if year == elem[0]:
                        elem[1] = item[0]
            elif item[2] ==  year and item[1]=='F':
                for elem in female_count:
                    if year == elem[0]:
                        elem[1] = item[0]
    

    print(male_count)
    print(female_count)

    final_male,final_female = [],[]

    for count in male_count:
        final_male.append(count[1])
    

    for count in female_count:
        final_female.append(count[1])

    print(final_female,final_male)
    multi_line_plot_data = {
        "labels": list(years),
        "type": 'line',
        "defaultFontFamily": 'Poppins',
        "datasets": [{
            "label": "Male",
            "data": final_male,
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(220,53,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(220,53,69,0.75)',
        }, 
        {
            "label": "Female",
            "data": final_female,
            "backgroundColor": 'transparent',
            "borderColor": 'rgba(40,167,69,0.75)',
            "borderWidth": 3,
            "pointStyle": 'circle',
            "pointRadius": 5,
            "pointBorderColor": 'transparent',
            "pointBackgroundColor": 'rgba(40,167,69,0.75)',
        }
        ]
    }
    return {
        'multi_line_plot_data_one': json.dumps(multi_line_plot_data),
        'multi_line_plot_data_one_title': 'Year VS Gender'
    }



def get_polar_chart_data_genre():
    import json


    coll = execute_sql_query(
        """
            SELECT SUM(collections) as collections,
                genre_id,
                g.name
            FROM imdb_movie AS m
            INNER JOIN imdb_movie_genre as mg
            ON mg.movie_id = m.id
            INNER JOIN imdb_genre AS g
            ON mg.genre_id = g.id
            GROUP BY genre_id;
        """
    )
    labels = [item[2] for item in coll]
    data = [item[0] for item in coll]
    polar_chart_data = {
        "datasets": [{
            "data": data,
            # "backgroundColor": [
            #     "rgba(0, 123, 255,0.9)",
            #     "rgba(0, 123, 255,0.8)",
            #     "rgba(0, 123, 255,0.7)",
            #     "rgba(0,0,0,0.2)",
            #     "rgba(0, 123, 255,0.5)"
            # ]


            "backgroundColor": [
                'red',
                'maroon',
                'blue',
                'tomato',
                'orangered',
                'orange'
            ]

        }],
        "labels": labels
    }
    return {
        'polar_chart_data_one': json.dumps(
            polar_chart_data),
        'polar_chart_data_one_title': 'Genre_Collections'
    }




def get_one_bar_plot_data_subscribers():
    import json

    subs = execute_sql_query(
        """
            SELECT SUM(no_of_subscribers) AS subs,
                strftime('%Y', date_of_release) AS year
            FROM imdb_movie
            WHERE year > "(SELECT strftime('%Y', 'now')-10)"
            GROUP BY year;
        """
    )

    years = [item[1] for item in subs]
    subscribers = [item[0] for item in subs]

    single_bar_chart_data = {
        "labels": years,
        "datasets":[
            {
                "data": subscribers,
                "name": "Single Bar Chart",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "border_width": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
                
            }
        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Subscribers over the years'
    }




def get_one_bar_plot_data_award_nominees():
    import json

    award_list = list(Award.objects.all())
    awards = [award.name for award in award_list]
    count = []
    for award in award_list:
        count.append(award.actor_set.all().count())

    single_bar_chart_data = {
        "labels": awards,
        "datasets":[
            {
                "data": count,
                "name": "Awards",
                "borderColor": "rgba(0, 123, 255, 0.9)",
                "border_width": "0",
                "backgroundColor": "rgba(0, 123, 255, 0.5)"
            }
        ]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Award_count'
    }