pipeline {
    agent any
    stages {
         stage('build') {
              when {
                  branch 'dev'             
              }
              steps {
                 echo "Working on dev branch"
              }
         }
     }
}