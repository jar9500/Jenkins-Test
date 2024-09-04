pipeline {
    agent any

    parameters {
        choice(name: 'FORCE_INSTALL', choices: ['No', 'Yes'], description: 'Do you need to install composer dependencies?')
        choice(name: 'FORCE_AUTOLOAD', choices: ['No', 'Yes'], description: 'Do you need to run composer dump-autoload?')
    }

    environment {
        GIT_URL             = "https://github.com/jar9500/Final-Project-TSA-NP.git"
        GIT_BRANCH          = "master"
        GIT_CREDENTIALS_JENKINS = "Ubuntu-Server"
        EMAIL_TO            = "jadid.ramadhan@sqiva.com"
    }

    // checkout from sa-frontend repo branch dev
    stages {
        stage("Checkout Test Project") {
            steps {
                sh "mkdir -p Test-Project"
                dir("Test-Project") {
                    git credentialsId: "${GIT_CREDENTIALS_JENKINS}",
                        branch: "${GIT_BRANCH}",
                            url: "${GIT_URL_DEV}"
                }
            }
        }

        stage("Install Test-Project") {
            steps {
                dir("Test-Project") {
                    script {
                        // check install composer or not
                        if (params.FORCE_INSTALL == 'Yes') {
                            echo "user choose to install , installing..."

                            //sh 'composer install --ignore-platform-reqs --no-dev'
                        } else {
                            echo "user choose to skip install."
                        }

                        // run composer dump-autoload or not
                        if (params.FORCE_AUTOLOAD == 'Yes') {
                            echo "user choose to run autoload"
                            
                            // prevent double run composer install
                            if (params.FORCE_INSTALL == "No") {
                                //sh 'composer install --ignore-platform-reqs --no-dev'
                            }

                            //sh 'composer dump-autoload'
                        } else {
                            echo "user choose to skip run autoload"
                        }

                        //sh "rm -rf .git"
                    }
                }
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
