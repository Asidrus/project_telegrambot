properties([disableConcurrentBuilds()])

pipeline {
    agent {
        label 'jenkins_host'
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
    }
    environment {
        WEBSITE_IP="37.140.198.248"
        WEBSITE_PORT=80
        TELEGRAMBOT_PORT=8081
    }
    stages {
        stage('git clone') {
            steps {
                git branch: "master", url: 'git@github.com:Asidrus/project_telegrambot.git', credentialsId: 'Github_ssh'
            }
        }
        stage('docker-compose up'){
            steps {
                withCredentials([string(credentialsId: 'API_TOKEN', variable: 'API_TOKEN')]) {
                    sh """
                    echo "API_TOKEN=$API_TOKEN" > .env
                    echo "WEBSITE_IP=$WEBSITE_IP" >> .env
                    echo "WEBSITE_PORT=$WEBSITE_PORT" >> .env
                    """
                }
                sh "docker-compose up -d --build"
            }
        }
    }
}
