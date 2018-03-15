# winemap
This is the app that calls a postgresql db to show a map of wine reviews using these commands:

```sh
oc create -f https://radanalytics.io/resources.yaml
```

```sh
oc new-app --template=oshinko-python-build-dc -p APPLICATION_NAME=winemap -p GIT_URI=https://github.com/rebeccaSimmonds19/winemap.git -p SPARK_OPTIONS='--packages org.postgresql:postgresql:42.1.4' -p APP_ARGS="-SERVER=postgresql -USER=username -PASSWORD=password -DBNAME=wineDb"
oc new-app --template=oshinko-pyspark-build-dc -p APPLICATION_NAME=winemap -p GIT_URI=https://github.com/radanalyticsio/winemap.git -p SPARK_OPTIONS='--packages org.postgresql:postgresql:42.1.4' -e SERVER=postgresql -e DBNAME=wineDb -e PASSWORD=password -e USER=username
