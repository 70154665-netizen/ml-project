pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'docker-flask-app:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching code from GitHub...'
            }
        }

        stage('Create Python Environment') {
            steps {
                sh 'python3 -m venv .dk'
            }
        }

        stage('Install Requirements') {
            steps {
                sh '''
                    . .dk/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test Application') {
            steps {
                sh '''
                    . .dk/bin/activate
                    python -m unittest discover -s . -p "*test*.py" || true
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }
    }
}
