SCHEMA = {
  "typeName" : "AWS::OpenSearchServerless::SecurityPolicy",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-opensearchserverless",
  "description" : "Amazon OpenSearchServerless security policy resource",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "definitions" : {
    "SecurityPolicyType" : {
      "type" : "string",
      "description" : "The possible types for the network policy",
      "enum" : [ "encryption", "network" ]
    }
  },
  "properties" : {
    "Description" : {
      "type" : "string",
      "maxLength" : 1000,
      "minLength" : 1,
      "description" : "The description of the policy"
    },
    "Policy" : {
      "type" : "string",
      "maxLength" : 20480,
      "minLength" : 1,
      "pattern" : "[\\u0009\\u000A\\u000D\\u0020-\\u007E\\u00A1-\\u00FF]+",
      "description" : "The JSON policy document that is the content for the policy"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 32,
      "minLength" : 3,
      "pattern" : "^[a-z][a-z0-9-]{2,31}$",
      "description" : "The name of the policy"
    },
    "Type" : {
      "$ref" : "#/definitions/SecurityPolicyType"
    }
  },
  "required" : [ "Type", "Name", "Policy" ],
  "createOnlyProperties" : [ "/properties/Type", "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Type", "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "aoss:GetSecurityPolicy", "aoss:CreateSecurityPolicy", "kms:DescribeKey", "kms:CreateGrant" ]
    },
    "update" : {
      "permissions" : [ "aoss:GetSecurityPolicy", "aoss:UpdateSecurityPolicy", "kms:DescribeKey", "kms:CreateGrant" ]
    },
    "delete" : {
      "permissions" : [ "aoss:GetSecurityPolicy", "aoss:DeleteSecurityPolicy" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "Type" : {
            "$ref" : "resource-schema.json#/properties/Type"
          }
        },
        "required" : [ "Type" ]
      },
      "permissions" : [ "aoss:ListSecurityPolicies" ]
    },
    "read" : {
      "permissions" : [ "aoss:GetSecurityPolicy", "kms:DescribeKey" ]
    }
  },
  "additionalProperties" : False
}