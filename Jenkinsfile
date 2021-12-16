
pipeline {
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub_id')
        }
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push anisa18/game-library'
                sh 'docker push anisa18/database'
            }
        }
    }
}