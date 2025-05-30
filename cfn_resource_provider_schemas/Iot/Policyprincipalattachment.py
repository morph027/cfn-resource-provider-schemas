SCHEMA = {
  "typeName" : "AWS::IoT::PolicyPrincipalAttachment",
  "description" : "Resource Type definition for AWS::IoT::PolicyPrincipalAttachment",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "PolicyName" : {
      "type" : "string"
    },
    "Principal" : {
      "type" : "string"
    }
  },
  "required" : [ "Principal", "PolicyName" ],
  "createOnlyProperties" : [ "/properties/PolicyName", "/properties/Principal" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}