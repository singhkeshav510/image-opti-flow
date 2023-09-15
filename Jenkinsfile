pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1' // Specify your desired AWS region
        FUNCTION_NAME = 'my-lambda-function' // Replace with your Lambda function name
        LAMBDA_HANDLER = 'my_lambda.handler' // Replace with your Lambda handler function
        ZIP_FILE = "${FUNCTION_NAME}.zip"
    }

    stages {
        stage("Checkout") {

            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/singhkeshav510/image-opti-flow']]])
            }
        }

        stage("Build") {
            environment {
                HOME = "${env.WORKSPACE}"
            }            
            steps {
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip3 install -r requirements.txt"
            }
        }

        stage("Test") {
            steps {
                sh "/Users/keshavsingh/anaconda3/bin/coverage run -m pytest"
                sh "/Users/keshavsingh/anaconda3/bin/coverage html"
            }
        }

        stage("Package") {
            steps {
                sh 'zip -r ${ZIP_FILE} .'
                archiveArtifacts artifacts: ZIP_FILE, fingerprint: true
            }
        }

        stage('Deploy Lambda Function') {
            steps {
                withAWS(credentials: 'lambda_cred', region: AWS_DEFAULT_REGION) {
                    lambdaDeploy(
                        functionName: FUNCTION_NAME,
                        functionAlias: 'latest', // Optionally specify an alias
                        s3Bucket: 'your-s3-bucket', // Replace with your S3 bucket name
                        s3Object: ZIP_FILE,
                        handler: LAMBDA_HANDLER,
                        runtime: 'python3.8', // Replace with your Lambda runtime
                        role: 'arn:aws:iam::602601681465:role/testing', // Replace with your Lambda execution role ARN
                        description: 'My Lambda Function',
                        memorySize: 256, // Specify the memory size in MB
                        timeout: 10, // Specify the function timeout in seconds
                        publish: true // Set to true to publish a new version
                    )
                }
            }
        }

    }
}