SCHEMA = {
  "typeName" : "AWS::IoT::ThingPrincipalAttachment",
  "description" : "Resource Type definition for AWS::IoT::ThingPrincipalAttachment",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Principal" : {
      "type" : "string"
    },
    "ThingName" : {
      "type" : "string"
    }
  },
  "required" : [ "Principal", "ThingName" ],
  "createOnlyProperties" : [ "/properties/ThingName", "/properties/Principal" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}