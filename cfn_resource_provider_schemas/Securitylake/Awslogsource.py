SCHEMA = {
  "typeName" : "AWS::SecurityLake::AwsLogSource",
  "description" : "Resource Type definition for AWS::SecurityLake::AwsLogSource",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-securitylake.git",
  "additionalProperties" : False,
  "properties" : {
    "Accounts" : {
      "description" : "AWS account where you want to collect logs from.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string",
        "pattern" : "^[0-9]{12}$"
      }
    },
    "DataLakeArn" : {
      "description" : "The ARN for the data lake.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256
    },
    "SourceName" : {
      "description" : "The name for a AWS source. This must be a Regionally unique value.",
      "type" : "string"
    },
    "SourceVersion" : {
      "description" : "The version for a AWS source. This must be a Regionally unique value.",
      "type" : "string",
      "pattern" : "^(latest|[0-9]\\.[0-9])$"
    }
  },
  "required" : [ "DataLakeArn", "SourceVersion", "SourceName" ],
  "primaryIdentifier" : [ "/properties/SourceName", "/properties/SourceVersion" ],
  "createOnlyProperties" : [ "/properties/DataLakeArn", "/properties/SourceName", "/properties/SourceVersion" ],
  "tagging" : {
    "taggable" : False
  },
  "replacementStrategy" : "delete_then_create",
  "handlers" : {
    "create" : {
      "permissions" : [ "glue:CreateDatabase", "glue:CreateTable", "glue:GetDatabase", "glue:GetTable", "iam:CreateServiceLinkedRole", "kms:CreateGrant", "kms:DescribeKey", "securitylake:CreateDataLake", "securitylake:CreateAwsLogSource", "securitylake:ListLogSources" ]
    },
    "read" : {
      "permissions" : [ "securitylake:ListLogSources" ]
    },
    "list" : {
      "permissions" : [ "securitylake:ListLogSources" ]
    },
    "delete" : {
      "permissions" : [ "securitylake:DeleteAwsLogSource", "securitylake:ListLogSources" ]
    },
    "update" : {
      "permissions" : [ "securitylake:CreateAwsLogSource", "securitylake:DeleteAwsLogSource", "glue:CreateDatabase", "glue:CreateTable", "glue:GetDatabase", "glue:GetTable", "iam:CreateServiceLinkedRole", "kms:CreateGrant", "kms:DescribeKey" ]
    }
  }
}