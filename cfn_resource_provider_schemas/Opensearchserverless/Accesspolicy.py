SCHEMA = {
  "typeName" : "AWS::OpenSearchServerless::AccessPolicy",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-opensearchserverless",
  "description" : "Amazon OpenSearchServerless access policy resource",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "definitions" : {
    "AccessPolicyType" : {
      "type" : "string",
      "description" : "The possible types for the access policy",
      "enum" : [ "data" ]
    }
  },
  "properties" : {
    "Name" : {
      "type" : "string",
      "maxLength" : 32,
      "minLength" : 3,
      "pattern" : "^[a-z][a-z0-9-]{2,31}$",
      "description" : "The name of the policy"
    },
    "Type" : {
      "$ref" : "#/definitions/AccessPolicyType"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1000,
      "minLength" : 1,
      "description" : "The description of the policy"
    },
    "Policy" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 20480,
      "pattern" : "[\\u0009\\u000A\\u000D\\u0020-\\u007E\\u00A1-\\u00FF]+",
      "description" : "The JSON policy document that is the content for the policy"
    }
  },
  "required" : [ "Type", "Name", "Policy" ],
  "createOnlyProperties" : [ "/properties/Type", "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Type", "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "aoss:CreateAccessPolicy", "aoss:GetAccessPolicy" ]
    },
    "read" : {
      "permissions" : [ "aoss:GetAccessPolicy" ]
    },
    "update" : {
      "permissions" : [ "aoss:UpdateAccessPolicy", "aoss:GetAccessPolicy" ]
    },
    "delete" : {
      "permissions" : [ "aoss:DeleteAccessPolicy", "aoss:GetAccessPolicy" ]
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
      "permissions" : [ "aoss:ListAccessPolicies" ]
    }
  },
  "additionalProperties" : False
}