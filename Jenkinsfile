pipeline {
    agent {
        docker {
            label 'ec2-fleet'
            image 'python:3.13'
            reuseNode true
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Pip install') {
            steps {
                script {
                    sh '''
                        python -m venv venv
                        . venv/bin/activate
                        pip install -r requirements-dev.txt
                    '''
                    stash includes: 'venv/**', name: 'venv'
                }
            }
        }
        stage('Parallel Tasks') {
            parallel {
                stage('UnitTest') {
                    steps {
                        unstash 'venv'
                        script {
                            sh '''
                                . venv/bin/activate
                                python -m coverage run -m unittest discover -s tests
                                python -m coverage report --fail-under=100
                            '''
                        }
                    }
                }
                stage('pytest') {
                    steps {
                        unstash 'venv'
                        script {
                            sh '''
                                . venv/bin/activate
                                python -m coverage run -m pytest --junitxml=pytest-results.xml
                                coverage xml -o coverage.xml
                                python -m coverage report --fail-under=100
                            '''
                        }
                    }
                    post {
                        always {
                            junit 'pytest-results.xml'
                            cobertura coberturaReportFile: 'coverage.xml'
                        }
                    }
                }
                stage('Lint') {
                    steps {
                        unstash 'venv'
                        script {
                            sh '''
                                . venv/bin/activate
                                ruff check . --config pyproject.toml
                            '''
                        }
                    }
                }
                stage('Formatting') {
                    steps {
                        unstash 'venv'
                        script {
                            sh '''
                                . venv/bin/activate
                                black --check .
                            '''
                        }
                    }
                }
                stage('Type Checking') {
                    steps {
                        unstash 'venv'
                        script {
                            sh '''
                                . venv/bin/activate
                                mypy application_name
                            '''
                        }
                    }
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'dist/*', allowEmptyArchive: true
        }
    }
}
