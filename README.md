# winemap

Prerequisites:

https://radanalytics.io/get-started

https://github.com/radanalyticsio/winemap-data-loader
 
This is the app that calls a postgresql db to show a map of wine reviews using these commands:


```sh
oc new-app --template=oshinko-python-spark-build-dc \
  -p APPLICATION_NAME=winemap \
  -p GIT_URI=https://github.com/radanalyticsio/winemap.git \
  -p SPARK_OPTIONS='--packages org.postgresql:postgresql:42.1.4' \
  -e SERVER=postgresql \
  -e DBNAME=wineDb \
  -e PASSWORD=password \
  -e USER=username
  ```
