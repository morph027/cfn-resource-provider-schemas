SCHEMA = {
  "typeName" : "AWS::Pinpoint::GCMChannel",
  "description" : "Resource Type definition for AWS::Pinpoint::GCMChannel",
  "additionalProperties" : False,
  "properties" : {
    "Enabled" : {
      "type" : "boolean"
    },
    "ServiceJson" : {
      "type" : "string"
    },
    "DefaultAuthenticationMethod" : {
      "type" : "string"
    },
    "ApiKey" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "ApplicationId" : {
      "type" : "string"
    }
  },
  "required" : [ "ApplicationId" ],
  "createOnlyProperties" : [ "/properties/ApplicationId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}