# Keycloak

## Prerequisites

Put some information here about generating the realm.json secret in AWS Secrets Manager

## Installation

Ensure you have executed `gimme-aws-credentials` and are mapped to the appropriate role and account.

Ideally, the following would be executed as part of a Github Action or similar.

```bash
cd regtech-user-fi-management/k8s/keycloak

# let's add the chart repository and determine the latest version
helm repo add bitnami https://charts.bitnami.com/bitnami
helm search repo bitnami | grep keycloak
# helm search repo bitnami | grep keycloak
# bitnami/keycloak     	16.1.5       	22.0.3       	Keycloak is a high performance Java-based ident...

helm upgrade \
  --install keycloak bitnami/keycloak \
  --version 16.1.5 \
  --values values.yaml \
  --namespace regtech
```
