SCHEMA = {
  "typeName" : "AWS::Pinpoint::EmailChannel",
  "description" : "Resource Type definition for AWS::Pinpoint::EmailChannel",
  "additionalProperties" : False,
  "properties" : {
    "ConfigurationSet" : {
      "type" : "string"
    },
    "FromAddress" : {
      "type" : "string"
    },
    "OrchestrationSendingRoleArn" : {
      "type" : "string"
    },
    "Enabled" : {
      "type" : "boolean"
    },
    "Id" : {
      "type" : "string"
    },
    "ApplicationId" : {
      "type" : "string"
    },
    "Identity" : {
      "type" : "string"
    },
    "RoleArn" : {
      "type" : "string"
    }
  },
  "required" : [ "FromAddress", "ApplicationId", "Identity" ],
  "createOnlyProperties" : [ "/properties/ApplicationId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}