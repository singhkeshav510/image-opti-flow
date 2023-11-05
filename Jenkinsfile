pipeline {
    agent any

    environment {
        LAMBDA_FUNCTION_NAME = 'test_lambda'
        S3_BUCKET = 'image-opti-flow-bucket'
        S3_KEY = 'test_code.zip'
    }

    stages {
        stage("Checkout") {

            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/singhkeshav510/image-opti-flow']]])
            }
        }

        stage("Build") {          
            steps {
                sh "python3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip3 install -r requirements.txt"
            }
        }

        stage("Package") {
            steps {
                sh "zip -r ${S3_KEY} ."
            }
        }

        stage('Deploy') {
            steps {
                sh "aws s3 cp ${S3_KEY} s3://${S3_BUCKET}"
                sh "aws lambda update-function-code --function-name ${LAMBDA_FUNCTION_NAME} --s3-bucket ${S3_BUCKET} --s3-key ${S3_KEY}"
            }
        }
    }
}