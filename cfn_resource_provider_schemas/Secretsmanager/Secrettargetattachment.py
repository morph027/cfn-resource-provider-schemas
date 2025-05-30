SCHEMA = {
  "typeName" : "AWS::SecretsManager::SecretTargetAttachment",
  "$schema" : "https://raw.githubusercontent.com/aws-cloudformation/cloudformation-resource-schema/blob/master/src/main/resources/schema/provider.definition.schema.v1.json",
  "description" : "Resource Type definition for AWS::SecretsManager::SecretTargetAttachment",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "SecretId" : {
      "type" : "string"
    },
    "TargetType" : {
      "type" : "string"
    },
    "TargetId" : {
      "type" : "string"
    }
  },
  "required" : [ "TargetType", "TargetId", "SecretId" ],
  "tagging" : {
    "taggable" : False
  },
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/SecretId" ],
  "handlers" : {
    "read" : {
      "permissions" : [ "secretsmanager:GetSecretValue" ]
    },
    "list" : {
      "permissions" : [ "secretsmanager:GetSecretValue", "secretsmanager:ListSecrets" ]
    },
    "create" : {
      "permissions" : [ "secretsmanager:GetSecretValue", "secretsmanager:PutSecretValue", "rds:DescribeDBInstances", "redshift:DescribeClusters", "rds:DescribeDBClusters", "docdb-elastic:GetCluster", "redshift-serverless:ListWorkgroups", "redshift-serverless:GetNamespace" ]
    },
    "delete" : {
      "permissions" : [ "secretsmanager:GetSecretValue", "secretsmanager:PutSecretValue" ]
    },
    "update" : {
      "permissions" : [ "secretsmanager:GetSecretValue", "secretsmanager:PutSecretValue", "rds:DescribeDBInstances", "redshift:DescribeClusters", "rds:DescribeDBClusters", "docdb-elastic:GetCluster", "redshift-serverless:ListWorkgroups", "redshift-serverless:GetNamespace" ]
    }
  }
}