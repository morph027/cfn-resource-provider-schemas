SCHEMA = {
  "typeName" : "AWS::AppStream::StackUserAssociation",
  "description" : "Resource Type definition for AWS::AppStream::StackUserAssociation",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "SendEmailNotification" : {
      "type" : "boolean"
    },
    "UserName" : {
      "type" : "string"
    },
    "StackName" : {
      "type" : "string"
    },
    "AuthenticationType" : {
      "type" : "string"
    }
  },
  "required" : [ "StackName", "UserName", "AuthenticationType" ],
  "createOnlyProperties" : [ "/properties/StackName", "/properties/AuthenticationType", "/properties/SendEmailNotification", "/properties/UserName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}