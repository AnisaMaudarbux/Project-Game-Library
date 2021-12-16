
pipeline {
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 9c884f2 (this works?)
    environment {
        DOCKERHUB_CREDENTIALS=credentials('dockerhub_id')
        }

<<<<<<< HEAD
=======
>>>>>>> 09aa6b3 (jenkins)
=======
>>>>>>> 9c884f2 (this works?)
    agent any
    stages {
        stage('Build') {
            steps {
<<<<<<< HEAD
<<<<<<< HEAD
                sh 'docker-compose build'
=======
                //
=======
                sh 'docker-compose build'
>>>>>>> 9c884f2 (this works?)
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
<<<<<<< HEAD
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push anisa18/game-library'
                sh 'docker push anisa18/database'
=======
                //
>>>>>>> 09aa6b3 (jenkins)
=======
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push anisa18/game-library'
                sh 'docker push anisa18/database'
>>>>>>> 9c884f2 (this works?)
            }
        }
    }
}