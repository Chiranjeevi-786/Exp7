Codeshare logo
 ShareSign UpLog In

1
pipeline {
2
    agent any
3
​
4
    stages {
5
        stage('Checkout Source Code') {
6
            steps {
7
                echo 'Pulling code from Git repository...'
8
                checkout scm
9
            }
10
        }
11
​
12
        stage('Build & Execute Script') {
13
            steps {
14
                echo 'Running first.py...'
15
                bat 'python first.py'
16
            }
17
        }
18
​
19
        stage('Code Stability Check') {
20
            steps {
21
                echo 'Verifying pipeline execution...'
22
                bat 'echo "Python script executed successfully!"'
23
            }
24
        }
25
    }
26
​
27
    post {
28
        success {
29
            echo 'SUCCESS: CI Pipeline completed successfully!'
30
        }
31
        failure {
32
            echo 'FAILURE: Pipeline failed. Check build logs.'
33
        }
34
    }
35
}




Google Cloud
Code using any language, framework, and library. Package it as a container and deploy.
px
Hide Ads
