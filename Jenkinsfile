pipeline {
    agent any

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
                sh "pip install -r requirements.txt"
            }
        }

        stage("Test") {
            steps {
                sh "python3 -m pytest tests/"
            }
        }

    }
}