#!/bin/bash
source "$(dirname "${BASH_SOURCE}")/../../hack/lib/init.sh"
trap os::test::junit::reconcile_output EXIT

RESOURCE_DIR="$(dirname "${BASH_SOURCE}")/../resources"

os::test::junit::declare_suite_start "cmd/create"

os::cmd::expect_success 'oc new-project winemap-namespace' 

os::cmd::try_until_text 'oc new-app --template=postgresql-persistent -p POSTGRESQL_USER=username -p POSTGRESQL_PASSWORD=password -p POSTGRESQL_DATABASE=wineDb' 'Success'

os::cmd::try_until_text  'oc create -f $RESOURCE_DIR/wine-data-loader.yaml' 'template "wine-data-loader" created'

os::cmd::try_until_text 'oc create -f $RESOURCE_DIR/secret.yaml' 'secret "winemap-secret" created'

os::cmd::try_until_text 'oc new-app --template=wine-data-loader' 'Success'

os::cmd::try_until_text 'oc create -f https://radanalytics.io/resources.yaml' 'rolebinding ''"oshinko-edit" created'

os::cmd::try_until_text 'oc get templates' 'oshinko-webui'

os::cmd::try_until_text 'oc new-app --template=oshinko-python-spark-build-dc -p APPLICATION_NAME=winemap -p GIT_URI=https://github.com/radanalyticsio/winemap.git -p SPARK_OPTIONS='"'"'--packages org.postgresql:postgresql:42.1.4'"'"'-p APP_ARGS="-SERVER=postgresql -USER=username -PASSWORD=password -DBNAME=wineDb"' 'Success'
