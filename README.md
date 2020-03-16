<h3>This will provide prometheus custom metrics using python code base to call API's and build using docker image rajeshcse515/custome_metrics_pro and setup a kuberneted pod.</h3>


<b>Key folders</b>

src/app.py - Python application to expose custom prometheus metrics.

requirements.txt - Moduled to be installed.

Dockerfile - Docker file to build the application

kubernetes/deployment.yml - Create a deployment in kubernetes

kubernetes/service.yml - Nodeport setup service

unitTests/test_app.py - Unit test cases, more can be added and customized. 

<b>Project setup and configuration:</b>

git clone https://github.com/rkondra1/python_api_prometheus_k8.git

kubectl apply -f kubernetes/deployment.yml
kubectl apply -f kubernetes/service.yml

<b>Verify if the pod is up and runnning</b>

Eg: 

kubectl get pods --namespace=default
NAME                                READY   STATUS    RESTARTS   AGE
app-deployment-7d8b658686-vhpck     1/1     Running   0          7h8m

<b>To access the service :</b>

http://<HOST IP>:30000/metrics


<b>Unit Tests:</b>

To run the unit tests 

python -m unittest unitTests/unit_test.py

![Output from app.py](https://github.com/rkondra1/python_api_prometheus_k8/blob/master/code_output.png)
![Metrics from prometheus](https://github.com/rkondra1/python_api_prometheus_k8/blob/master/image_metrics_prometheus.png)

