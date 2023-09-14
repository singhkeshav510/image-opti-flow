pipeline {
    agent {
        docker {
            image 'python:3'
            label 'my-build-agent'
        }
    }
    stages {
        stage("Checkout") {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/singhkeshav510/image-opti-flow']]])
            }
        }

        stage("Build") {
            steps {
                sh "pyton3 -m venv venv"
                sh ". venv/bin/activate"
                sh "pip3 install -r requirements.txt"
            }
        }

        stage("Test") {
            steps {
                sh "python3 -m pytest test/"
                sh "coverage run -m pytest"
            }
        }

    }
}