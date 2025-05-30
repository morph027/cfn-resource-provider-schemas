SCHEMA = {
  "typeName" : "AWS::AppSync::ApiCache",
  "description" : "Resource Type definition for AWS::AppSync::ApiCache",
  "additionalProperties" : False,
  "properties" : {
    "Type" : {
      "type" : "string"
    },
    "TransitEncryptionEnabled" : {
      "type" : "boolean"
    },
    "HealthMetricsConfig" : {
      "type" : "string"
    },
    "AtRestEncryptionEnabled" : {
      "type" : "boolean"
    },
    "Id" : {
      "type" : "string"
    },
    "ApiId" : {
      "type" : "string"
    },
    "ApiCachingBehavior" : {
      "type" : "string"
    },
    "Ttl" : {
      "type" : "number"
    }
  },
  "required" : [ "Type", "ApiId", "ApiCachingBehavior", "Ttl" ],
  "createOnlyProperties" : [ "/properties/ApiId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}