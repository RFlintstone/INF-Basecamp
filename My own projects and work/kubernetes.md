## Learning Kubernetes

**Author:** Ruben Flinterman

As an hobby and as of 20-11-23 also for work (datalab) I research Kubernetes and try to get it working for a production environment where it needs to be able to scale easily, on a bare-metal server.

Although kubernetes is not a programming language it does provide a few things regarding experience which could be important for a developer (with an eye for writing safe software):
1) How you can both easily and safely configure services, so it won't give any issues on long term (IP, ports, subnets)
2) It gives you a general understanding of networking
3) It gives you a general understanding of yaml and bash scripts
4) It forces you to properly think-out your infrastructure. Ex: Do you want a database next to your web application? Do they need to run on the same cluster, and if so, do they need to be in the same pod?