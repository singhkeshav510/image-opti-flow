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
                sh "coverage run -m pytest"
                sh "coverage html"
            }
        }

        stage("Package") {
            steps {
                sh 'zip -r ${ZIP_FILE} .'
                archiveArtifacts artifacts: ZIP_FILE, fingerprint: true
            }
        }
    }
}