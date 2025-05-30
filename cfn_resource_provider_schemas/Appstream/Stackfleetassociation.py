SCHEMA = {
  "typeName" : "AWS::AppStream::StackFleetAssociation",
  "description" : "Resource Type definition for AWS::AppStream::StackFleetAssociation",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "FleetName" : {
      "type" : "string"
    },
    "StackName" : {
      "type" : "string"
    }
  },
  "required" : [ "FleetName", "StackName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}