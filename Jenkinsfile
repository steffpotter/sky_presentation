pipeline{
 environment {
 registry = "deannec/allthefeels-test"
        registryCredentials = "deannec_dockerhub_id"
        dockerImage = ""
    }
    agent any
        stages {

            stage ('Run Tests'){
                steps{
                    script {

                        sh '''#!/bin/bash

                            export WORKSPACE=`pwd`

                            virtualenv testenv -p /usr/bin/python3

                            source testenv/bin/activate

                            echo 'Running tests...'

                            pip install -r requirements.txt

                            python -m unittest discover tests/db
                            python -m unittest discover tests/dao
                        '''
                    }
                }
            }

            stage ('Build Docker Image'){
                steps{
                    script {
                        dockerImage = docker.build(registry)
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
                        dockerImage.run('-p 6000:6000 -d')
                    }
                }
            }
        }
}
