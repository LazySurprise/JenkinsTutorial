pipeline {
    agent { docker { image 'node:6.9.0' } }
    stages {
        stage('build') {
            steps {
                sh 'npm --version'
            }
        }
    }
}
