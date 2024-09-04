pipeline {
    agent any

    parameters {
        choice(name: 'FORCE_INSTALL_COMPOSER', choices: ['No', 'Yes'], description: 'Do you need to install composer dependencies?')
        choice(name: 'FORCE_COMPOSER_DUMP_AUTOLOAD', choices: ['No', 'Yes'], description: 'Do you need to run composer dump-autoload?')
    }

    environment {
        GIT_CREDENTIALS_JENKINS = "jenkins-server-sapi"
        GIT_URL_DEV         = "git@github.com:sqiva-sistem/sa-frontend.git"
        GIT_URL_DEV_BUILD   = "git@github.com:sqiva-sistem/sa-frontend-build.git"
        GIT_BRANCH          = "master"
        EMAIL_TO            = "jadid.ramadhan@sqiva.com"
    }

    // checkout from sa-frontend repo branch dev
    stages {
        stage("Checkout sa-frontend branch dev") {
            steps {
                sh "mkdir -p sa-frontend-dev"
                dir("sa-frontend-dev") {
                    git credentialsId: "${GIT_CREDENTIALS_JENKINS}",
                        branch: "${GIT_BRANCH}",
                            url: "${GIT_URL_DEV}"
                }
            }
        }

        stage("Install Composer Dependencies") {
            steps {
                dir("sa-frontend-dev") {
                    script {
                        // check install composer or not
                        if (params.FORCE_INSTALL_COMPOSER == 'Yes') {
                            echo "user choose to install composer, installing composer base on composer.json"

                            //sh 'composer install --ignore-platform-reqs --no-dev'
                        } else {
                            echo "user choose to skip composer install."
                        }

                        // run composer dump-autoload or not
                        if (params.FORCE_COMPOSER_DUMP_AUTOLOAD == 'Yes') {
                            echo "user choose to run composer dump-autoload, running base on composer.json"
                            
                            // prevent double run composer install
                            if (params.FORCE_INSTALL_COMPOSER == "No") {
                                //sh 'composer install --ignore-platform-reqs --no-dev'
                            }

                            //sh 'composer dump-autoload'
                        } else {
                            echo "user choose to skip run composer dump-autoload"
                        }

                        //sh "rm -rf .git"
                    }
                }
            }
        }

        stage("Checkout sa-frontend build branch dev") {
            steps {
                sh 'mkdir -p sa-frontend-dev-build'
                /*dir("sa-frontend-dev-build") {
                    git credentialsId: "${GIT_CREDENTIALS_JENKINS}",
                        branch: "${GIT_BRANCH}",
                            url: "${GIT_URL_DEV_BUILD}"

                }*/
            }
        }

        stage("Prepare and Push build to sa-frontend-build branch dev") {
            steps {
                /*dir("sa-frontend-dev-build") {
                    script {
                        // sh "git checkout -f ${GIT_BRANCH}"

                        // copy all build deploy to build dev folder
                        sh "yes | sudo cp -R -p ../sa-frontend-dev/* ."
                        
                        // copy .gitignore .env to build folder
                        // sh "yes | cp -p ../sa-frontend-dev-env/dev/.gitignore ."
                        sh "yes | cp -p ../sa-frontend-env/dev/.env ."

                        gitStatus = sh(returnStdout: true, script: 'git status --porcelain')
                        
                        if (gitStatus.trim().isEmpty()) {
                            echo 'No new changes detected.'
                        } else {
                            sh "git status"
                            sh 'git add .'
                            sh "git commit -m 'update dev to latest change by ${BUILD_USER}'"
                            sh "git push origin ${GIT_BRANCH}"
                        }
                    }
                }*/
            }
        }

        stage("sync to dev server") {
            steps {
                // rsync into dev server
                /*
                sh "sudo chown dockernet:sqiva -R /var/lib/jenkins/workspace/sa-portal/sa-frontend/deploy-to-dev/sa-frontend-dev-build"
                sh "sudo chmod 775 -R /var/lib/jenkins/workspace/sa-portal/sa-frontend/deploy-to-dev/sa-frontend-dev-build"
                sh "sudo chmod +x -R /var/lib/jenkins/workspace/sa-portal/sa-frontend/deploy-to-dev/rsync-script-sa-frontend"
                sh "sudo /var/lib/jenkins/workspace/sa-portal/sa-frontend/deploy-to-dev/rsync-script-sa-frontend/rsync-launcher-dev"
                */
            }
        }
    }

    post {
        always {
            emailext to: "${BUILD_USER_EMAIL},${EMAIL_TO}",
            subject: "Build:${currentBuild.currentResult}: ${env.JOB_NAME}",
            body: "${currentBuild.currentResult}: Job ${env.JOB_NAME}\nMore Info can be found here: ${env.BUILD_URL}"
        }
    }
}
