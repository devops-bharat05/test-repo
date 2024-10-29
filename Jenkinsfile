pipeline {
    agent { label 'Jenkins-worker01' }

    environment {
        VENV_PATH = "venv" // Path to the virtual environment
    }
    stages {
        stage('Build') {
            steps {
                // Install dependencies in a virtual environment
                sh 'sudo apt install python3-pip'
                sh 'sudo apt install python3-virtualenv'
				sh """	virtualenv venv
						source venv/bin/activate
						pip install Flask
				   """
            }
        }
        stage('Test') {
            steps {
                // Run unit tests
                sh './$VENV_PATH/bin/pytest test/'
            }
        }
        stage('Deploy') {
            steps {
                // Deploy to staging (example: simple gunicorn command)
                script {
                    sh """
							nohup gunicorn -w 5 -b 0.0.0.0:5000 app:app &
                    """
                }
            }
        }
    }
    post {
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
