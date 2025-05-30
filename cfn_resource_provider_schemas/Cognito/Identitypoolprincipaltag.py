SCHEMA = {
  "typeName" : "AWS::Cognito::IdentityPoolPrincipalTag",
  "description" : "Resource Type definition for AWS::Cognito::IdentityPoolPrincipalTag",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "properties" : {
    "IdentityPoolId" : {
      "type" : "string"
    },
    "IdentityProviderName" : {
      "type" : "string"
    },
    "UseDefaults" : {
      "type" : "boolean"
    },
    "PrincipalTags" : {
      "type" : "object"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "additionalProperties" : False,
  "required" : [ "IdentityPoolId", "IdentityProviderName" ],
  "createOnlyProperties" : [ "/properties/IdentityPoolId", "/properties/IdentityProviderName" ],
  "primaryIdentifier" : [ "/properties/IdentityPoolId", "/properties/IdentityProviderName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "cognito-identity:GetPrincipalTagAttributeMap", "cognito-identity:SetPrincipalTagAttributeMap" ]
    },
    "read" : {
      "permissions" : [ "cognito-identity:GetPrincipalTagAttributeMap" ]
    },
    "update" : {
      "permissions" : [ "cognito-identity:GetPrincipalTagAttributeMap", "cognito-identity:SetPrincipalTagAttributeMap" ]
    },
    "delete" : {
      "permissions" : [ "cognito-identity:GetPrincipalTagAttributeMap", "cognito-identity:SetPrincipalTagAttributeMap" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "IdentityPoolId" : {
            "$ref" : "resource-schema.json#/properties/IdentityPoolId"
          },
          "IdentityProviderName" : {
            "$ref" : "resource-schema.json#/properties/IdentityProviderName"
          }
        },
        "required" : [ "IdentityPoolId", "IdentityProviderName" ]
      },
      "permissions" : [ "cognito-identity:GetPrincipalTagAttributeMap" ]
    }
  }
}