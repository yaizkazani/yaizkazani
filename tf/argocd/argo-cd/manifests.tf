# Initial manifests files, used for cluster bootstrap
# DO NOT move this manifests to already existing cluster, since there might be more recent manifests

module "template_files" {
  source = "apparentlymart/dir/template"

  base_dir             = "${path.module}/k8s"
  template_file_suffix = ".yaml"
  template_vars = {
    # Pass in any values that you wish to use in your templates.
    github_sso_secret_name     = var.github_sso_secret_name
    github_ssh_key_secret_name = var.github_ssh_key_secret_name
    cluster_name               = local.k8s_cluster_name
    aws_region                 = local.aws_region
    dns_zone                   = var.dns_zone
    app_name                   = local.app_name
    domain_name                = var.domain_name
    app_repo                   = var.app_repo
    github_org                 = var.github_org
    github_teams               = jsonencode(var.github_teams)
    policy                     = indent(4, var.policy)
    system_project             = var.system_project
    app_repo_path              = local.app_repo_path
    argo_version               = var.argo_version
    system_repo                = var.system_repo
    system_repo_path           = local.system_repo_path
    additional_repositories    = var.additional_repositories
    additional_credentials     = indent(6, var.additional_credentials)
    create_ingress             = var.create_ingress
    create_ext_ingress         = var.create_ext_ingress
    webhook_repo_list          = var.webhook_repo_list
    additional_apps            = var.additional_apps
    additional_projects        = var.additional_projects
    finalizers                 = var.finalizers
    cloudflare_proxy           = var.cloudflare_proxy
    cloudflare_solver          = var.cloudflare_solver
    custom_tools               = var.custom_tools
    cluster_apps_recurse       = var.cluster_apps_recurse
    cluster_sysapps_recurse    = var.cluster_sysapps_recurse
    ingress_whitelist          = join(",",var.ingress_whitelist)
    ingress_version            = var.ingress_version

    # ESO vars
    external_secret_type          = var.external_secret_type
    external_secret_eso_kind      = var.external_secret_eso_kind
    external_secret_eso_kind_name = var.external_secret_eso_kind_name
    namespace                     = local.namespace
    external_secret_aws_role      = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:role/${local.app_name}-${local.k8s_cluster_name}-ss"

    resources = local.resources_merged
  }
}

resource "local_file" "k8s" {
  for_each             = module.template_files.files
  content              = each.value.content
  file_permission      = "0644"
  directory_permission = "0755"
  filename             = "${path.cwd}/${local.k8s_path}/${local.namespace}/${each.key}.yaml"
}

resource "local_file" "values" {
  count = var.webhook_repo_list == "" ? 0 : 1
  content = templatefile("${path.module}/k8s-override/${local.namespace}/argo-cd-server-secret.yaml",
    {
      webhook_github_secret = base64encode(var.webhook_github_secret)
  })
  file_permission      = "0644"
  directory_permission = "0755"
  filename             = "${path.cwd}/${local.k8s_path}/${local.namespace}/${local.namespace}/argo-cd-server-secret.yaml"
}

resource "local_file" "apps" {
  count = var.additional_apps == "" ? 0 : 1
  content = templatefile("${path.module}/k8s-override/${local.namespace}/argo-cd-additional-applications.yaml",
    {
      additional_apps = var.additional_apps
      app_name        = local.app_name
      finalizers      = var.finalizers
  })
  file_permission      = "0644"
  directory_permission = "0755"
  filename             = "${path.cwd}/${local.k8s_path}/${local.namespace}/${local.namespace}/argo-cd-additional-applications.yaml"
}

resource "local_file" "projects" {
  count = var.additional_projects == "" ? 0 : 1
  content = templatefile("${path.module}/k8s-override/${local.namespace}/argo-cd-additional-projects.yaml",
    {
      additional_projects = var.additional_projects
      app_name            = local.app_name
  })
  file_permission      = "0644"
  directory_permission = "0755"
  filename             = "${path.cwd}/${local.k8s_path}/${local.namespace}/${local.namespace}/argo-cd-additional-projects.yaml"
}
