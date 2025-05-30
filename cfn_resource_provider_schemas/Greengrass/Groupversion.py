SCHEMA = {
  "typeName" : "AWS::Greengrass::GroupVersion",
  "description" : "Resource Type definition for AWS::Greengrass::GroupVersion",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
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
    },
    "GroupId" : {
      "type" : "string"
    }
  },
  "required" : [ "GroupId" ],
  "createOnlyProperties" : [ "/properties/CoreDefinitionVersionArn", "/properties/DeviceDefinitionVersionArn", "/properties/ConnectorDefinitionVersionArn", "/properties/SubscriptionDefinitionVersionArn", "/properties/LoggerDefinitionVersionArn", "/properties/GroupId", "/properties/ResourceDefinitionVersionArn", "/properties/FunctionDefinitionVersionArn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}