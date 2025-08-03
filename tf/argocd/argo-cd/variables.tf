variable "domain_name" {
  type        = string
  description = "A domain name prefix for ArgoCD installation"
  default     = "argo-cd"
}

variable "argo_version" {
  default     = "v2.2.4"
  description = "Version of the Helm chart"
}

variable "release_name" {
  default     = "argo-cd"
  description = "Release name of the Helm chart"
}

variable "chart_values" {
  default     = ""
  description = "Chart values"
}

variable "github_sso_secret_name" {
  type        = string
  description = "AWS secrets manager name of the secret with two keys - clientSecret and clientID"
  default     = ""
}

variable "aws_region" {
  type        = string
  description = "AWS region of secrets manager to access from external secrets"
  default     = ""
}

variable "dns_zone" {
  type        = string
  description = "DNS zone of the cluster to use in ingress objects"
  default     = "example.com"
}

variable "github_ssh_key_secret_name" {
  type        = string
  description = "AWS Secrets manager's key name with ssh key for github access"
  default     = "/eks/argo-cd/github-ssh-key"
}

variable "k8s_cluster_name" {
  type        = string
  description = "Optional custom cluster name, by default it'll be the name of environment's folder"
  default     = ""
}

variable "app_repo" {
  description = "Repository where cluster specific application manifests are stored."
  default     = "git@github.com:pepsico-ecommerce/k8s-clusters.git"
}

variable "github_org" {
  description = "Org to use for github auth"
  default     = "pepsico-ecommerce"
}

variable "github_teams" {
  description = "Teams to use for github auth and policies."
  default     = ["Operations"]
}

variable "policy" {
  description = "Policy to use for argo-cd access."
  default     = "g, pepsico-ecommerce:Operations, role:admin"
}

variable "system_project" {
  description = "Project to use for system applications."
  default     = "system"
}

variable "app_repo_path" {
  description = "Optional path to use for app repo. Defaults to cluster_name/argo-cd/applications, set in local values."
  default     = ""
}

variable "system_repo_path" {
  description = "Optional path to use for system repo. Defaults to terraform/environments/cluster_name/k8s/app_name/applications"
  default     = ""
}

variable "system_repo" {
  description = "Repository where cluster specific application manifests are stored."
  default     = "git@github.com:pepsico-ecommerce/ops-core.git"
}

variable "additional_repositories" {
  description = "Additional repositories to add beyond system and app. Application files will not be created for these."
  default     = []
}

variable "additional_credentials" {
  description = "Additional credentials to use. Will always have github ssh key configured."
  default     = ""
}

variable "create_ingress" {
  description = "Pass false to disable creation of ingress."
  default     = true
}

variable "create_ext_ingress" {
  description = "Pass true to create ingress for external integrations"
  default     = false
}

variable "webhook_repo_list" {
  description = "List of repositories to add a webhook for."
  default     = ""
}

variable "webhook_github_secret" {
  description = "Optional password to use for github webhook, will default to random password."
  default     = ""
}

variable "additional_apps" {
  description = "Optional list of additional applications to install beyond system and cluster applications."
  default     = ""
}

variable "additional_projects" {
  description = "Optional list of projects to create."
  default     = ""
}

variable "finalizers" {
  description = "List of optional finalizers for applications create by this module specifically."
  default     = ""
}

variable "cloudflare_proxy" {
  description = "Pass any non blank value to set external-dns.alpha.kubernetes.io/cloudflare-proxied: true for argo-cd ingress."
  default     = ""
}

variable "cloudflare_solver" {
  description = "Pass true to use use-cloudflare-solver: true for argo-cd int ingress."
  default     = false
  type        = bool
}

variable "custom_tools" {
  description = "Pass the list of additional tools for ArgoCD"
  default     = []
  type        = list(string)
}

variable "cluster_apps_recurse" {
  description = "Pass false to disable spec/source/directory/recursive option"
  default     = true
}

variable "cluster_sysapps_recurse" {
  description = "Pass false to disable spec/source/directory/recursive option"
  default     = true
}

variable "ingress_whitelist" {
  description = "external nginx ingress whitelist"
  default     = []
  type        = list
}
variable "ingress_version" {
  description = "for new syntax, set v1, for other values, old syntax would be used"
  default     = "v1"
  type        = string
}

variable "external_secret_type" {
  description = "ESO used by default, set 'kes' to switch on original type"
  default     = "eso"
  type        = string
}

variable "external_secret_eso_kind" {
  description = "Set SecretStore to create own irsa for new SecretStore if eso type used"
  default     = "SecretStore"
  type        = string
}

variable "external_secret_eso_kind_name" {
  description = "Leave default if not using SecretStore if eso type used"
  default     = "argo-cd-secrets-store"
  type        = string
}

variable "k8s_cluster_oidc_issuer_url" {
  type        = string
  description = "cluster_oidc_issuer_url output of Kubernetes module"
  default     = ""
}

variable "k8s_oidc_provider_arn" {
  type        = string
  description = "oidc_provider_arn output of Kubernetes module"
  default     = ""
}

variable "resources" {
  default     = {}
  description = "custom resource specification for argocd services"
}

variable "tags" {
  default = {}
}

variable "cloud_provider" {
  type        = string
  description = "Which cloud provider we will be working on."
  default     = "aws"
}

variable "new_k8s_path" {
  type        = bool
  description = "If true template files will output to k8s/provider/region instead of just k8s."
  default     = false
}
