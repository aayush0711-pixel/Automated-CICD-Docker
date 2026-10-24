
pipeline {
    agent any

    environment {
        DOCKER = 'C:\\Users\\aayus\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
        IMAGE = 'jenkins-docker-app'
        CONTAINER = 'jenkins-docker-app'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub.'
            }
        }

        stage('Validate') {
            steps {
                bat 'if not exist app.py exit /b 1'
                bat 'if not exist Dockerfile exit /b 1'
                bat 'if not exist requirements.txt exit /b 1'
                echo 'All required files are present.'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"%DOCKER%" build -t %IMAGE% .'
            }
        }

        stage('Test Application') {
            steps {
                bat '"%DOCKER%" run --rm %IMAGE% python -c "import app; print(\'Application test passed\')"'
            }
        }

        stage('Deploy') {
            steps {
                bat '"%DOCKER%" rm -f %CONTAINER% || exit /b 0'
                bat '"%DOCKER%" run -d --name %CONTAINER% -p 5000:5000 %IMAGE%'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'powershell -NoProfile -Command "Start-Sleep -Seconds 5; Invoke-RestMethod http://localhost:5000/health"'
            }
        }
    }
}
