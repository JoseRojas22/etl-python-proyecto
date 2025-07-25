pipeline {
    agent any

    stages {
        stage('Clonar repositorio') {
            steps {
                git branch: 'develop', url: 'https://github.com/JoseRojas22/etl-python-proyecto.git'
            }
        }

        stage('Ejecutar ETL') {
            steps {
                sh 'python lectura.py'
            }
        }
    }
}
