resource "aws_iam_role" "role" {
  count = var.external_secret_type == "eso" && var.external_secret_eso_kind == "SecretStore" ? 1 : 0
  name  = "${local.app_name}-${local.k8s_cluster_name}-ss"
  tags  = var.tags

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "${var.k8s_oidc_provider_arn}"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringLike": {
          "${replace(var.k8s_cluster_oidc_issuer_url, "https://", "")}:sub": "system:serviceaccount:${local.namespace}:${local.app_name}-secret-store-sa"
        }
      }
    }
  ]
}
EOF
}

locals {
  resources = join("\", \"", formatlist("arn:aws:secretsmanager:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:secret:%s", tolist(["${var.github_sso_secret_name}*","${var.github_ssh_key_secret_name}*"])))
}

resource "aws_iam_role_policy" "role_access" {
  count = var.external_secret_type == "eso" && var.external_secret_eso_kind == "SecretStore" ? 1 : 0
  name  = "${local.app_name}-${local.k8s_cluster_name}-ss-access"
  role  = aws_iam_role.role[0].id

  policy = <<-EOF
{
  "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SecretsAccess",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:ListSecretVersionIds",
                "secretsmanager:GetSecretValue",
                "secretsmanager:GetResourcePolicy",
                "secretsmanager:DescribeSecret"
            ],
            "Resource": [
                "${local.resources}"
            ]
        },
        {
            "Sid": "RoleAssume",
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "${aws_iam_role.role[0].arn}"
        }
    ]
}
  EOF
}
