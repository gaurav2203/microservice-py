pipeline {
    agent any

    stages {
        stage('clean workspace'){
            steps{
                cleanWs()
            }
        }
        stage('whoami'){
            steps{
                sh "whoami"
                sh "id"
            }
        }
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
        stage('checkout from github'){
            steps{
                git branch: 'v2', url: 'https://github.com/gaurav2203/microservice-py.git'
            }
        }
        stage('docker build'){
            steps{
                script{
                    withDockerRegistry(credentialsId: 'docker', toolName: 'docker'){
                        sh "docker build -t gaurav2203/microservice-frontend:v2.2 ./frontend/"
                        sh "docker push gaurav2203/microservice-frontend:v2.2"
                    }
                }
            }
        }
        stage('kubernetes deployment'){
            steps{
                script{
                    dir('k8s'){
                        withKubeConfig(caCertificate: '', clusterName: '', contextName: '', credentialsId: 'k8s', namespace: '', restrictKubeConfigAccess: false, serverUrl: ''){
                            sh "kubectl apply -f ."
                        }
                    }
                }
            }
        }
    }
}

