build: CMD=build
push: CMD=push
clean: CMD=clean
context: CMD=context
clean-context: CMD=clean-context
zero-tarballs: CMD=zero-tarballs

test-e2e:
	LOCAL_IMAGE=$(OPENSHIFT_SPARK_TEST_IMAGE) make build
	test/run.sh
