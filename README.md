# Trabalho Prático 2 - Computação em nuvem

## Executando o Docker
Para montar e executar os contâineres Docker, execute o comando abaixo: 
```
./start.sh
``` 

## Executando o Kubernetes 
Para criar os pods do Kubernetes, execute a seguinte sequência de comandos: 
```
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```
Para verificar se a aplicação foi criada com sucesso, faça a seguinte chamada: 
```
wget --server-response \
    --output-document response.out \
    --header='Content-Type: application/json' \
    --post-data '{"songs": ["Yesterday", "Bohemian Rhapsody"]}' \
    http://<meu-ip>:30049/api/recommender
```
Onde `<meu-ip>` é o endereço IP da sua máquina host