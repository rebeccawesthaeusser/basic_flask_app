node{
    stage('SCM Checkout'){
        git credentialsId: 'git-credits', url: 'https://swinfrastructure.iao.fraunhofer.de/gitlab/westhaeu/basic-flask-app'
    }
    stage('Mvn Package'){
        tool name: 'maven-3', type: 'maven'
    }
    stage('Build Docker Image'){
        bat label: '', script: 'docker build -t rw044/flask_tutorial:latest .'
    }
    stage('Push Docker Image'){
        withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerHubPwd')]) {
            bat label: '', script: "docker login -u rw044 -p ${dockerHubPwd}"
        }
        bat label: '', script: 'docker push rw044/flask_tutorial'
    }
}