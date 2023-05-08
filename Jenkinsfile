pipeline{
 environment {
 registry = "deannec/allthefeels-test"
        registryCredentials = "deannec_dockerhub_id"
        dockerImage = ""
    }
    agent any
        stages {

            stage ('Build Docker Image'){
                steps{
                    script {
                        dockerImage = docker.build(registry)
                    }
                }
            }

            stage ('Run Tests'){
                steps{
                    script {

                        sh '''#!/bin/bash

                            echo 'Running tests...'
                            python3 --version
                            python -m pip --version
                            echo "PATH is: $PATH"


                            python3 -m venv testenv
                            source testenv/bin/activate


                            python -m pip install -r requirements.txt

                            python -m unittest discover tests/db
                            python -m unittest discover tests/dao
                        '''
                    }
                }
            }

            stage ("Push to Docker Hub"){
                steps {
                    script {
                        docker.withRegistry('', registryCredentials) {
                            dockerImage.push("${env.BUILD_NUMBER}")
                            dockerImage.push("latest")
                        }
                    }
                }
            }

            stage ("Clean up"){
                steps {
                    script {
                        sh 'docker image prune --all --force --filter "until=48h"'
                    }
                }
            }
         
         
            stage ("Run container")
            {
                steps {
                    script{
                        echo 'Stopping existing container'
                        sh 'docker stop allTheFeelsWeb'
                        # run new container
                        echo 'Starting new container'
                        dockerImage.run('-name allTheFeelsWeb -p 5000:5000 -d')
                    }
                }
            }
        }
}
