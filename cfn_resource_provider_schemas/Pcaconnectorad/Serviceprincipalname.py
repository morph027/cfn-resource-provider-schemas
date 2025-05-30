SCHEMA = {
  "typeName" : "AWS::PCAConnectorAD::ServicePrincipalName",
  "description" : "Definition of AWS::PCAConnectorAD::ServicePrincipalName Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-pcaconnectorad",
  "properties" : {
    "ConnectorArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:[\\w-]+:pca-connector-ad:[\\w-]+:[0-9]+:connector(\\/[\\w-]+)$"
    },
    "DirectoryRegistrationArn" : {
      "type" : "string",
      "maxLength" : 200,
      "minLength" : 5,
      "pattern" : "^arn:[\\w-]+:pca-connector-ad:[\\w-]+:[0-9]+:directory-registration(\\/[\\w-]+)$"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "createOnlyProperties" : [ "/properties/ConnectorArn", "/properties/DirectoryRegistrationArn" ],
  "primaryIdentifier" : [ "/properties/ConnectorArn", "/properties/DirectoryRegistrationArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "ds:UpdateAuthorizedApplication", "pca-connector-ad:GetServicePrincipalName", "pca-connector-ad:CreateServicePrincipalName" ]
    },
    "read" : {
      "permissions" : [ "pca-connector-ad:GetServicePrincipalName" ]
    },
    "delete" : {
      "permissions" : [ "ds:UpdateAuthorizedApplication", "pca-connector-ad:GetServicePrincipalName", "pca-connector-ad:DeleteServicePrincipalName" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "DirectoryRegistrationArn" : {
            "$ref" : "resource-schema.json#/properties/DirectoryRegistrationArn"
          }
        },
        "required" : [ "DirectoryRegistrationArn" ]
      },
      "permissions" : [ "pca-connector-ad:ListServicePrincipalNames" ]
    }
  },
  "additionalProperties" : False
}