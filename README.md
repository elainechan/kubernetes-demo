# Kubernetes Demo

## Create Pod
- run container inside a pod with exposed port
- run container inside a pod without exposed port

## Communicate with a container
- with exposed port
- without exposed port

## Use cases
1. App that needs a container without exposed port
    - build and run a container
    - run app
    - delete container

2. App that needs a container with an exposed port
    - build and run a container
    - run the app
    - when user saves and exits, delete container 

## Kubernetes Notes

### Networking
- Docker Host-private Networking
- Containers can talk to other containers only if they are on the same machine.
- In order for Docker containers to communicate across Nodes:
- There must be allocated ports on the machine’s own IP address
- Ports are then forwarded or proxied to the containers. 
- Containers must either:
- Coordinate which ports they use very carefully OR
- Ports must be allocated dynamically.

### Kubernetes Networking
- Assumes that Pods can communicate with other Pods, regardless of which host they land on.
- Gives every Pod its own cluster-private IP address ClusterIP.
- you do not need to explicitly create links between Pods or map container ports to host ports. 
- containers within a Pod can all reach each other’s ports on localhost
- All Pods in a Cluster can see each other without NAT.
- the IP that a Pod sees itself as is the same IP that others see it as.

#### References
- https://kubernetes.io/docs/concepts/cluster-administration/networking/
- https://sookocheff.com/post/kubernetes/understanding-kubernetes-networking-model/

### Ports

`port`
- “Inside the Cluster, what port does the Service expose?”
- Exposes the Service on the specified port internally within the Cluster.
- The Service becomes visible on this port, and will send requests made to this port to the Pods selected by the Service.

`targetPort`
- “Which port do Pods selected by this Service expose?”
- If you hit the port from inside the cluster, your request will be routed to the Pods via the targetPort.

`nodePort`
- “Which port on the node makes the service available to the outside world?”
- A Service uses nodePort to expose pods for external traffic.
- Makes the service visible outside the Kubernetes cluster by the node’s IP address and the port number declared in this property.
- Exposes the service on each Node’s IP via the defined static port.
- No matter which Node within the Cluster is accessed, the service will be reachable based on the port number defined.
- If this field isn’t specified, Kubernetes will allocate a node port automatically.

`clusterIP`
- Makes a Service available inside the Cluster
- The default approach when creating a Kubernetes Service.
- The Service is allocated an internal IP that other components can use to access the pods.
- Having a single IP address enables the Service to be load-balanced across multiple Pods.

#### References
- https://medium.com/@deepeshtripathi/all-about-kubernetes-port-types-nodeport-targetport-port-containerport-e9f447330b19
- https://stackoverflow.com/questions/49981601/difference-between-targetport-and-port-in-kubernetes-service-definition
- Get YAML for Kubernetes Objects: https://stackoverflow.com/questions/43941772/get-yaml-for-deployed-kubernetes-services
