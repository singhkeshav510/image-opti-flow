pipeline {
     agent any
     stages {
         stage('build') {
              when {
                  expression {
                     return env.BRANCH_NAME == 'main';
                  }             
              }
              steps {
                 echo "Working on dev branch"
              }
         }
     }
}