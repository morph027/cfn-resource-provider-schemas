SCHEMA = {
  "typeName" : "AWS::CodeBuild::SourceCredential",
  "description" : "Resource Type definition for AWS::CodeBuild::SourceCredential",
  "additionalProperties" : False,
  "properties" : {
    "ServerType" : {
      "type" : "string"
    },
    "Token" : {
      "type" : "string"
    },
    "AuthType" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Username" : {
      "type" : "string"
    }
  },
  "required" : [ "ServerType", "Token", "AuthType" ],
  "createOnlyProperties" : [ "/properties/ServerType" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}