SCHEMA = {
  "typeName" : "AWS::Pinpoint::SMSChannel",
  "description" : "Resource Type definition for AWS::Pinpoint::SMSChannel",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ShortCode" : {
      "type" : "string"
    },
    "Enabled" : {
      "type" : "boolean"
    },
    "ApplicationId" : {
      "type" : "string"
    },
    "SenderId" : {
      "type" : "string"
    }
  },
  "required" : [ "ApplicationId" ],
  "createOnlyProperties" : [ "/properties/ApplicationId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}