SCHEMA = {
  "typeName" : "AWS::OpenSearchServerless::LifecyclePolicy",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-opensearchserverless",
  "description" : "Amazon OpenSearchServerless lifecycle policy resource",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "definitions" : {
    "LifecyclePolicyType" : {
      "type" : "string",
      "description" : "The type of lifecycle policy",
      "enum" : [ "retention" ]
    }
  },
  "properties" : {
    "Name" : {
      "type" : "string",
      "maxLength" : 32,
      "minLength" : 3,
      "pattern" : "^[a-z][a-z0-9-]+$",
      "description" : "The name of the policy"
    },
    "Type" : {
      "$ref" : "#/definitions/LifecyclePolicyType"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1000,
      "minLength" : 0,
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
      "permissions" : [ "aoss:CreateLifecyclePolicy" ]
    },
    "read" : {
      "permissions" : [ "aoss:BatchGetLifecyclePolicy" ]
    },
    "update" : {
      "permissions" : [ "aoss:UpdateLifecyclePolicy", "aoss:BatchGetLifecyclePolicy" ]
    },
    "delete" : {
      "permissions" : [ "aoss:DeleteLifecyclePolicy" ]
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
      "permissions" : [ "aoss:ListLifecyclePolicies" ]
    }
  },
  "additionalProperties" : False
}