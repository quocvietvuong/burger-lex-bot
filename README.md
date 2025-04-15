# burger-lex-bot
A demo for Amazon Lex with validation lambda, dynamoDB and S3

# Step to build and run lex
1. Create S3 bucket to store code of Lambda LexValidator and LambdaLogSaver

2. Enter lambdaValidate folder

cd lambdaValidate

3. zip the content (lambda_handler):

zip -r order_burger_bot_validate_lambda.zip .

4. Enter lambdaLogSaver folder

cd lambdaLogSaver

5. zip the content (lambda_handler):

zip -r order_burger_bot_cloudwatch_log_save_lambda.zip .

6. push the lambda_handler to s3 bucket

aws s3 rm s3://[Lambda-Lex-Validator-Log-Saver-Bucket-Name]/order_burger_bot_validate_lambda.zip
aws s3 cp order_burger_bot_validate_lambda.zip s3://[Lambda-Lex-Validator-Log-Saver-Bucket-Name]/order_burger_bot_validate_lambda.zip

aws s3 rm s3://[Lambda-Lex-Validator-Log-Saver-Bucket-Name]/order_burger_bot_cloudwatch_log_save_lambda.zip
aws s3 cp order_burger_bot_validate_lambda.zip s3://[Lambda-Lex-Validator-Log-Saver-Bucket-Name]/order_burger_bot_cloudwatch_log_save_lambda.zip

7. Deploy CloudFormation

aws cloudformation deploy --template-file template.yaml --stack-name [stack-name] --capabilities CAPABILITY_IAM

8. Add Lambda permission for LexValidator get called by Lex:

aws lambda add-permission --function-name LexValidator --statement-id chatbot-fulfillment --action "lambda:InvokeFunction" --principal "lex.amazonaws.com"

9. Build and Test the Lex bot