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
                        sh '''#!/bin/bash

                                if ! sudo service docker status | grep -q "running"; then
                                  echo "Docker is not running. Starting Docker service..."
                                  sudo service docker start
                                else
                                  echo "Docker is already running."
                                fi
                            '''
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
                        sh '''#!/bin/bash

                            container_name="allTheFeelsWeb"
                            use_mock="True"
                            if docker inspect "$container_name" >/dev/null 2>&1; then
                                echo "container exists"
                                echo "Existing container found, stopping existing container"
                                docker stop "$container_name"
                                docker rm "$container_name"
                            fi

                            echo "Starting new container"
                            docker run -d -p 5000:5000 -e USEMOCK=$use_mock --name "$container_name"  deannec/allthefeels-test

                        '''
                    }
                }
            }
        }
}
