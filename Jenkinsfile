pipeline {
     agent any
     stages {
         stage('build') {
              when {
                  branch 'main'             
              }
              steps {
                 echo "Working on dev branch"
              }
         }
     }
}