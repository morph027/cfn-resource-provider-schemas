SCHEMA = {
  "typeName" : "AWS::AppStream::User",
  "description" : "Resource Type definition for AWS::AppStream::User",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "UserName" : {
      "type" : "string"
    },
    "FirstName" : {
      "type" : "string"
    },
    "MessageAction" : {
      "type" : "string"
    },
    "LastName" : {
      "type" : "string"
    },
    "AuthenticationType" : {
      "type" : "string"
    }
  },
  "required" : [ "UserName", "AuthenticationType" ],
  "createOnlyProperties" : [ "/properties/FirstName", "/properties/MessageAction", "/properties/LastName", "/properties/AuthenticationType", "/properties/UserName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}