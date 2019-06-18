# apig-cognito
Control Access to a REST API Using Amazon Cognito User Pools as Authorizer.

Deploy
------
Everthing:

	sls --stage $STAGE_NAME deploy

One function:

	sls --stage $STAGE_NAME deploy function --function $FUNCTION_NAME

Monitor
-------
One function:

	sls --stage $STAGE_NAME logs --tail --startTime 60m --function $FUNCTION_NAME
