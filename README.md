# Zero Trust Kubernetes Demo (Cilium + Hubble)

This project demonstrates a **Zero Trust security model in Kubernetes**, showing how lateral movement between services can be blocked using **Cilium Network Policies** and observed in real time with **Hubble**.

---

## 🧰 Prerequisites

Install the following tools on macOS:

- Docker Desktop  
  https://docs.docker.com/desktop/setup/install/mac-install/

- kind (Kubernetes in Docker)
    ```sh
    brew install kind
    ```

- kubectl (Kubernetes CLI)
    ```sh
    brew install kubectl
    ```

- Cilium CLI  
  https://docs.cilium.io/en/stable/gettingstarted/k8s-install-default/

---

## 🚀 Demo Overview

Services:
- frontend → UI + simulated attack entry point
- backend → jokes API
- clientapi → business logic API
- clientdb → data store

---

## ▶️ Run Demo

### 1. Baseline (no Cilium)

```sh
./1-docker-build.sh
./2-deploy.sh
./3-expose.sh
```

Attack test:

```sh
cat ./4-attack-commands.sh
```

Cleanup:

```sh
./9-cleanup.sh
```

---

### 2. Secure scenario (Cilium + Hubble)

Deploy:

```sh
./2-deploy-cilium.sh
```

Expose:

```sh
./3-expose.sh
./3-expose-hubble.sh
```

Observe traffic:

```sh
cat ./4-attack-commands.sh
```

---

### Apply Zero Trust policies

```sh
./5-netpol.sh
```

Re-test attack:

```sh
cat ./4-attack-commands.sh
```

---

## 🧹 Cleanup

```sh
./9-cleanup.sh
```
