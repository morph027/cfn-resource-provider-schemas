SCHEMA = {
  "typeName" : "AWS::MSK::BatchScramSecret",
  "description" : "Resource Type definition for AWS::MSK::BatchScramSecret",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-msk",
  "definitions" : {
    "SecretArnList" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    }
  },
  "properties" : {
    "ClusterArn" : {
      "type" : "string"
    },
    "SecretArnList" : {
      "$ref" : "#/definitions/SecretArnList"
    }
  },
  "additionalProperties" : False,
  "required" : [ "ClusterArn" ],
  "createOnlyProperties" : [ "/properties/ClusterArn" ],
  "primaryIdentifier" : [ "/properties/ClusterArn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "kafka:BatchAssociateScramSecret", "kafka:ListScramSecrets", "kms:CreateGrant", "kms:DescribeKey", "secretsmanager:GetSecretValue" ]
    },
    "delete" : {
      "permissions" : [ "kafka:BatchDisassociateScramSecret", "kafka:ListScramSecrets", "kms:CreateGrant", "kms:DescribeKey" ]
    },
    "list" : {
      "permissions" : [ "kafka:ListScramSecrets", "kms:CreateGrant", "kms:DescribeKey", "secretsmanager:GetSecretValue" ],
      "handlerSchema" : {
        "properties" : {
          "ClusterArn" : {
            "$ref" : "resource-schema.json#/properties/ClusterArn"
          }
        },
        "required" : [ "ClusterArn" ]
      }
    },
    "read" : {
      "permissions" : [ "kafka:ListScramSecrets", "kms:CreateGrant", "kms:DescribeKey", "secretsmanager:GetSecretValue" ]
    },
    "update" : {
      "permissions" : [ "kafka:BatchAssociateScramSecret", "kafka:BatchDisassociateScramSecret", "kafka:ListScramSecrets", "kms:CreateGrant", "kms:DescribeKey", "secretsmanager:GetSecretValue" ]
    }
  }
}