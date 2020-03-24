"""
Example using k8s Python client to create a pod:
https://github.com/kubernetes-client/python/blob/master/examples/notebooks/create_pod.ipynb

First, run `kubectl proxy --port 8001`.
If a proxy is not set up, you will get MaxRetryError.
https://stackoverflow.com/questions/55742540/kubernetes-python-client-connection-issue
"""
from kubernetes import config, client


# Configure client to point to proxy
configuration = client.Configuration()
configuration.host="http://127.0.0.1:8001"
v1 = client.CoreV1Api(client.ApiClient(configuration))

# Initiate pod object and container
pod = client.V1Pod()
container = client.V1Container(
    name="chicken",
    image="chicken",
    image_pull_policy="Never"
)

# Define pod details
spec = client.V1PodSpec(containers=[container])
pod.spec = spec
pod.metadata = client.V1ObjectMeta(name="chicken-noodle")

# Create pod
v1.create_namespaced_pod(namespace="default", body=pod)

# Get list of pods after creation
ret = v1.list_namespaced_pod(namespace="default")
for item in ret.items:
    print(
        f"{item.status.pod_ip}\t{item.metadata.namespace}\t{item.metadata.name}"
    )

# Delete pod
# res = v1.delete_namespaced_pod(name="chicken-noodle", namespace="default",
#                                body=client.V1DeleteOptions())
# print(res)

