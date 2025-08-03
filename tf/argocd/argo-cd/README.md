```
module "argo-cd" {
  source                  = "git@github.com:pepsico-ecommerce/ops-tf-module-argo-cd.git?ref=v1.3.0"
  dns_zone                = var.dns_zone
  github_sso_secret_name  = "/eks/${var.cluster_name}/github-sso-secret"
  policy                  = var.argo_cd_oauth_rbac_config_policy # Optional
  github_teams            = var.argo_cd_oauth_github_teams # Optional
  additional_repositories = var.argo_additional_repos # Optional
  webhook_repo_list       = var.argo_cd_webhooks_repo_list # Optional
}
```

The github secret must already exist, it is not auto created and is required for github authentication.

All other variables are optional. Please look at variables.tf for values that can be passed, as well as the default values already defined.


Examples for some of the additional variables can be found below.
```
argo_cd_oauth_rbac_config_policy = <<EOF
p, role:sync, applications, get, */*, allow
p, role:sync, applications, sync, default/*, allow
p, role:sync, certificates, get, *, allow
p, role:sync, clusters, get, *, allow
p, role:sync, repositories, get, *, allow
p, role:sync, projects, get, *, allow
p, role:sync, accounts, get, *, allow
g, pepsico-ecommerce:Operations, role:admin
g, pepsico-ecommerce:Data Engineering, role:sync
EOF

argo_cd_oauth_github_teams                = ["Operations", "Data Engineering"]
argo_additional_repos = [
  { "name" : "k8s-airflow", "value" : "git@github.com:pepsico-ecommerce/k8s-airflow.git" },
]

argo_cd_webhooks_repo_list = [
  "k8s-airflow",
  "k8s-config"
]

argo_additional_applications = [
  { "name" : "pr-envs", "repoURL" : "git@github.com:pepsico-ecommerce/k8s-config.git", "project" : "pr-envs", "path" : "argocd/applications/overlays/pr/apps", "targetRevision" : "master", "recurse": "true" }

argo_additional_projects = [
  "pr-envs"
]
```
## Specify custom resources
Default resources that would be committed for Argo CD services
```
{
  argocd_server = {
    limits = { cpu = "200m", memory = "256Mi" },
    requests = { cpu = "50m", memory = "64Mi" }
  },
  dex = {
    limits = { cpu = "50m", memory = "64Mi" },
    requests = { cpu = "10m", memory = "32Mi" }
  },
  redis = {
    limits = { cpu = "200m", memory = "128Mi" },
    requests = { cpu = "100m", memory = "64Mi" }
  },
  repo_server = {
    limits = { cpu = "1", memory = "1024Mi" },
    requests = { cpu = "50m", memory = "128Mi" }
  },
  controller = {
    limits = { cpu = "1", memory = "1Gi" },
    requests = { cpu = "250m", memory = "256Mi" }
  }
}
```
You can optionally customize any of these defaults by providing `resource` object parameter.
Be sure to provide compelete specification for combinations cpu/memory and limits/requests for the service that you're doing customization. Any missing value would override with `null`.
### Example
```
module "argo-cd" {
  source                 = "git@github.com:pepsico-ecommerce/ops-tf-module-argo-cd.git?ref=v3.0.1"

  resources = {
    controller = {
      limits = { cpu = "2", memory = "2Gi" },
      requests = { cpu = "500m", memory = "512Mi" }
    }
  }
}
```
