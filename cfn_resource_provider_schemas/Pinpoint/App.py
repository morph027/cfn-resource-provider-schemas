SCHEMA = {
  "typeName" : "AWS::Pinpoint::App",
  "description" : "Resource Type definition for AWS::Pinpoint::App",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "object"
    },
    "Name" : {
      "type" : "string"
    }
  },
  "required" : [ "Name" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Id" ]
}