SCHEMA = {
  "typeName" : "AWS::Cognito::UserPoolUser",
  "description" : "Resource Type definition for AWS::Cognito::UserPoolUser",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "definitions" : {
    "AttributeType" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DesiredDeliveryMediums" : {
      "type" : "array",
      "items" : {
        "type" : "string"
      }
    },
    "ForceAliasCreation" : {
      "type" : "boolean"
    },
    "UserAttributes" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/AttributeType"
      }
    },
    "MessageAction" : {
      "type" : "string"
    },
    "Username" : {
      "type" : "string"
    },
    "UserPoolId" : {
      "type" : "string"
    },
    "ValidationData" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/AttributeType"
      }
    },
    "ClientMetadata" : {
      "type" : "object",
      "patternProperties" : {
        "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    }
  },
  "additionalProperties" : False,
  "required" : [ "UserPoolId" ],
  "primaryIdentifier" : [ "/properties/UserPoolId", "/properties/Username" ],
  "createOnlyProperties" : [ "/properties/DesiredDeliveryMediums", "/properties/ForceAliasCreation", "/properties/UserAttributes", "/properties/Username", "/properties/UserPoolId", "/properties/ValidationData", "/properties/ClientMetadata", "/properties/MessageAction" ],
  "writeOnlyProperties" : [ "/properties/DesiredDeliveryMediums", "/properties/ForceAliasCreation", "/properties/ValidationData", "/properties/ClientMetadata", "/properties/MessageAction" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "cognito-idp:AdminCreateUser", "cognito-idp:AdminGetUser", "iam:PassRole" ],
      "timeoutInMinutes" : 2
    },
    "read" : {
      "permissions" : [ "cognito-idp:AdminGetUser" ]
    },
    "delete" : {
      "permissions" : [ "cognito-idp:AdminDeleteUser" ],
      "timeoutInMinutes" : 2
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "UserPoolId" : {
            "$ref" : "resource-schema.json#/properties/UserPoolId"
          }
        },
        "required" : [ "UserPoolId" ]
      },
      "permissions" : [ "cognito-idp:ListUsers" ]
    }
  }
}