SCHEMA = {
  "typeName" : "AWS::WorkSpacesWeb::IdentityProvider",
  "description" : "Definition of AWS::WorkSpacesWeb::IdentityProvider Resource Type",
  "definitions" : {
    "IdentityProviderDetails" : {
      "type" : "object",
      "patternProperties" : {
        "^[\\s\\S]*$" : {
          "type" : "string",
          "maxLength" : 131072,
          "minLength" : 0,
          "pattern" : "^[\\s\\S]*$"
        }
      },
      "additionalProperties" : False
    },
    "IdentityProviderType" : {
      "type" : "string",
      "enum" : [ "SAML", "Facebook", "Google", "LoginWithAmazon", "SignInWithApple", "OIDC" ]
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "IdentityProviderArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[\\w+=\\/,.@-]+:[a-zA-Z0-9\\-]+:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\\/[a-fA-F0-9\\-]{36}){2,}$"
    },
    "IdentityProviderDetails" : {
      "$ref" : "#/definitions/IdentityProviderDetails"
    },
    "IdentityProviderName" : {
      "type" : "string",
      "maxLength" : 32,
      "minLength" : 1,
      "pattern" : "^[^_][\\p{L}\\p{M}\\p{S}\\p{N}\\p{P}][^_]+$"
    },
    "IdentityProviderType" : {
      "$ref" : "#/definitions/IdentityProviderType"
    },
    "PortalArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:[\\w+=\\/,.@-]+:[a-zA-Z0-9\\-]+:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:[a-zA-Z]+(\\/[a-fA-F0-9\\-]{36})+$"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 0,
      "insertionOrder" : False
    }
  },
  "required" : [ "IdentityProviderDetails", "IdentityProviderName", "IdentityProviderType" ],
  "readOnlyProperties" : [ "/properties/IdentityProviderArn" ],
  "writeOnlyProperties" : [ "/properties/PortalArn" ],
  "createOnlyProperties" : [ "/properties/PortalArn" ],
  "primaryIdentifier" : [ "/properties/IdentityProviderArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "workspaces-web:CreateIdentityProvider", "workspaces-web:GetIdentityProvider", "workspaces-web:ListTagsForResource", "workspaces-web:TagResource" ]
    },
    "read" : {
      "permissions" : [ "workspaces-web:GetIdentityProvider", "workspaces-web:ListIdentityProviders", "workspaces-web:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "workspaces-web:UpdateIdentityProvider", "workspaces-web:TagResource", "workspaces-web:UntagResource", "workspaces-web:GetIdentityProvider", "workspaces-web:ListIdentityProviders", "workspaces-web:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "workspaces-web:GetIdentityProvider", "workspaces-web:DeleteIdentityProvider" ]
    },
    "list" : {
      "permissions" : [ "workspaces-web:ListIdentityProviders" ],
      "handlerSchema" : {
        "properties" : {
          "PortalArn" : {
            "$ref" : "resource-schema.json#/properties/PortalArn"
          }
        },
        "required" : [ "PortalArn" ]
      }
    }
  },
  "sourceUrl" : "https://github.com/shivankgoel/aws-cloudformation-resource-providers-workspaces-web",
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : True,
    "tagProperty" : "/properties/Tags",
    "tagUpdatable" : True,
    "taggable" : True,
    "permissions" : [ "workspaces-web:UntagResource", "workspaces-web:ListTagsForResource", "workspaces-web:TagResource" ]
  },
  "additionalProperties" : False
}