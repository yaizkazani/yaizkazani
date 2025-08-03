locals {
  app_name              = "argo-cd"
  namespace             = "argo-cd"
  k8s_path              = var.new_k8s_path == true ? "k8s/${var.cloud_provider}/${local.k8s_cluster_name}" : "k8s"
  k8s_cluster_name      = var.k8s_cluster_name == "" ? basename(path.cwd) : var.k8s_cluster_name
  app_repo_path         = var.app_repo_path == "" ? "${local.k8s_cluster_name}/argo-cd/applications" : var.app_repo_path
  system_repo_path      = var.system_repo_path == "" ? "terraform/environments/${local.k8s_cluster_name}/${local.k8s_path}/${local.app_name}" : var.system_repo_path
  aws_region            = var.aws_region == "" ? data.aws_region.current.name : var.aws_region
  #webhook_github_secret = length(random_password.webhook_shared_secret) > 0 ? random_password.webhook_shared_secret[0].result : var.webhook_github_secret

  resources_default = {
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

  resources_merged = "${merge(local.resources_default,var.resources)}"
}
