from flask import Flask
from flask import app, render_template
import os
import pyspark
from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.functions import mean, desc
from plotly.offline import download_plotlyjs, plot
from plotly.graph_objs import *
import psycopg2
import argparse


class MyClass:

    def __init__(self):
        parser = argparse.ArgumentParser(description='map')
        parser.add_argument('--servers', help='the postgreql ip address')
        args = parser.parse_args()

        self.make(args.servers)

    def make(self, servers):
        sparkSession = SparkSession.builder \
            .getOrCreate()

        url = "jdbc:postgresql://" + servers + "/wineDb?user=username&password=password"
        df = (sparkSession.read.format("jdbc")
              .options(url=url, dbtable="wine_reviews")
              .load())
        table = df.select('country', 'points').groupBy('country').agg(mean('points')).orderBy('avg(points)',
                                                                                              ascending=False)
        countryCols = table.select('country').collect()
        countries = list()
        for country in countryCols:
            countries.append(str(country[0]))
        pointCols = table.select('avg(points)').collect()
        points = list()
        for point in pointCols:
            points.append(point[0])
        data = dict(type='choropleth',
                    locationmode='country names',
                    locations=countries,
                    colorscale='Blues',
                    z=points,
                    colorbar={'title': 'Average Rating'}
                    )
        layout = dict(geo={'scope': 'world'})
        choromap = dict(data=[data], layout=layout)
        # get the html file path
        plot(choromap, filename='map.html')

def setUp():
    MyClass()

app = Flask(__name__)

@app.route('/')
def index():
    setUp()
     # make the templates dir
    newpath = r'/opt/app-root/src/templates'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    # move the file to the templates dir
    os.system('mv /opt/app-root/src/map.html /opt/app-root/src/templates/')
    #os.chmod(/opt/app-root/src/templates/map.html', 077)
    resp = render_template("map.html", title='Maps')
    return resp

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)