pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Stage1') {
      steps {
        sh '''# Build new image and push to ACR.
WEB_IMAGE_NAME="${ACR_LOGINSERVER}/azure-vote-front:kube${BUILD_NUMBER}"
docker build -t $WEB_IMAGE_NAME ./azure-vote
docker login ${ACR_LOGINSERVER} -u ${AZURE_CLIENT_ID} -p ${AZURE_CLIENT_SECRET}
docker push $WEB_IMAGE_NAME'''
      }
    }
    stage('Stage2') {
      steps {
        acsDeploy(azureCredentialsId: 'msi_2', resourceGroupName: 'seusher_boulder_upskill', containerService: 'cseboulderupskill', configFilePaths: 'azure-vote-all-in-one-redis.yaml', sshCredentialsId: 'jenkins')
      }
    }
  }
}