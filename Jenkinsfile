pipeline {
     agent any
     stages {
         stage('build') {
              when {
                  expression {
                     return env.BRANCH_NAME == 'dev';
                  }             
              }
              steps {
                 echo "Working on dev branch"
              }
         }
     }
}