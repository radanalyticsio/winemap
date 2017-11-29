# winemap
This is the app that calls a postgresql db to show a map of wine reviews using these commands:

oc create -f https://radanalytics.io/resources.yaml

oc new-app --template oshinko-pyspark-build-dc -p APPLICATION_NAME=winemap -p GIT_URI=https://github.com/rebeccaSimmonds19/winemap.git -p SPARK_OPTIONS='--jars postgresql-42.1.4.jar --conf spark.driver.extraClassPath=postgresql-42.1.4.jar' -p APP_ARGS=--servers='postgresql'

oc expose svc/

oc new-app --template oshinko-pyspark-build-dc -p APPLICATION_NAME=winemap -p GIT_URI=https://github.com/rebeccaSimmonds19/winemap.git -p SPARK_OPTIONS='--packages org.postgresql:postgresql:42.1.4 --conf spark.driver.extraClassPath=postgresql-42.1.4.jar' -p APP_ARGS="-server=postgresql -user=username -password=password -dbname=wineDb"

