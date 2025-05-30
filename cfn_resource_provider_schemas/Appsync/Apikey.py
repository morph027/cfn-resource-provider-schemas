SCHEMA = {
  "typeName" : "AWS::AppSync::ApiKey",
  "description" : "Resource Type definition for AWS::AppSync::ApiKey",
  "additionalProperties" : False,
  "properties" : {
    "ApiKey" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "ApiKeyId" : {
      "type" : "string"
    },
    "Expires" : {
      "type" : "number"
    },
    "Arn" : {
      "type" : "string"
    },
    "ApiId" : {
      "type" : "string"
    }
  },
  "required" : [ "ApiId" ],
  "createOnlyProperties" : [ "/properties/ApiId" ],
  "primaryIdentifier" : [ "/properties/ApiKeyId" ],
  "readOnlyProperties" : [ "/properties/ApiKeyId", "/properties/ApiKey", "/properties/Arn" ]
}