pipeline {
    agent any
    stages {
        stage("Checkout") {
            environment {
                HOME = "${env.WORKSPACE}"
            }

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
            steps {t
                sh "zip -r function.zip ."
                archiveArtifacts artifacts: 'function.zip', fingerprint: true
            }
        }

    }
}