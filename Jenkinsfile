pipeline {
    agent {
        docker {
            image 'python:3.5.1'
        }
    }

    stages {
        stage('build') {
            steps {
                sh 'python -m py_compile demo_1.py'
                stash(name: "compiled-results", includes: '*.py*')
            }
        }
    }
}