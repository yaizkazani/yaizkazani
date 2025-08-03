#resource "random_password" "webhook_shared_secret" {
#  count   = var.webhook_repo_list == "" ? 0 : 1
#  length  = 32
#  special = false
#}

#resource "github_repository_webhook" "argocd_webhooks" {
#  count      = length(var.webhook_repo_list)
#  repository = var.webhook_repo_list[count.index]
#
#  configuration {
#    url          = "https://${local.argo_domain}/api/webhook"
#    content_type = "json"
#    insecure_ssl = false
#    secret       = random_password.webhook_shared_secret[0].result
#  }
#
#  active = true
#  events = ["push"]
#}
