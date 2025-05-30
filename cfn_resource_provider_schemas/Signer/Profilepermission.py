SCHEMA = {
  "typeName" : "AWS::Signer::ProfilePermission",
  "description" : "An example resource schema demonstrating some basic constructs and validation rules.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "ProfileName" : {
      "type" : "string",
      "pattern" : "^[0-9a-zA-Z_]{2,64}$"
    },
    "ProfileVersion" : {
      "type" : "string",
      "pattern" : "^[0-9a-zA-Z]{10}$"
    },
    "Action" : {
      "type" : "string"
    },
    "Principal" : {
      "type" : "string"
    },
    "StatementId" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "ProfileName", "Action", "Principal", "StatementId" ],
  "createOnlyProperties" : [ "/properties/ProfileName", "/properties/Action", "/properties/Principal", "/properties/StatementId", "/properties/ProfileVersion" ],
  "primaryIdentifier" : [ "/properties/StatementId", "/properties/ProfileName" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "signer:AddProfilePermission", "signer:ListProfilePermissions" ]
    },
    "read" : {
      "permissions" : [ "signer:ListProfilePermissions" ]
    },
    "delete" : {
      "permissions" : [ "signer:RemoveProfilePermission", "signer:ListProfilePermissions" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ProfileName" : {
            "$ref" : "resource-schema.json#/properties/ProfileName"
          },
          "StatementId" : {
            "$ref" : "resource-schema.json#/properties/StatementId"
          }
        }
      },
      "permissions" : [ "signer:ListProfilePermissions", "signer:GetSigningProfile" ]
    }
  }
}