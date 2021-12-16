
pipeline {
<<<<<<< HEAD
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub_id')
        }

=======
>>>>>>> 09aa6b3 (jenkins)
    agent any
    stages {
        stage('Build') {
            steps {
<<<<<<< HEAD
                sh 'docker-compose build'
=======
                //
            }
        }
        stage('Test') {
            steps {
                //
>>>>>>> 09aa6b3 (jenkins)
            }
        }
        stage('Deploy') {
            steps {
<<<<<<< HEAD
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push anisa18/game-library'
                sh 'docker push anisa18/database'
=======
                //
>>>>>>> 09aa6b3 (jenkins)
            }
        }
    }
}