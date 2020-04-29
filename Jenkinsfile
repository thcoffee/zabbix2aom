pipeline {
  agent none
  stages {
    stage('pwd_d') {
      parallel {
        stage('pwd_d') {
          steps {
            sh 'pwd'
          }
        }

        stage('ls') {
          steps {
            sh 'ls -l'
          }
        }

        stage('df') {
          steps {
            sh 'df'
          }
        }

      }
    }

  }
}