SCHEMA = {
  "typeName" : "AWS::Cognito::UserPoolUICustomizationAttachment",
  "description" : "Resource Type definition for AWS::Cognito::UserPoolUICustomizationAttachment",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "properties" : {
    "UserPoolId" : {
      "type" : "string"
    },
    "ClientId" : {
      "type" : "string"
    },
    "CSS" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ "UserPoolId", "ClientId" ],
  "primaryIdentifier" : [ "/properties/UserPoolId", "/properties/ClientId" ],
  "createOnlyProperties" : [ "/properties/UserPoolId", "/properties/ClientId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "cognito-idp:SetUICustomization", "cognito-idp:GetUICustomization" ],
      "timeoutInMinutes" : 2
    },
    "read" : {
      "permissions" : [ "cognito-idp:GetUICustomization" ]
    },
    "update" : {
      "permissions" : [ "cognito-idp:SetUICustomization" ],
      "timeoutInMinutes" : 2
    },
    "delete" : {
      "permissions" : [ "cognito-idp:SetUICustomization", "cognito-idp:GetUICustomization" ],
      "timeoutInMinutes" : 2
    }
  }
}