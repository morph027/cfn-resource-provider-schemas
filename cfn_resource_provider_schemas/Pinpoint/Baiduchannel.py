SCHEMA = {
  "typeName" : "AWS::Pinpoint::BaiduChannel",
  "description" : "Resource Type definition for AWS::Pinpoint::BaiduChannel",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "SecretKey" : {
      "type" : "string"
    },
    "ApiKey" : {
      "type" : "string"
    },
    "Enabled" : {
      "type" : "boolean"
    },
    "ApplicationId" : {
      "type" : "string"
    }
  },
  "required" : [ "ApplicationId", "SecretKey", "ApiKey" ],
  "createOnlyProperties" : [ "/properties/ApplicationId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}