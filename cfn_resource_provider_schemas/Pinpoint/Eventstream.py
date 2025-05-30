SCHEMA = {
  "typeName" : "AWS::Pinpoint::EventStream",
  "description" : "Resource Type definition for AWS::Pinpoint::EventStream",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ApplicationId" : {
      "type" : "string"
    },
    "DestinationStreamArn" : {
      "type" : "string"
    },
    "RoleArn" : {
      "type" : "string"
    }
  },
  "required" : [ "ApplicationId", "DestinationStreamArn", "RoleArn" ],
  "createOnlyProperties" : [ "/properties/ApplicationId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}