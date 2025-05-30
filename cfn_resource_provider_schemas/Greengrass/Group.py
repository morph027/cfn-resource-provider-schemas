SCHEMA = {
  "typeName" : "AWS::Greengrass::Group",
  "description" : "Resource Type definition for AWS::Greengrass::Group",
  "additionalProperties" : False,
  "properties" : {
    "RoleAttachedAt" : {
      "type" : "string"
    },
    "LatestVersionArn" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "RoleArn" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string"
    },
    "InitialVersion" : {
      "$ref" : "#/definitions/GroupVersion"
    },
    "Tags" : {
      "type" : "object"
    }
  },
  "definitions" : {
    "GroupVersion" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "LoggerDefinitionVersionArn" : {
          "type" : "string"
        },
        "DeviceDefinitionVersionArn" : {
          "type" : "string"
        },
        "FunctionDefinitionVersionArn" : {
          "type" : "string"
        },
        "CoreDefinitionVersionArn" : {
          "type" : "string"
        },
        "ResourceDefinitionVersionArn" : {
          "type" : "string"
        },
        "ConnectorDefinitionVersionArn" : {
          "type" : "string"
        },
        "SubscriptionDefinitionVersionArn" : {
          "type" : "string"
        }
      }
    }
  },
  "required" : [ "Name" ],
  "readOnlyProperties" : [ "/properties/LatestVersionArn", "/properties/RoleAttachedAt", "/properties/Id", "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/InitialVersion" ],
  "primaryIdentifier" : [ "/properties/Id" ]
}