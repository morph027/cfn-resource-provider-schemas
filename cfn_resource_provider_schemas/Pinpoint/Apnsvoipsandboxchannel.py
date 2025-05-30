SCHEMA = {
  "typeName" : "AWS::Pinpoint::APNSVoipSandboxChannel",
  "description" : "Resource Type definition for AWS::Pinpoint::APNSVoipSandboxChannel",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "BundleId" : {
      "type" : "string"
    },
    "PrivateKey" : {
      "type" : "string"
    },
    "Enabled" : {
      "type" : "boolean"
    },
    "DefaultAuthenticationMethod" : {
      "type" : "string"
    },
    "TokenKey" : {
      "type" : "string"
    },
    "ApplicationId" : {
      "type" : "string"
    },
    "TeamId" : {
      "type" : "string"
    },
    "Certificate" : {
      "type" : "string"
    },
    "TokenKeyId" : {
      "type" : "string"
    }
  },
  "required" : [ "ApplicationId" ],
  "createOnlyProperties" : [ "/properties/ApplicationId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}