pipeline {
    agent any
    
    stages {
        stage('Deploy - Staging') {
            steps {
                sh 'printenv'
            }
        }

        stage('Sanity check') {
            steps {
                input "Does the staging environment look ok?"
            }
        }

        stage('Deploy - Production') {
            steps {
                sh 'printenv'
            }
        }
    }
}
