SCHEMA = {
  "typeName" : "AWS::OpsWorks::UserProfile",
  "description" : "Resource Type definition for AWS::OpsWorks::UserProfile",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "SshUsername" : {
      "type" : "string"
    },
    "AllowSelfManagement" : {
      "type" : "boolean"
    },
    "IamUserArn" : {
      "type" : "string"
    },
    "SshPublicKey" : {
      "type" : "string"
    }
  },
  "required" : [ "IamUserArn" ],
  "createOnlyProperties" : [ "/properties/IamUserArn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}