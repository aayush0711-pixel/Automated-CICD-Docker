
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/aayush0711-pixel/Automated-CICD-Docker.git'
            }
        }

        stage('Validate') {
            steps {
                bat 'if not exist app.py exit /b 1'
                bat 'if not exist Dockerfile exit /b 1'
                bat 'if not exist requirements.txt exit /b 1'
                echo 'All project files are present.'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t jenkins-docker-app .'
            }
        }

        stage('Test Application') {
            steps {
                bat 'docker run --rm jenkins-docker-app python -c "import app; print(\'Application test passed\')"'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker rm -f jenkins-docker-app || echo No existing container to remove'
                bat 'docker run -d --name jenkins-docker-app -p 5000:5000 jenkins-docker-app'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'powershell -NoProfile -Command "Start-Sleep -Seconds 3; Invoke-RestMethod http://localhost:5000/health"'
            }
        }
    }
}
